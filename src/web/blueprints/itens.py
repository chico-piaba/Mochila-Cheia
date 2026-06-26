"""
Módulo de Itens (Controller) - Mochila Cheia

Telas de itens (design do Figma): listagem/busca, meus itens (doador),
publicar, editar e detalhes (visão doador e visão receptor).

>>> A LIGAR AO BACKEND — Responsável: Júlio (Backend e Análise de Fluxo)
    Criar ItemRepository e usar a classe de domínio Item (fluxo de status).
    A busca da home (home.index) já lê itens reais — usar como referência.
"""

from flask import Blueprint, render_template

from src.web.repositories import EstatisticasRepository

itens_bp = Blueprint("itens", __name__)


@itens_bp.route("/")
def listar():
    """
    Busca/listagem de itens com dados reais (reusa a tela de busca index.html).
    TODO Júlio: aplicar o filtro de texto (?q=) e categoria via ItemRepository.
    """
    repo = EstatisticasRepository()
    return render_template(
        "index.html",
        resumo=repo.resumo(),
        itens=repo.itens_disponiveis(limite=24),
        nav_ativa="home",
    )


@itens_bp.route("/meus")
def meus():
    """Meus itens (doador). TODO Júlio: itens do doador logado."""
    return render_template("itens/meus.html", nav_ativa="home")


@itens_bp.route("/publicar")
def publicar():
    """Cadastrar item (Figma). TODO Júlio: criar Item no POST."""
    return render_template("itens/publicar.html", nav_ativa="home")


@itens_bp.route("/<int:id_item>")
def detalhe(id_item):
    """Detalhe do item (visão receptor). TODO Júlio: carregar item real."""
    return render_template("itens/detalhe.html", id_item=id_item, nav_ativa="home")


@itens_bp.route("/<int:id_item>/doador")
def detalhe_doador(id_item):
    """Detalhe do item (visão doador). TODO Júlio: carregar item real."""
    return render_template("itens/detalhe_doador.html", id_item=id_item, nav_ativa="home")


@itens_bp.route("/<int:id_item>/editar")
def editar(id_item):
    """Editar item (Figma). TODO Júlio: atualizar Item no POST."""
    return render_template("itens/editar.html", id_item=id_item, nav_ativa="home")
