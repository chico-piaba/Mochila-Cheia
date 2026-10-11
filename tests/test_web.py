"""
Testes da Aplicação Web - Mochila Cheia

Sobem a aplicação real (app factory) contra um banco SQLite temporário,
criado do zero a partir de schema.sql + seed.sql, e fazem requisições com o
test client do Flask. São estes testes que a esteira de CI roda antes de
deixar o Docker construir a imagem.

Execute com: pytest tests/test_web.py -v
"""

import pytest

from src.web import create_app
from src.web.database import init_db


@pytest.fixture
def app(tmp_path, monkeypatch):
    """Aplicação com banco isolado em pasta temporária (não toca no banco real)."""
    monkeypatch.setenv("MOCHILA_DB", str(tmp_path / "teste.db"))
    app = create_app("production")
    app.config.update(TESTING=True, DATABASE_PATH=str(tmp_path / "teste.db"))
    with app.app_context():
        init_db()
    return app


@pytest.fixture
def client(app):
    return app.test_client()


class TestApi:
    """Rotas JSON (equivalentes à /api/soma do roteiro)."""

    def test_saude_responde_ok(self, client):
        resposta = client.get("/api/saude")
        assert resposta.status_code == 200
        assert resposta.get_json() == {"status": "ok", "servico": "mochila-cheia"}

    def test_resumo_traz_todos_os_campos(self, client):
        dados = client.get("/api/resumo").get_json()
        assert set(dados) == {
            "total_doadores", "total_receptores", "itens_disponiveis",
            "itens_doados", "doacoes_concluidas", "pontos_ativos",
        }

    def test_resumo_le_o_seed(self, client):
        dados = client.get("/api/resumo").get_json()
        assert dados["itens_disponiveis"] > 0
        assert dados["pontos_ativos"] > 0


class TestPaginas:
    """As telas principais renderizam com o banco recém-criado."""

    @pytest.mark.parametrize("url", ["/", "/splash", "/itens/", "/pontos/", "/auth/login"])
    def test_pagina_publica_abre(self, client, url):
        assert client.get(url).status_code == 200

    def test_ponto_inexistente_da_404(self, client):
        assert client.get("/pontos/999999").status_code == 404
