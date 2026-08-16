"""
Módulo de Pontos de Coleta (Controller) - Mochila Cheia

Locais parceiros para entrega/retirada de itens. Liga as telas do Figma ao
PontoColetaRepository.

Responsável: Júlio (Backend)
"""

from flask import Blueprint, render_template, abort

from src.web.repositories import PontoColetaRepository

pontos_bp = Blueprint("pontos", __name__)


@pontos_bp.route("/")
def listar():
    """Lista os pontos de coleta ativos."""
    pontos = PontoColetaRepository().listar_ativos()
    return render_template("pontos/listar.html", pontos=pontos, nav_ativa="pontos")


@pontos_bp.route("/<int:id_ponto>")
def detalhe(id_ponto):
    """Detalhe de um ponto de coleta."""
    ponto = PontoColetaRepository().buscar_por_id(id_ponto)
    if ponto is None:
        abort(404)
    return render_template("pontos/detalhe.html", ponto=ponto, nav_ativa="pontos")
