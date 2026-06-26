"""
Camada de Controle (Controllers / Blueprints) - Mochila Cheia

Cada módulo do sistema é um Blueprint Flask independente. Essa
componentização permite que cada membro da equipe trabalhe no seu módulo sem
conflitar com os demais, e mantém as rotas organizadas por responsabilidade.

Mapa dos módulos, telas (Figma) e responsáveis:
    home          -> Rodrigo  (index = busca com dados reais; doador; splash)
    auth          -> Júlio    (login, cadastro, esqueci senha, perfil, logout)
    itens         -> Júlio    (listar, meus, publicar, detalhe[doador], editar)
    solicitacoes  -> Júlio    (minhas, confirmar)
    moderacao     -> Júlio    (fila, painel, revisar)
    pontos        -> Júlio    (listar, detalhe)
    mensagens     -> Lucas    (conversas, conversa/chat)
    notificacoes  -> Lucas    (listar)

As telas (templates) vêm do protótipo de alta fidelidade (Figma/Stitch) e já
estão integradas. O que falta em cada módulo é ligar os formulários/ações ao
backend (ver TODOs em cada blueprint).
"""

from src.web.blueprints.home import home_bp
from src.web.blueprints.auth import auth_bp
from src.web.blueprints.itens import itens_bp
from src.web.blueprints.solicitacoes import solicitacoes_bp
from src.web.blueprints.moderacao import moderacao_bp
from src.web.blueprints.pontos import pontos_bp
from src.web.blueprints.mensagens import mensagens_bp
from src.web.blueprints.notificacoes import notificacoes_bp


def registrar_blueprints(app) -> None:
    """Registra todos os módulos da aplicação na instância Flask."""
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(itens_bp, url_prefix="/itens")
    app.register_blueprint(solicitacoes_bp, url_prefix="/solicitacoes")
    app.register_blueprint(moderacao_bp, url_prefix="/moderacao")
    app.register_blueprint(pontos_bp, url_prefix="/pontos")
    app.register_blueprint(mensagens_bp, url_prefix="/mensagens")
    app.register_blueprint(notificacoes_bp, url_prefix="/notificacoes")
