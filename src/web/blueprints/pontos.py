"""
Módulo de Pontos de Coleta (Controller) - Mochila Cheia

Telas dos locais parceiros (design do Figma): lista e detalhe do ponto.

>>> A LIGAR AO BACKEND — Responsável: Júlio (Backend)
    Usar a classe PontoDeColeta e a tabela PONTO_COLETA.
"""

from flask import Blueprint, render_template

pontos_bp = Blueprint("pontos", __name__)


@pontos_bp.route("/")
def listar():
    """Lista de pontos de coleta (Figma). TODO: pontos ativos reais."""
    return render_template("pontos/listar.html", nav_ativa="pontos")


@pontos_bp.route("/<int:id_ponto>")
def detalhe(id_ponto):
    """Detalhe do ponto de coleta (Figma). TODO: carregar ponto real."""
    return render_template("pontos/detalhe.html", id_ponto=id_ponto, nav_ativa="pontos")
