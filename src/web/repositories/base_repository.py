"""
BaseRepository - padrão Repository (infra) - Mochila Cheia

Define operações genéricas de leitura sobre uma tabela, evitando repetição de
SQL boilerplate nos repositórios concretos. Cada repositório de domínio (Item,
Usuario, Solicitacao…) herda desta base e adiciona apenas as consultas
específicas do seu agregado.

Responsável: Rodrigo (infra/padrão) — repositórios concretos: Júlio
"""

from typing import Optional

from src.web.database import get_db


class BaseRepository:
    """
    Repositório base com CRUD de leitura genérico.

    Subclasses devem definir:
        tabela    -> nome da tabela no banco
        chave     -> nome da coluna de chave primária
    """

    tabela: str = ""
    chave: str = "id"

    def _conn(self):
        """Atalho para a conexão da requisição atual."""
        return get_db()

    def listar(self, ordenar_por: Optional[str] = None) -> list:
        """Retorna todas as linhas da tabela (opcionalmente ordenadas)."""
        sql = f"SELECT * FROM {self.tabela}"
        if ordenar_por:
            sql += f" ORDER BY {ordenar_por}"
        return self._conn().execute(sql).fetchall()

    def buscar_por_id(self, id_valor):
        """Retorna uma única linha pela chave primária, ou None."""
        sql = f"SELECT * FROM {self.tabela} WHERE {self.chave} = ?"
        return self._conn().execute(sql, (id_valor,)).fetchone()

    def contar(self) -> int:
        """Conta o total de linhas da tabela."""
        sql = f"SELECT COUNT(*) AS total FROM {self.tabela}"
        return self._conn().execute(sql).fetchone()["total"]
