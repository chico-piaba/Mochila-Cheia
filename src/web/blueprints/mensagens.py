"""
Módulo de Mensagens / Chat (Controller) - Mochila Cheia

Chat interno entre doador e receptor, ancorado a uma solicitação. Lista as
conversas do usuário, exibe o histórico e envia novas mensagens, sempre
notificando a outra parte.

Responsável: Lucas (IHC/UX) + Júlio (Backend)
"""

from flask import (
    Blueprint, render_template, request, redirect, url_for, flash, abort
)

from src.web.repositories import MensagemRepository, NotificacaoRepository
from src.web.sessao import usuario_logado, login_obrigatorio

mensagens_bp = Blueprint("mensagens", __name__)


@mensagens_bp.route("/")
@login_obrigatorio
def conversas():
    """Lista de conversas do usuário logado."""
    conversas = MensagemRepository().listar_conversas(usuario_logado()["id"])
    return render_template(
        "mensagens/conversas.html", conversas=conversas, nav_ativa="mensagens"
    )


@mensagens_bp.route("/<int:id_solicitacao>", methods=["GET", "POST"])
@login_obrigatorio
def conversa(id_solicitacao):
    """Histórico da conversa e envio de mensagens (contexto: uma solicitação)."""
    repo = MensagemRepository()
    contexto = repo.contexto(id_solicitacao)
    if contexto is None:
        abort(404)

    usuario = usuario_logado()
    # Só os dois participantes (doador e receptor) acessam a conversa
    if usuario["id"] not in (contexto["doador_id"], contexto["receptor_id"]):
        abort(403)

    # Identifica quem é o outro participante (destinatário das mensagens)
    if usuario["id"] == contexto["doador_id"]:
        outro_id, outro_nome = contexto["receptor_id"], contexto["receptor_nome"]
    else:
        outro_id, outro_nome = contexto["doador_id"], contexto["doador_nome"]

    if request.method == "POST":
        texto = request.form.get("conteudo", "").strip()
        if texto:
            repo.enviar(id_solicitacao, usuario["id"], outro_id, texto)
            NotificacaoRepository().criar(
                usuario_destino_id=outro_id,
                titulo="Nova mensagem recebida",
                mensagem=f'{usuario["nome"]} enviou uma mensagem sobre '
                         f'"{contexto["item_titulo"]}".',
                solicitacao_id=id_solicitacao,
                link_destino=url_for("mensagens.conversa", id_solicitacao=id_solicitacao),
            )
        return redirect(url_for("mensagens.conversa", id_solicitacao=id_solicitacao))

    repo.marcar_lidas(id_solicitacao, usuario["id"])
    mensagens = repo.listar_mensagens(id_solicitacao)
    return render_template(
        "mensagens/conversa.html",
        mensagens=mensagens,
        contexto=contexto,
        outro_nome=outro_nome,
        eu_id=usuario["id"],
        id_solicitacao=id_solicitacao,
        nav_ativa="mensagens",
    )
