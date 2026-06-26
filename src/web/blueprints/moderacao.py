"""
Módulo de Moderação (Controller) - Mochila Cheia

Painel do moderador: fila de itens pendentes para aprovar ou recusar antes de
ficarem disponíveis. Usa os métodos aprovar()/recusar() de src.models.Item.

>>> A IMPLEMENTAR — Responsável: Júlio (Backend e Análise de Fluxo)

Rotas planejadas:
    GET   /moderacao/             -> fila de itens pendentes (apenas moderador)
    POST  /moderacao/<id>/aprovar -> aprova o item (fica disponível)
    POST  /moderacao/<id>/recusar -> recusa o item (com motivo)

Atenção: proteger as rotas para o perfil 'moderador' (verificar a sessão).
"""

from flask import Blueprint, render_template

moderacao_bp = Blueprint("moderacao", __name__)


@moderacao_bp.route("/")
def fila():
    """STUB: fila de moderação. Implementar aprovar/recusar (Júlio)."""
    return render_template(
        "placeholder.html",
        modulo="Moderação — Fila de Itens",
        responsavel="Júlio (Backend e Análise de Fluxo)",
    )
