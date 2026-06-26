"""
Camada de Persistência (Data Layer) - Mochila Cheia

Concentra o acesso ao banco SQLite. Os módulos de negócio NÃO abrem conexões
diretamente: eles passam pela função get_db(), que devolve uma conexão única
por requisição (armazenada em flask.g) e é fechada automaticamente no fim.

Isso isola a tecnologia de banco do restante do sistema — se um dia trocarmos
SQLite por PostgreSQL, apenas esta camada muda.

Responsável: Rodrigo (infra) — repositórios concretos: Júlio (Backend e Análise de Fluxo)
"""

import sqlite3
from pathlib import Path

from flask import current_app, g


def get_db() -> sqlite3.Connection:
    """
    Retorna a conexão SQLite da requisição atual.

    Cria a conexão na primeira chamada e a reaproveita nas seguintes (padrão
    "uma conexão por requisição"). Configura row_factory para acessar colunas
    pelo nome (row["titulo"]) e ativa as foreign keys.
    """
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE_PATH"],
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        g.db.row_factory = sqlite3.Row          # acesso por nome de coluna
        g.db.execute("PRAGMA foreign_keys = ON")  # integridade referencial
    return g.db


def close_db(exception=None) -> None:
    """Fecha a conexão ao fim da requisição (registrado em teardown)."""
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db() -> None:
    """
    (Re)cria o banco a partir de schema.sql e carrega seed.sql.

    Executado pelo comando `flask --app run init-db`. Útil para preparar o
    ambiente de demonstração rapidamente.
    """
    db = get_db()
    schema_path = Path(current_app.config["SCHEMA_PATH"])
    seed_path = Path(current_app.config["SEED_PATH"])

    if schema_path.exists():
        db.executescript(schema_path.read_text(encoding="utf-8"))
    if seed_path.exists():
        db.executescript(seed_path.read_text(encoding="utf-8"))
    db.commit()


def init_app(app) -> None:
    """Liga o ciclo de vida do banco à aplicação (chamado pela app factory)."""
    app.teardown_appcontext(close_db)

    @app.cli.command("init-db")
    def init_db_command():
        """Comando de terminal: recria o banco e carrega os dados de exemplo."""
        init_db()
        print("✅ Banco inicializado a partir de schema.sql + seed.sql")
