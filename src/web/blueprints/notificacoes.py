"""
Módulo de Notificações (Controller) - Mochila Cheia

Tela de alertas do sistema (design do Figma).

>>> A LIGAR AO BACKEND — Responsável: Lucas (IHC/UX) + Júlio (Backend)
    Ler/escrever na tabela NOTIFICACAO (marcar como lida, etc.).
"""

from flask import Blueprint, render_template

notificacoes_bp = Blueprint("notificacoes", __name__)


@notificacoes_bp.route("/")
def listar():
    """Lista de notificações (Figma). TODO: notificações do usuário logado."""
    return render_template("notificacoes/listar.html", nav_ativa="home")
