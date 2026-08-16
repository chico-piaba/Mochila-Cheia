"""
NotificacaoRepository (Data Access) - Mochila Cheia

Alertas internos do sistema (solicitação recebida, solicitação aceita, item
aprovado, nova mensagem). Isola o SQL da tabela NOTIFICACAO e oferece a criação
de alertas usada pelos demais fluxos.

Responsável: Lucas (IHC/UX) + Júlio (Backend)
"""

from src.web.repositories.base_repository import BaseRepository


def _quando(valor):
    """Formata a data da notificação de forma tolerante (datetime ou texto)."""
    if valor is None:
        return ""
    try:
        return valor.strftime("%d/%m %H:%M")
    except AttributeError:
        return str(valor)[:16]


class NotificacaoRepository(BaseRepository):
    """Operações de persistência para a tabela NOTIFICACAO."""

    tabela = "NOTIFICACAO"
    chave = "id_notificacao"

    def listar(self, usuario_id: int) -> list:
        """Notificações do usuário, da mais recente para a mais antiga."""
        sql = """
            SELECT id_notificacao, titulo, mensagem, status, link_destino, data_criacao
            FROM NOTIFICACAO
            WHERE fk_id_usuario_destino = ?
            ORDER BY data_criacao DESC
        """
        linhas = self._conn().execute(sql, (usuario_id,)).fetchall()
        notifs = []
        for linha in linhas:
            n = dict(linha)
            n["quando"] = _quando(n["data_criacao"])
            n["nao_lida"] = n["status"] == "nao_lida"
            notifs.append(n)
        return notifs

    def contar_nao_lidas(self, usuario_id: int) -> int:
        """Quantidade de notificações não lidas (para o badge do sino)."""
        sql = """SELECT COUNT(*) AS total FROM NOTIFICACAO
                 WHERE fk_id_usuario_destino = ? AND status = 'nao_lida'"""
        return self._conn().execute(sql, (usuario_id,)).fetchone()["total"]

    def marcar_todas_lidas(self, usuario_id: int) -> None:
        """Marca todas as notificações do usuário como lidas."""
        conn = self._conn()
        conn.execute(
            """UPDATE NOTIFICACAO SET status = 'lida', data_leitura = CURRENT_TIMESTAMP
               WHERE fk_id_usuario_destino = ? AND status = 'nao_lida'""",
            (usuario_id,),
        )
        conn.commit()

    def criar(self, usuario_destino_id, titulo, mensagem,
              item_id=None, solicitacao_id=None, link_destino=None) -> int:
        """Cria um alerta para um usuário. Usado pelos fluxos de doação."""
        conn = self._conn()
        cur = conn.execute(
            """INSERT INTO NOTIFICACAO
                   (titulo, mensagem, status, link_destino,
                    fk_id_usuario_destino, fk_id_item, fk_id_solicitacao)
               VALUES (?, ?, 'nao_lida', ?, ?, ?, ?)""",
            (titulo, mensagem, link_destino, usuario_destino_id, item_id, solicitacao_id),
        )
        conn.commit()
        return cur.lastrowid
