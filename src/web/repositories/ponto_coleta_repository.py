"""
PontoColetaRepository (Data Access) - Mochila Cheia

Locais parceiros para entrega/retirada de itens. Isola o SQL da tabela
PONTO_COLETA.

Responsável: Júlio (Backend)
"""

from typing import Optional

from src.web.repositories.base_repository import BaseRepository


class PontoColetaRepository(BaseRepository):
    """Operações de leitura para a tabela PONTO_COLETA."""

    tabela = "PONTO_COLETA"
    chave = "id_ponto"

    def listar_ativos(self) -> list:
        """Pontos de coleta ativos, em ordem alfabética."""
        sql = "SELECT * FROM PONTO_COLETA WHERE ativo = 1 ORDER BY nome"
        return self._conn().execute(sql).fetchall()

    def buscar_por_id(self, id_ponto: int) -> Optional[dict]:
        """Retorna um ponto de coleta pelo id, ou None."""
        linha = super().buscar_por_id(id_ponto)
        return dict(linha) if linha else None
