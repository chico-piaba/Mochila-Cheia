"""
Módulo de Autenticação (Controller) - Mochila Cheia

Telas de cadastro, login, recuperação de senha e perfil (design do Figma).
As telas já existem; falta LIGAR ao backend.

>>> A LIGAR AO BACKEND — Responsável: Júlio (Backend e Análise de Fluxo)
    - login: validar credenciais com Usuario + abrir session["usuario_id"]
    - cadastro: criar Usuario (hash de senha já embutido) + UsuarioRepository
    - logout: session.clear()
"""

from flask import Blueprint, render_template, redirect, url_for, session

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login")
def login():
    """Tela de login (Figma). TODO Júlio: autenticar no POST."""
    return render_template("auth/login.html", sem_nav=True)


@auth_bp.route("/cadastro")
def cadastro():
    """Tela de cadastro (Figma). TODO Júlio: criar usuário no POST."""
    return render_template("auth/cadastro.html", sem_nav=True)


@auth_bp.route("/esqueci")
def esqueci_senha():
    """Tela de recuperação de senha (Figma). TODO Júlio: fluxo de reset."""
    return render_template("auth/esqueci_senha.html", sem_nav=True)


@auth_bp.route("/perfil")
def perfil():
    """Tela de perfil do usuário (Figma). TODO Júlio: dados do usuário logado."""
    return render_template("auth/perfil.html", nav_ativa="perfil")


@auth_bp.route("/logout")
def logout():
    """Encerra a sessão e volta para o login."""
    session.clear()
    return redirect(url_for("auth.login"))
