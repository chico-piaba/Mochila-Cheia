"""
Módulo de Mensagens / Chat (Controller) - Mochila Cheia

Telas de comunicação (design do Figma): lista de conversas e tela de conversa.

>>> A LIGAR AO BACKEND — Responsável: Lucas (IHC/UX) + Júlio (Backend)
    Usar a classe Mensagem e a tabela MENSAGEM (contexto: uma solicitação).
"""

from flask import Blueprint, render_template

mensagens_bp = Blueprint("mensagens", __name__)


@mensagens_bp.route("/")
def conversas():
    """Lista de conversas (Figma). TODO: conversas do usuário logado."""
    return render_template("mensagens/conversas.html", nav_ativa="mensagens")


@mensagens_bp.route("/<int:id_solicitacao>")
def conversa(id_solicitacao):
    """Tela de chat (Figma). TODO: histórico + envio de mensagem."""
    return render_template("mensagens/conversa.html", id_solicitacao=id_solicitacao, nav_ativa="mensagens")
