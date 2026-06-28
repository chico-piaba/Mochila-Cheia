"""
Módulo de Moderação (Controller) - Mochila Cheia

Fila de itens pendentes e ações de aprovar/recusar. Rotas protegidas para o
perfil 'moderador'. Liga as telas do Figma ao ItemRepository.

Responsável: Júlio (Backend e Análise de Fluxo)
"""

from flask import (
    Blueprint, render_template, redirect, url_for, flash, abort
)

from src.web.repositories import ItemRepository
from src.web.sessao import usuario_logado, login_obrigatorio

moderacao_bp = Blueprint("moderacao", __name__)


def _exige_moderador():
    """Bloqueia o acesso de quem não for moderador."""
    usuario = usuario_logado()
    if usuario is None or usuario["tipo"] != "moderador":
        abort(403)


@moderacao_bp.route("/")
@login_obrigatorio
def fila():
    """Fila de itens aguardando moderação."""
    _exige_moderador()
    itens = ItemRepository().listar_pendentes()
    return render_template("moderacao/fila.html", itens=itens, nav_ativa="home")


@moderacao_bp.route("/painel")
@login_obrigatorio
def painel():
    """Painel do moderador."""
    _exige_moderador()
    itens = ItemRepository().listar_pendentes()
    return render_template("moderacao/painel.html", itens=itens, nav_ativa="home")


@moderacao_bp.route("/<int:id_item>/revisar")
@login_obrigatorio
def revisar(id_item):
    """Tela de revisão de um item pendente."""
    _exige_moderador()
    item = ItemRepository().buscar_detalhe(id_item)
    if item is None:
        abort(404)
    return render_template("moderacao/revisar.html", item=item, nav_ativa="home")


@moderacao_bp.route("/<int:id_item>/aprovar", methods=["POST"])
@login_obrigatorio
def aprovar(id_item):
    """Aprova o item, tornando-o disponível no catálogo."""
    _exige_moderador()
    ItemRepository().aprovar(id_item, usuario_logado()["id"])
    flash("Item aprovado e publicado no catálogo.", "sucesso")
    return redirect(url_for("moderacao.fila"))


@moderacao_bp.route("/<int:id_item>/recusar", methods=["POST"])
@login_obrigatorio
def recusar(id_item):
    """Recusa o item, mantendo o catálogo confiável."""
    _exige_moderador()
    ItemRepository().recusar(id_item, usuario_logado()["id"])
    flash("Item recusado.", "aviso")
    return redirect(url_for("moderacao.fila"))
