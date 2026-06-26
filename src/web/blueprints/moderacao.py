"""
Módulo de Moderação (Controller) - Mochila Cheia

Telas do moderador (design do Figma): painel, fila de moderação e revisão de
um item.

>>> A LIGAR AO BACKEND — Responsável: Júlio (Backend e Análise de Fluxo)
    Usar Item.aprovar()/recusar(). Proteger as rotas para o perfil 'moderador'.
"""

from flask import Blueprint, render_template

moderacao_bp = Blueprint("moderacao", __name__)


@moderacao_bp.route("/")
def fila():
    """Fila de moderação (Figma). TODO Júlio: itens pendentes reais."""
    return render_template("moderacao/fila.html", nav_ativa="home")


@moderacao_bp.route("/painel")
def painel():
    """Painel do moderador (Figma). TODO Júlio: métricas reais."""
    return render_template("moderacao/painel.html", nav_ativa="home")


@moderacao_bp.route("/<int:id_item>/revisar")
def revisar(id_item):
    """Revisar item (Figma). TODO Júlio: aprovar/recusar no POST."""
    return render_template("moderacao/revisar.html", id_item=id_item, nav_ativa="home")
