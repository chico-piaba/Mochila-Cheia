"""
Módulo de Notificações (Controller) - Mochila Cheia

Central de alertas do usuário (solicitação recebida/aceita, item aprovado,
nova mensagem). Lista as notificações reais e as marca como lidas ao abrir.

Responsável: Lucas (IHC/UX) + Júlio (Backend)
"""

from flask import Blueprint, render_template

from src.web.repositories import NotificacaoRepository
from src.web.sessao import usuario_logado, login_obrigatorio

notificacoes_bp = Blueprint("notificacoes", __name__)


@notificacoes_bp.route("/")
@login_obrigatorio
def listar():
    """Notificações do usuário logado (marcadas como lidas ao visualizar)."""
    repo = NotificacaoRepository()
    usuario_id = usuario_logado()["id"]
    notificacoes = repo.listar(usuario_id)
    repo.marcar_todas_lidas(usuario_id)
    return render_template(
        "notificacoes/listar.html", notificacoes=notificacoes, nav_ativa="home"
    )
