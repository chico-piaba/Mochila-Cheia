"""
Módulo de Notificações (Controller) - Mochila Cheia

Alertas do sistema para o usuário (item aprovado, nova solicitação, doação
finalizada). Lê/escreve na tabela NOTIFICACAO.

>>> A IMPLEMENTAR — Responsável: Lucas (IHC/UX) com apoio do Backend (Júlio)

Rotas planejadas:
    GET   /notificacoes/            -> lista de notificações do usuário
    POST  /notificacoes/<id>/lida   -> marca notificação como lida
"""

from flask import Blueprint, render_template

notificacoes_bp = Blueprint("notificacoes", __name__)


@notificacoes_bp.route("/")
def listar():
    """STUB: lista de notificações. Implementar alertas (Lucas/Júlio)."""
    return render_template(
        "placeholder.html",
        modulo="Notificações",
        responsavel="Lucas (IHC/UX) + Júlio (Backend)",
    )
