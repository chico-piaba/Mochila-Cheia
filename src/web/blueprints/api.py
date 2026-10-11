"""
Módulo de API (Controller JSON) - Mochila Cheia

Rotas que devolvem JSON em vez de HTML. Existem para a esteira de CI/CD
(Integração de Sistemas, Estudo Guiado 01): são o equivalente, no Mochila
Cheia, da rota /api/soma do roteiro — pequenas, determinísticas e fáceis de
testar com o test client do Flask.

    /api/saude   -> o contêiner está de pé? (health check do Docker/deploy)
    /api/resumo  -> números gerais do sistema, lidos do banco

Responsável: Rodrigo (Arquitetura / DevOps)
"""

from flask import Blueprint, jsonify

from src.web.repositories import EstatisticasRepository

api_bp = Blueprint("api", __name__)


@api_bp.route("/saude")
def saude():
    """Health check: responde sem tocar no banco."""
    return jsonify(status="ok", servico="mochila-cheia")


@api_bp.route("/resumo")
def resumo():
    """Números gerais (doadores, receptores, itens, doações, pontos)."""
    return jsonify(EstatisticasRepository().resumo())
