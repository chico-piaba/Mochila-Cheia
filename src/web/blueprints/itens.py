"""
Módulo de Itens (Controller) - Mochila Cheia

Busca/listagem, meus itens (doador), publicação, edição e detalhes. Liga as
telas do Figma ao backend usando ItemRepository e CategoriaRepository.

Responsável: Júlio (Backend e Análise de Fluxo)
"""

from flask import (
    Blueprint, render_template, request, redirect, url_for, flash, abort
)

from src.web.repositories import (
    EstatisticasRepository, ItemRepository, CategoriaRepository
)
from src.web.repositories.item_repository import ESTADO_FORM_PARA_BD
from src.web.sessao import usuario_logado, login_obrigatorio

itens_bp = Blueprint("itens", __name__)


@itens_bp.route("/")
def listar():
    """Busca/listagem de itens disponíveis (reusa a tela de busca index.html)."""
    repo = EstatisticasRepository()
    return render_template(
        "index.html",
        resumo=repo.resumo(),
        itens=repo.itens_disponiveis(limite=24),
        nav_ativa="home",
    )


@itens_bp.route("/meus")
@login_obrigatorio
def meus():
    """Itens publicados pelo doador logado."""
    itens = ItemRepository().listar_por_doador(usuario_logado()["id"])
    return render_template("itens/meus.html", itens=itens, nav_ativa="home")


@itens_bp.route("/publicar", methods=["GET", "POST"])
@login_obrigatorio
def publicar():
    """Publica um novo item (nasce pendente de moderação)."""
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        descricao = request.form.get("descricao", "").strip()
        categoria_nome = request.form.get("categoria", "")
        estado_form = request.form.get("estado", "")

        estado_bd = ESTADO_FORM_PARA_BD.get(estado_form)
        if not titulo or not categoria_nome or not estado_bd:
            flash("Preencha título, categoria e estado de conservação.", "erro")
            return render_template("itens/publicar.html", nav_ativa="home")

        usuario = usuario_logado()
        categoria_id = CategoriaRepository().id_por_nome(categoria_nome)
        ItemRepository().criar(
            titulo=titulo,
            descricao=descricao,
            categoria_id=categoria_id,
            estado_conservacao=estado_bd,
            doador_id=usuario["id"],
        )
        flash("Item publicado! Aguardando aprovação da moderação.", "sucesso")
        return redirect(url_for("itens.meus"))

    return render_template("itens/publicar.html", nav_ativa="home")


@itens_bp.route("/<int:id_item>")
def detalhe(id_item):
    """Detalhe do item (visão receptor)."""
    item = ItemRepository().buscar_detalhe(id_item)
    if item is None:
        abort(404)
    return render_template("itens/detalhe.html", item=item, nav_ativa="home")


@itens_bp.route("/<int:id_item>/doador")
def detalhe_doador(id_item):
    """Detalhe do item (visão doador)."""
    item = ItemRepository().buscar_detalhe(id_item)
    if item is None:
        abort(404)
    return render_template("itens/detalhe_doador.html", item=item, nav_ativa="home")


@itens_bp.route("/<int:id_item>/editar")
@login_obrigatorio
def editar(id_item):
    """Editar item (form do Figma). Atualização no POST prevista para a próxima iteração."""
    item = ItemRepository().buscar_detalhe(id_item)
    if item is None:
        abort(404)
    return render_template("itens/editar.html", item=item, nav_ativa="home")
