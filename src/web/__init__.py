"""
Mochila Cheia - MVP Web (Flask)
===============================

Application Factory: ponto único de criação e configuração da aplicação web.
Concentra a inicialização das camadas e o registro dos módulos (blueprints),
mantendo o app desacoplado e testável.

Arquitetura (MVC em camadas):

    Apresentação (Jinja/templates + static)
            │
    Controle  (blueprints/*  — rotas Flask)
            │
    Domínio   (src/models/*  — classes POO: regras de negócio)
            │
    Persistência (database.py + repositories/* — SQLite)

Responsável: Rodrigo (Gestão, Comunicação e Arquitetura)
"""

from flask import Flask

from src.web.config import config_por_nome


def create_app(ambiente: str = "default") -> Flask:
    """
    Cria e configura a instância da aplicação Flask.

    Args:
        ambiente: chave de configuração ("development", "production", "default").

    Returns:
        Aplicação Flask pronta para rodar.
    """
    app = Flask(__name__)
    app.config.from_object(config_por_nome.get(ambiente, config_por_nome["default"]))

    # Camada de persistência (conexão por requisição + comando init-db)
    from src.web import database
    database.init_app(app)

    # Camada de controle (registro dos módulos/blueprints)
    from src.web.blueprints import registrar_blueprints
    registrar_blueprints(app)

    return app
