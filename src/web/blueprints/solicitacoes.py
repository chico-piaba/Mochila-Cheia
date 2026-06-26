"""
Módulo de Solicitações (Controller) - Mochila Cheia

Telas do fluxo de doação (design do Figma): minhas solicitações e confirmação
de solicitação de um item.

>>> A LIGAR AO BACKEND — Responsável: Júlio (Backend e Análise de Fluxo)
    Usar a classe Solicitacao (aceitar/finalizar coordenam o status do Item).
"""

from flask import Blueprint, render_template

solicitacoes_bp = Blueprint("solicitacoes", __name__)


@solicitacoes_bp.route("/minhas")
def minhas():
    """Minhas solicitações (Figma). TODO Júlio: solicitações do usuário logado."""
    return render_template("solicitacoes/minhas.html", nav_ativa="solicitacoes")


@solicitacoes_bp.route("/confirmar")
def confirmar():
    """Confirmação de solicitação (Figma). TODO Júlio: criar Solicitacao no POST."""
    return render_template("solicitacoes/confirmar.html", nav_ativa="solicitacoes")
