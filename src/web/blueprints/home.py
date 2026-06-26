"""
Módulo Home (Controller) - Mochila Cheia

Página inicial / busca do receptor. É o EXEMPLO VIVO da arquitetura: busca os
itens disponíveis no banco (via repositório) e renderiza com o design do Figma.

    Navegador -> home.index -> EstatisticasRepository -> SQLite -> index.html

Responsável: Rodrigo (núcleo + dados reais)
A fazer (Júlio): ligar a barra de busca/filtros a ItemRepository.
"""

from flask import Blueprint, render_template

from src.web.repositories import EstatisticasRepository

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def index():
    """Home/busca (receptor) com itens reais do banco."""
    repo = EstatisticasRepository()
    return render_template(
        "index.html",
        resumo=repo.resumo(),
        itens=repo.itens_disponiveis(limite=12),
        nav_ativa="home",
    )


@home_bp.route("/doador")
def doador():
    """Home do doador (dashboard). TODO Júlio: ligar a dados reais do doador logado."""
    return render_template("home_doador.html", nav_ativa="home")


@home_bp.route("/splash")
def splash():
    """Tela de abertura (splash). Estática."""
    return render_template("splash.html", sem_nav=True)
