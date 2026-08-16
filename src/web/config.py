"""
Configuração da aplicação web - Mochila Cheia

Centraliza os parâmetros de configuração do MVP Web (Flask).
Mantém as decisões de ambiente fora do código dos módulos (separação de
responsabilidades), facilitando a troca entre desenvolvimento e produção.

Responsável: Rodrigo (Gestão, Comunicação e Arquitetura)
"""

import os
from pathlib import Path

# Raiz do projeto (…/Mochila Cheia - Projeto Integrado)
BASE_DIR = Path(__file__).resolve().parents[2]
DATABASE_DIR = BASE_DIR / "database"


class Config:
    """Configuração base, compartilhada por todos os ambientes."""

    # Chave usada para assinar a sessão (login). Em produção deve vir do ambiente.
    SECRET_KEY = os.environ.get("MOCHILA_SECRET_KEY", "dev-mochila-cheia-trocar-em-producao")

    # Caminho do banco SQLite (desenvolvimento). Em produção: PostgreSQL.
    DATABASE_PATH = os.environ.get("MOCHILA_DB", str(DATABASE_DIR / "mochila_cheia.db"))

    # Scripts de criação e carga inicial do banco (Projeto Físico - EP2/PI2)
    SCHEMA_PATH = str(DATABASE_DIR / "schema.sql")
    SEED_PATH = str(DATABASE_DIR / "seed.sql")

    # Quantidade de itens por página na busca/listagem
    ITENS_POR_PAGINA = 12

    # Upload de fotos dos itens (salvas em static/uploads e servidas pelo Flask)
    UPLOAD_FOLDER = str(Path(__file__).resolve().parent / "static" / "uploads")
    EXTENSOES_IMAGEM = {"png", "jpg", "jpeg", "gif", "webp"}
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB por upload


class DevelopmentConfig(Config):
    """Ambiente de desenvolvimento (padrão para o MVP acadêmico)."""
    DEBUG = True


class ProductionConfig(Config):
    """Ambiente de produção (referência para evolução do projeto)."""
    DEBUG = False


# Mapeamento usado pela app factory para escolher o ambiente.
config_por_nome = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
