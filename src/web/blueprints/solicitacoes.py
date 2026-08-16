"""
Módulo de Solicitações (Controller) - Mochila Cheia

Fluxo de doação completo: o receptor solicita um item e acompanha seus pedidos;
o doador recebe as solicitações e decide aceitar ou recusar. Cada ação dispara
uma notificação interna para a outra parte.

Responsável: Júlio (Backend e Análise de Fluxo)
"""

from flask import (
    Blueprint, render_template, redirect, url_for, flash, abort
)

from src.web.repositories import (
    SolicitacaoRepository, ItemRepository, NotificacaoRepository
)
from src.web.sessao import usuario_logado, login_obrigatorio

solicitacoes_bp = Blueprint("solicitacoes", __name__)


@solicitacoes_bp.route("/minhas")
@login_obrigatorio
def minhas():
    """Solicitações feitas pelo usuário logado (lado receptor)."""
    solicitacoes = SolicitacaoRepository().listar_por_receptor(usuario_logado()["id"])
    return render_template(
        "solicitacoes/minhas.html",
        solicitacoes=solicitacoes,
        nav_ativa="solicitacoes",
    )


@solicitacoes_bp.route("/recebidas")
@login_obrigatorio
def recebidas():
    """Solicitações recebidas nos itens do usuário logado (lado doador)."""
    solicitacoes = SolicitacaoRepository().listar_recebidas(usuario_logado()["id"])
    return render_template(
        "solicitacoes/recebidas.html",
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

    id_solic = repo.criar(id_item, usuario["id"])
    NotificacaoRepository().criar(
        usuario_destino_id=item["doador_id"],
        titulo="Nova solicitação recebida!",
        mensagem=f'{usuario["nome"]} solicitou seu item "{item["titulo"]}".',
        item_id=id_item,
        solicitacao_id=id_solic,
    )
    flash("Solicitação enviada ao doador!", "sucesso")
    return redirect(url_for("solicitacoes.minhas"))


@solicitacoes_bp.route("/<int:id_solicitacao>/aceitar", methods=["POST"])
@login_obrigatorio
def aceitar(id_solicitacao):
    """Doador aceita a solicitação (reserva o item e avisa o receptor)."""
    repo = SolicitacaoRepository()
    solic = repo.buscar(id_solicitacao)
    if solic is None:
        abort(404)
    if solic["doador_id"] != usuario_logado()["id"]:
        abort(403)

    repo.aceitar(id_solicitacao)
    NotificacaoRepository().criar(
        usuario_destino_id=solic["receptor_id"],
        titulo="Sua solicitação foi aceita!",
        mensagem=f'{solic["doador_nome"]} aceitou sua solicitação para '
                 f'"{solic["item_titulo"]}". Combine a retirada pelo chat.',
        item_id=solic["item_id"],
        solicitacao_id=id_solicitacao,
    )
    flash("Solicitação aceita! O receptor foi notificado.", "sucesso")
    return redirect(url_for("solicitacoes.recebidas"))


@solicitacoes_bp.route("/<int:id_solicitacao>/recusar", methods=["POST"])
@login_obrigatorio
def recusar(id_solicitacao):
    """Doador recusa a solicitação (avisa o receptor)."""
    repo = SolicitacaoRepository()
    solic = repo.buscar(id_solicitacao)
    if solic is None:
        abort(404)
    if solic["doador_id"] != usuario_logado()["id"]:
        abort(403)

    repo.recusar(id_solicitacao)
    NotificacaoRepository().criar(
        usuario_destino_id=solic["receptor_id"],
        titulo="Solicitação recusada",
        mensagem=f'Sua solicitação para "{solic["item_titulo"]}" não foi aceita desta vez.',
        item_id=solic["item_id"],
        solicitacao_id=id_solicitacao,
    )
    flash("Solicitação recusada.", "aviso")
    return redirect(url_for("solicitacoes.recebidas"))


@solicitacoes_bp.route("/confirmar")
def confirmar():
    """Tela de confirmação de solicitação (design do Figma)."""
    return render_template("solicitacoes/confirmar.html", nav_ativa="solicitacoes")
