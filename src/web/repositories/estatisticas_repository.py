"""
EstatisticasRepository - exemplo de repositório concreto - Mochila Cheia

Repositório de leitura usado pela página inicial (home). Serve como EXEMPLO do
padrão para os demais repositórios que a equipe de backend vai implementar:
herda de BaseRepository e expõe consultas específicas, reaproveitando as VIEWS
já definidas no Projeto Físico (schema.sql).

Responsável: Rodrigo (exemplo do padrão)
"""

from src.web.repositories.base_repository import BaseRepository


class EstatisticasRepository(BaseRepository):
    """Consultas agregadas para o painel inicial, baseadas nas views do schema."""

    def resumo(self) -> dict:
        """
        Retorna os números gerais do sistema (view vw_estatisticas).

        Devolve um dicionário pronto para o template, com zeros como padrão
        caso o banco ainda não tenha sido populado.
        """
        linha = self._conn().execute("SELECT * FROM vw_estatisticas").fetchone()
        return {
            "total_doadores": linha["total_doadores"] if linha else 0,
            "total_receptores": linha["total_receptores"] if linha else 0,
            "itens_disponiveis": linha["itens_disponiveis"] if linha else 0,
            "itens_doados": linha["itens_doados"] if linha else 0,
            "doacoes_concluidas": linha["doacoes_concluidas"] if linha else 0,
            "pontos_ativos": linha["pontos_ativos"] if linha else 0,
        }

    def itens_disponiveis(self, limite: int = 12) -> list:
        """Lista os itens disponíveis mais recentes (view vw_itens_disponiveis)."""
        sql = "SELECT * FROM vw_itens_disponiveis LIMIT ?"
        return self._conn().execute(sql, (limite,)).fetchall()
