"""
Módulo de Autenticação (Controller) - Mochila Cheia

Cadastro, login e logout dos três perfis (doador, receptor, moderador).
Reaproveita a classe de domínio src.models.Usuario (hash de senha já embutido)
e a sessão do Flask para manter o usuário autenticado.

>>> A IMPLEMENTAR — Responsável: Júlio (Backend e Análise de Fluxo)

Rotas planejadas:
    GET/POST  /auth/cadastro   -> formulário de cadastro + criação do usuário
    GET/POST  /auth/login      -> autenticação e abertura de sessão
    GET       /auth/logout     -> encerra a sessão

Sugestão de fluxo (cadastro):
    1. Validar dados do formulário (request.form)
    2. usuario = Usuario(nome, email, senha, tipo_usuario)   # domínio
    3. UsuarioRepository().criar(usuario)                    # persistência
    4. session["usuario_id"] = ...; redirect para a home
"""

from flask import Blueprint, render_template

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login")
def login():
    """STUB: tela de login. Implementar autenticação (Júlio)."""
    return render_template(
        "placeholder.html",
        modulo="Autenticação — Login",
        responsavel="Júlio (Backend e Análise de Fluxo)",
    )


@auth_bp.route("/cadastro")
def cadastro():
    """STUB: tela de cadastro. Implementar criação de usuário (Júlio)."""
    return render_template(
        "placeholder.html",
        modulo="Autenticação — Cadastro",
        responsavel="Júlio (Backend e Análise de Fluxo)",
    )
