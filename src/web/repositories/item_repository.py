"""
ItemRepository (Data Access) - Mochila Cheia

Persistência da entidade Item: publicação, listagem, detalhe e transições de
status (moderação e reserva). Reaproveita a classe de domínio Item para as
regras de negócio (status inicial, mapeamento de enums) e mantém o SQL isolado.

Responsável: Júlio (Backend e Análise de Fluxo)
"""

from typing import Optional

from src.web.repositories.base_repository import BaseRepository

# Mapeamento entre os rótulos do formulário (Figma) e os valores do enum/banco
ESTADO_FORM_PARA_BD = {
    "Novo": "novo",
    "Seminovo": "pouco_usado",
    "Usado": "usado",
    "Necessita Reparo": "necessita_reparo",
}

# Rótulos amigáveis para exibição nas telas de detalhe
ESTADO_BD_PARA_ROTULO = {
    "novo": "Novo",
    "pouco_usado": "Seminovo",
    "usado": "Usado",
    "necessita_reparo": "Necessita Reparo",
}


class ItemRepository(BaseRepository):
    """Operações de persistência para a tabela ITEM."""

    tabela = "ITEM"
    chave = "id_item"

    def buscar_detalhe(self, id_item: int) -> Optional[dict]:
        """
        Retorna um item com os dados do doador, categoria e ponto de coleta,
        já formatado para as telas de detalhe (chaves 'id', 'estado', etc.).
        """
        sql = """
            SELECT i.id_item, i.titulo, i.descricao, i.estado_conservacao,
                   i.status, i.localizacao, i.foto_url,
                   i.fk_id_doador AS doador_id,
                   c.nome AS categoria,
                   u.nome AS doador_nome,
                   p.nome AS ponto_coleta
            FROM ITEM i
            JOIN CATEGORIA c ON i.fk_id_categoria = c.id_categoria
            JOIN USUARIO u ON i.fk_id_doador = u.id_usuario
            LEFT JOIN PONTO_COLETA p ON i.fk_id_ponto_coleta = p.id_ponto
            WHERE i.id_item = ?
        """
        linha = self._conn().execute(sql, (id_item,)).fetchone()
        if linha is None:
            return None
        item = dict(linha)
        item["id"] = item["id_item"]
        item["estado"] = ESTADO_BD_PARA_ROTULO.get(
            item["estado_conservacao"], item["estado_conservacao"]
        )
        item["ponto_coleta"] = item["ponto_coleta"] or "A combinar no chat"
        return item

    def listar_por_doador(self, doador_id: int) -> list:
        """Itens publicados por um doador, do mais recente ao mais antigo."""
        sql = """
            SELECT i.id_item, i.titulo, i.status, i.estado_conservacao,
                   i.foto_url, c.nome AS categoria
            FROM ITEM i
            JOIN CATEGORIA c ON i.fk_id_categoria = c.id_categoria
            WHERE i.fk_id_doador = ?
            ORDER BY i.data_cadastro DESC
        """
        return self._conn().execute(sql, (doador_id,)).fetchall()

    def listar_pendentes(self) -> list:
        """Itens aguardando moderação, para a fila do moderador."""
        sql = """
            SELECT i.id_item, i.titulo, i.descricao, i.estado_conservacao,
                   i.foto_url, c.nome AS categoria, u.nome AS doador_nome
            FROM ITEM i
            JOIN CATEGORIA c ON i.fk_id_categoria = c.id_categoria
            JOIN USUARIO u ON i.fk_id_doador = u.id_usuario
            WHERE i.status = 'pendente_moderacao'
            ORDER BY i.data_cadastro ASC
        """
        return self._conn().execute(sql).fetchall()

    def criar(
        self,
        titulo: str,
        descricao: str,
        categoria_id: int,
        estado_conservacao: str,
        doador_id: int,
        localizacao: Optional[str] = None,
    ) -> int:
        """
        Publica um novo item. Nasce com status 'pendente_moderacao', acionando
        o fluxo de moderação antes de aparecer no catálogo.

        Returns:
            O id do item criado.
        """
        conn = self._conn()
        sql = """
            INSERT INTO ITEM
                (titulo, descricao, estado_conservacao, status,
                 localizacao, fk_id_doador, fk_id_categoria)
            VALUES (?, ?, ?, 'pendente_moderacao', ?, ?, ?)
        """
        cur = conn.execute(
            sql,
            (titulo.strip(), descricao.strip(), estado_conservacao,
             localizacao, doador_id, categoria_id),
        )
        conn.commit()
        return cur.lastrowid

    def aprovar(self, id_item: int, moderador_id: int) -> None:
        """Aprova um item: passa para 'disponivel' e registra o moderador."""
        conn = self._conn()
        conn.execute(
            """UPDATE ITEM
               SET status = 'disponivel',
                   fk_id_moderador = ?,
                   data_moderacao = CURRENT_TIMESTAMP
               WHERE id_item = ? AND status = 'pendente_moderacao'""",
            (moderador_id, id_item),
        )
        conn.commit()

    def recusar(self, id_item: int, moderador_id: int) -> None:
        """Recusa um item: passa para 'recusado' e registra o moderador."""
        conn = self._conn()
        conn.execute(
            """UPDATE ITEM
               SET status = 'recusado',
                   fk_id_moderador = ?,
                   data_moderacao = CURRENT_TIMESTAMP
               WHERE id_item = ? AND status = 'pendente_moderacao'""",
            (moderador_id, id_item),
        )
        conn.commit()

    def reservar(self, id_item: int) -> None:
        """Marca o item como 'reservado' (quando uma solicitação é criada)."""
        conn = self._conn()
        conn.execute(
            "UPDATE ITEM SET status = 'reservado' WHERE id_item = ? AND status = 'disponivel'",
            (id_item,),
        )
        conn.commit()
