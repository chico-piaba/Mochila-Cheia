"""
Módulo de Itens (Controller) - Mochila Cheia

Publicação, busca/listagem e detalhe dos materiais escolares. Usa a classe de
domínio src.models.Item (fluxo de status: pendente -> disponível -> reservado
-> doado) e o ItemRepository (a criar) para persistência.

>>> A IMPLEMENTAR — Responsável: Júlio (Backend e Análise de Fluxo)

Rotas planejadas:
    GET       /itens/            -> busca/listagem com filtros (categoria, local)
    GET       /itens/<id>        -> detalhe do item
    GET/POST  /itens/publicar    -> cadastro de novo item (doador)

Reaproveitar a view vw_itens_disponiveis (já existe no schema.sql) para a
listagem, seguindo o exemplo de EstatisticasRepository.
"""

from flask import Blueprint, render_template

itens_bp = Blueprint("itens", __name__)


@itens_bp.route("/")
def listar():
    """STUB: busca/listagem de itens. Implementar filtros (Júlio)."""
    return render_template(
        "placeholder.html",
        modulo="Itens — Busca e Listagem",
        responsavel="Júlio (Backend e Análise de Fluxo)",
    )


@itens_bp.route("/publicar")
def publicar():
    """STUB: publicação de item. Implementar cadastro (Júlio)."""
    return render_template(
        "placeholder.html",
        modulo="Itens — Publicar Item",
        responsavel="Júlio (Backend e Análise de Fluxo)",
    )
