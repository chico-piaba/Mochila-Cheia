"""
UsuarioRepository (Data Access) - Mochila Cheia

Persistência da entidade Usuario: cadastro, busca e autenticação. Todo o SQL
da tabela USUARIO fica isolado aqui (padrão Repository), mantendo os
controllers livres de acesso direto ao banco.

Responsável: Júlio (Backend e Análise de Fluxo)
"""

import sqlite3
from typing import Optional

from src.web.repositories.base_repository import BaseRepository
from src.web.seguranca import gerar_hash_senha, verificar_senha


class UsuarioRepository(BaseRepository):
    """Operações de persistência para a tabela USUARIO."""

    tabela = "USUARIO"
    chave = "id_usuario"

    def buscar_por_email(self, email: str):
        """Retorna o usuário com o e-mail informado, ou None."""
        sql = "SELECT * FROM USUARIO WHERE email = ?"
        return self._conn().execute(sql, (email.lower().strip(),)).fetchone()

    def email_existe(self, email: str) -> bool:
        """Indica se já há um cadastro com este e-mail."""
        return self.buscar_por_email(email) is not None

    def autenticar(self, email: str, senha: str):
        """
        Valida as credenciais e devolve a linha do usuário em caso de sucesso.

        Retorna None se o e-mail não existir, a senha não conferir ou a conta
        estiver inativa.
        """
        usuario = self.buscar_por_email(email)
        if usuario is None or not usuario["ativo"]:
            return None
        if not verificar_senha(senha, usuario["senha_hash"]):
            return None
        return usuario

    def criar(
        self,
        nome: str,
        email: str,
        senha: str,
        tipo_usuario: str,
        telefone: Optional[str] = None,
        endereco: Optional[str] = None,
    ) -> int:
        """
        Cadastra um novo usuário (senha guardada como hash bcrypt).

        Returns:
            O id do usuário criado.

        Raises:
            ValueError: se o e-mail já estiver cadastrado.
        """
        conn = self._conn()
        sql = """
            INSERT INTO USUARIO (nome, email, senha_hash, telefone, endereco, tipo_usuario)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        try:
            cur = conn.execute(
                sql,
                (
                    nome.strip(),
                    email.lower().strip(),
                    gerar_hash_senha(senha),
                    telefone,
                    endereco,
                    tipo_usuario,
                ),
            )
            conn.commit()
        except sqlite3.IntegrityError as exc:
            raise ValueError("Já existe uma conta com este e-mail.") from exc
        return cur.lastrowid
