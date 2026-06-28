"""
Módulo de Solicitações (Controller) - Mochila Cheia

Fluxo de doação: o receptor solicita um item disponível e acompanha suas
solicitações. Liga as telas do Figma ao SolicitacaoRepository.

Responsável: Júlio (Backend e Análise de Fluxo)
"""

from flask import (
    Blueprint, render_template, redirect, url_for, flash, abort
)

from src.web.repositories import SolicitacaoRepository, ItemRepository
from src.web.sessao import usuario_logado, login_obrigatorio

solicitacoes_bp = Blueprint("solicitacoes", __name__)


@solicitacoes_bp.route("/minhas")
@login_obrigatorio
def minhas():
    """Solicitações do usuário logado."""
    solicitacoes = SolicitacaoRepository().listar_por_receptor(usuario_logado()["id"])
    return render_template(
        "solicitacoes/minhas.html",
        solicitacoes=solicitacoes,
        nav_ativa="solicitacoes",
    )


@solicitacoes_bp.route("/nova/<int:id_item>", methods=["GET", "POST"])
@login_obrigatorio
def nova(id_item):
    """Confirma e cria uma solicitação para o item informado."""
    item = ItemRepository().buscar_detalhe(id_item)
    if item is None:
        abort(404)

    usuario = usuario_logado()
    if item["doador_id"] == usuario["id"]:
        flash("Você não pode solicitar um item que você mesmo publicou.", "erro")
        return redirect(url_for("itens.detalhe", id_item=id_item))

    repo = SolicitacaoRepository()
    if repo.ja_solicitou(id_item, usuario["id"]):
        flash("Você já solicitou este item.", "aviso")
        return redirect(url_for("solicitacoes.minhas"))

    repo.criar(id_item, usuario["id"])
    flash("Solicitação enviada ao doador!", "sucesso")
    return redirect(url_for("solicitacoes.minhas"))


@solicitacoes_bp.route("/confirmar")
def confirmar():
    """Tela de confirmação de solicitação (design do Figma)."""
    return render_template("solicitacoes/confirmar.html", nav_ativa="solicitacoes")
