"""
Módulo de Autenticação (Controller) - Mochila Cheia

Cadastro, login, recuperação de senha e perfil. Liga as telas do Figma ao
backend: valida credenciais com o UsuarioRepository, aplica hash de senha
(bcrypt) e gerencia a sessão do usuário.

Responsável: Júlio (Backend e Análise de Fluxo)
"""

from flask import (
    Blueprint, render_template, redirect, url_for, session, request, flash
)

from src.web.repositories import UsuarioRepository
from src.web.sessao import usuario_logado, iniciar_sessao, login_obrigatorio

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """Autentica o usuário e abre a sessão."""
    if request.method == "POST":
        email = request.form.get("email", "")
        senha = request.form.get("senha", "")

        usuario = UsuarioRepository().autenticar(email, senha)
        if usuario is None:
            flash("E-mail ou senha incorretos.", "erro")
            return render_template("auth/login.html", sem_nav=True, email=email)

        iniciar_sessao(usuario)
        flash(f"Bem-vindo(a), {usuario['nome']}!", "sucesso")
        return redirect(url_for("home.index"))

    return render_template("auth/login.html", sem_nav=True)


@auth_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    """Cria uma nova conta e já inicia a sessão."""
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()
        senha = request.form.get("senha", "")
        tipo = request.form.get("tipo_usuario", "receptor")
        telefone = request.form.get("telefone") or None
        endereco = request.form.get("endereco") or None

        repo = UsuarioRepository()
        if not nome or not email or not senha:
            flash("Preencha nome, e-mail e senha.", "erro")
        elif repo.email_existe(email):
            flash("Já existe uma conta com este e-mail.", "erro")
        else:
            id_usuario = repo.criar(nome, email, senha, tipo, telefone, endereco)
            iniciar_sessao(repo.buscar_por_id(id_usuario))
            flash("Conta criada com sucesso!", "sucesso")
            return redirect(url_for("home.index"))

        return render_template("auth/cadastro.html", sem_nav=True, dados=request.form)

    return render_template("auth/cadastro.html", sem_nav=True)


@auth_bp.route("/esqueci")
def esqueci_senha():
    """Tela de recuperação de senha (fluxo de reset previsto para versão futura)."""
    return render_template("auth/esqueci_senha.html", sem_nav=True)


@auth_bp.route("/perfil")
@login_obrigatorio
def perfil():
    """Perfil do usuário logado."""
    dados = UsuarioRepository().buscar_por_id(usuario_logado()["id"])
    return render_template("auth/perfil.html", nav_ativa="perfil", usuario=dados)


@auth_bp.route("/logout")
def logout():
    """Encerra a sessão e volta para o login."""
    session.clear()
    flash("Sessão encerrada.", "sucesso")
    return redirect(url_for("auth.login"))
