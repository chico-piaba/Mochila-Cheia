"""
SolicitacaoRepository (Data Access) - Mochila Cheia

Persistência do fluxo de doação: criação de solicitações por receptores e
listagem das solicitações de um usuário. As transições de status (aceitar,
finalizar) seguem as regras da classe de domínio Solicitacao.

Responsável: Júlio (Backend e Análise de Fluxo)
"""

import sqlite3

from src.web.repositories.base_repository import BaseRepository

# Rótulos amigáveis dos status para exibição nas telas
STATUS_ROTULO = {
    "pendente": "Pendente",
    "aceita": "Aceita",
    "recusada": "Recusada",
    "cancelada": "Cancelada",
    "finalizada": "Finalizada",
    "expirada": "Expirada",
}


class SolicitacaoRepository(BaseRepository):
    """Operações de persistência para a tabela SOLICITACAO."""

    tabela = "SOLICITACAO"
    chave = "id_solicitacao"

    def ja_solicitou(self, item_id: int, receptor_id: int) -> bool:
        """Indica se o receptor já tem uma solicitação para este item."""
        sql = """SELECT 1 FROM SOLICITACAO
                 WHERE fk_id_item = ? AND fk_id_receptor = ?"""
        return self._conn().execute(sql, (item_id, receptor_id)).fetchone() is not None

    def criar(self, item_id: int, receptor_id: int) -> int:
        """
        Registra uma solicitação pendente de um receptor para um item.

        Returns:
            O id da solicitação criada.

        Raises:
            ValueError: se o receptor já houver solicitado o mesmo item
            (constraint UNIQUE item+receptor).
        """
        conn = self._conn()
        try:
            cur = conn.execute(
                """INSERT INTO SOLICITACAO (status, fk_id_item, fk_id_receptor)
                   VALUES ('pendente', ?, ?)""",
                (item_id, receptor_id),
            )
            conn.commit()
        except sqlite3.IntegrityError as exc:
            raise ValueError("Você já solicitou este item.") from exc
        return cur.lastrowid

    def listar_por_receptor(self, receptor_id: int) -> list:
        """Solicitações feitas por um receptor, com dados do item."""
        sql = """
            SELECT s.id_solicitacao, s.status, s.data_solicitacao,
                   i.id_item, i.titulo AS item_titulo, i.foto_url AS item_foto,
                   doador.nome AS doador_nome
            FROM SOLICITACAO s
            JOIN ITEM i ON s.fk_id_item = i.id_item
            JOIN USUARIO doador ON i.fk_id_doador = doador.id_usuario
            WHERE s.fk_id_receptor = ?
            ORDER BY s.data_solicitacao DESC
        """
        return self._conn().execute(sql, (receptor_id,)).fetchall()
