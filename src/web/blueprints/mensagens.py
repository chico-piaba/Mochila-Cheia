"""
Módulo de Mensagens / Chat (Controller) - Mochila Cheia

Comunicação entre doador e receptor no contexto de uma solicitação. Usa
src.models.Mensagem (status: enviada/entregue/lida) e a tabela MENSAGEM.

>>> A IMPLEMENTAR — Responsável: Lucas (IHC/UX) com apoio do Backend (Júlio)

Rotas planejadas:
    GET   /mensagens/                 -> lista de conversas do usuário
    GET   /mensagens/<id_solicitacao> -> histórico de uma conversa
    POST  /mensagens/<id_solicitacao> -> envia nova mensagem
"""

from flask import Blueprint, render_template

mensagens_bp = Blueprint("mensagens", __name__)


@mensagens_bp.route("/")
def conversas():
    """STUB: lista de conversas. Implementar chat (Lucas/Júlio)."""
    return render_template(
        "placeholder.html",
        modulo="Mensagens — Chat",
        responsavel="Lucas (IHC/UX) + Júlio (Backend)",
    )
