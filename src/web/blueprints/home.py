"""
Módulo Home (Controller) - Mochila Cheia

Página inicial do MVP. Serve como EXEMPLO COMPLETO do fluxo de uma requisição
atravessando todas as camadas da arquitetura:

    Navegador  ->  rota Flask (controller)  ->  Repository  ->  SQLite  ->  template (view)

A equipe pode usar este módulo como referência ao implementar os demais.

Responsável: Rodrigo (Gestão, Comunicação e Arquitetura)
"""

from flask import Blueprint, render_template

from src.web.repositories import EstatisticasRepository

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def index():
    """
    Painel inicial: mostra os números do sistema e os itens disponíveis.

    Demonstra a separação de responsabilidades — o controller apenas
    coordena: pede os dados ao repositório e entrega ao template.
    """
    repo = EstatisticasRepository()
    resumo = repo.resumo()
    itens = repo.itens_disponiveis(limite=12)
    return render_template("index.html", resumo=resumo, itens=itens)
