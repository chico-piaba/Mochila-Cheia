"""
Módulo de Solicitações (Controller) - Mochila Cheia

Fluxo de doação: o receptor solicita um item; o doador aceita/recusa; ao
concluir, a doação é finalizada. Usa src.models.Solicitacao, que coordena a
mudança de status do Item (reservar/finalizar).

>>> A IMPLEMENTAR — Responsável: Júlio (Backend e Análise de Fluxo)

Rotas planejadas:
    POST  /solicitacoes/criar/<id_item>   -> receptor solicita um item
    GET   /solicitacoes/minhas            -> solicitações do usuário logado
    POST  /solicitacoes/<id>/aceitar      -> doador aceita (reserva o item)
    POST  /solicitacoes/<id>/finalizar    -> conclui a doação
"""

from flask import Blueprint, render_template

solicitacoes_bp = Blueprint("solicitacoes", __name__)


@solicitacoes_bp.route("/minhas")
def minhas():
    """STUB: solicitações do usuário. Implementar fluxo (Júlio)."""
    return render_template(
        "placeholder.html",
        modulo="Solicitações",
        responsavel="Júlio (Backend e Análise de Fluxo)",
    )
