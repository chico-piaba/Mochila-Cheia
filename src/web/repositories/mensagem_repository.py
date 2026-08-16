"""
MensagemRepository (Data Access) - Mochila Cheia

Chat interno entre doador e receptor. Cada conversa é ancorada a uma
solicitação (fk_id_solicitacao), conforme a modelagem do banco. Isola o SQL da
tabela MENSAGEM e monta as estruturas prontas para as telas de chat.

Responsável: Lucas (IHC/UX) + Júlio (Backend)
"""

from src.web.repositories.base_repository import BaseRepository


def _hora(valor):
    """Formata um timestamp (datetime ou texto) como HH:MM, de forma tolerante."""
    if valor is None:
        return ""
    try:
        return valor.strftime("%H:%M")
    except AttributeError:
        return str(valor)[11:16]


class MensagemRepository(BaseRepository):
    """Operações de persistência para a tabela MENSAGEM."""

    tabela = "MENSAGEM"
    chave = "id_mensagem"

    def contexto(self, id_solicitacao: int):
        """
        Dados da conversa (participantes, item e status da solicitação).
        Retorna dict ou None se a solicitação não existir.
        """
        sql = """
            SELECT s.id_solicitacao,
                   s.status AS status_solicitacao,
                   s.fk_id_receptor AS receptor_id,
                   receptor.nome AS receptor_nome,
                   i.fk_id_doador AS doador_id,
                   doador.nome AS doador_nome,
                   i.titulo AS item_titulo
            FROM SOLICITACAO s
            JOIN ITEM i ON s.fk_id_item = i.id_item
            JOIN USUARIO receptor ON s.fk_id_receptor = receptor.id_usuario
            JOIN USUARIO doador ON i.fk_id_doador = doador.id_usuario
            WHERE s.id_solicitacao = ?
        """
        linha = self._conn().execute(sql, (id_solicitacao,)).fetchone()
        return dict(linha) if linha else None

    def listar_conversas(self, usuario_id: int) -> list:
        """
        Conversas das quais o usuário participa (como doador ou receptor),
        com o outro participante, a última mensagem e o nº de não lidas.
        """
        sql = """
            SELECT s.id_solicitacao,
                   i.titulo AS item_titulo,
                   CASE WHEN s.fk_id_receptor = :uid THEN doador.nome
                        ELSE receptor.nome END AS outro_nome,
                   (SELECT conteudo FROM MENSAGEM m
                     WHERE m.fk_id_solicitacao = s.id_solicitacao
                     ORDER BY m.data_envio DESC LIMIT 1) AS ultima_mensagem,
                   (SELECT MAX(data_envio) FROM MENSAGEM m
                     WHERE m.fk_id_solicitacao = s.id_solicitacao) AS ultima_data,
                   (SELECT COUNT(*) FROM MENSAGEM m
                     WHERE m.fk_id_solicitacao = s.id_solicitacao
                       AND m.fk_id_destinatario = :uid
                       AND m.status != 'lida') AS nao_lidas
            FROM SOLICITACAO s
            JOIN ITEM i ON s.fk_id_item = i.id_item
            JOIN USUARIO receptor ON s.fk_id_receptor = receptor.id_usuario
            JOIN USUARIO doador ON i.fk_id_doador = doador.id_usuario
            WHERE (s.fk_id_receptor = :uid OR i.fk_id_doador = :uid)
              AND EXISTS (SELECT 1 FROM MENSAGEM m
                          WHERE m.fk_id_solicitacao = s.id_solicitacao)
            ORDER BY ultima_data DESC
        """
        linhas = self._conn().execute(sql, {"uid": usuario_id}).fetchall()
        conversas = []
        for linha in linhas:
            item = dict(linha)
            item["hora"] = _hora(item["ultima_data"])
            conversas.append(item)
        return conversas

    def listar_mensagens(self, id_solicitacao: int) -> list:
        """Mensagens da conversa, da mais antiga para a mais recente."""
        sql = """
            SELECT m.id_mensagem, m.conteudo, m.data_envio, m.status,
                   m.fk_id_remetente AS remetente_id,
                   u.nome AS remetente_nome
            FROM MENSAGEM m
            JOIN USUARIO u ON m.fk_id_remetente = u.id_usuario
            WHERE m.fk_id_solicitacao = ?
            ORDER BY m.data_envio ASC
        """
        linhas = self._conn().execute(sql, (id_solicitacao,)).fetchall()
        mensagens = []
        for linha in linhas:
            msg = dict(linha)
            msg["hora"] = _hora(msg["data_envio"])
            mensagens.append(msg)
        return mensagens

    def enviar(self, id_solicitacao, remetente_id, destinatario_id, conteudo) -> int:
        """Registra uma mensagem na conversa e devolve o id criado."""
        conn = self._conn()
        cur = conn.execute(
            """INSERT INTO MENSAGEM
                   (conteudo, status, fk_id_remetente, fk_id_destinatario, fk_id_solicitacao)
               VALUES (?, 'enviada', ?, ?, ?)""",
            (conteudo.strip(), remetente_id, destinatario_id, id_solicitacao),
        )
        conn.commit()
        return cur.lastrowid

    def marcar_lidas(self, id_solicitacao: int, usuario_id: int) -> None:
        """Marca como lidas as mensagens recebidas pelo usuário nesta conversa."""
        conn = self._conn()
        conn.execute(
            """UPDATE MENSAGEM SET status = 'lida', data_leitura = CURRENT_TIMESTAMP
               WHERE fk_id_solicitacao = ? AND fk_id_destinatario = ? AND status != 'lida'""",
            (id_solicitacao, usuario_id),
        )
        conn.commit()
