"""
Sessão e controle de acesso (infra) - Mochila Cheia

Helpers para identificar o usuário logado e proteger rotas que exigem
autenticação. A sessão guarda apenas o essencial (id, nome e tipo), evitando
expor dados sensíveis no cookie.
"""

from functools import wraps
from typing import Optional

from flask import session, redirect, url_for, flash


def usuario_logado() -> Optional[dict]:
    """Retorna os dados do usuário logado (ou None se não houver sessão)."""
    if "usuario_id" not in session:
        return None
    return {
        "id": session["usuario_id"],
        "nome": session.get("usuario_nome"),
        "tipo": session.get("usuario_tipo"),
    }


def iniciar_sessao(usuario) -> None:
    """Grava na sessão os dados do usuário autenticado (linha do banco)."""
    session["usuario_id"] = usuario["id_usuario"]
    session["usuario_nome"] = usuario["nome"]
    session["usuario_tipo"] = usuario["tipo_usuario"]


def login_obrigatorio(view):
    """Decorator que redireciona para o login quando não há sessão ativa."""

    @wraps(view)
    def wrapper(*args, **kwargs):
        if usuario_logado() is None:
            flash("Faça login para continuar.", "aviso")
            return redirect(url_for("auth.login"))
        return view(*args, **kwargs)

    return wrapper
