"""
CategoriaRepository (Data Access) - Mochila Cheia

Consulta as categorias de materiais escolares. Usado principalmente para
traduzir o nome escolhido no formulário de publicação no id correspondente
da tabela CATEGORIA.

Responsável: Júlio (Backend e Análise de Fluxo)
"""

from src.web.repositories.base_repository import BaseRepository


class CategoriaRepository(BaseRepository):
    """Operações de leitura para a tabela CATEGORIA."""

    tabela = "CATEGORIA"
    chave = "id_categoria"

    def listar_ativas(self) -> list:
        """Categorias ativas, em ordem alfabética."""
        sql = "SELECT * FROM CATEGORIA WHERE ativa = 1 ORDER BY nome"
        return self._conn().execute(sql).fetchall()

    def id_por_nome(self, nome: str) -> int:
        """
        Resolve o id da categoria a partir do nome vindo do formulário.

        Tenta correspondência exata e, em seguida, aproximada (LIKE) — assim
        o valor "Escrita" do formulário casa com "Material de Escrita" do
        seed. Recai em 'Outros' quando nada corresponde.
        """
        conn = self._conn()
        linha = conn.execute(
            "SELECT id_categoria FROM CATEGORIA WHERE nome = ?", (nome,)
        ).fetchone()
        if linha is None:
            linha = conn.execute(
                "SELECT id_categoria FROM CATEGORIA WHERE nome LIKE ?", (f"%{nome}%",)
            ).fetchone()
        if linha is None:
            linha = conn.execute(
                "SELECT id_categoria FROM CATEGORIA WHERE nome = 'Outros'"
            ).fetchone()
        return linha["id_categoria"] if linha else 1
