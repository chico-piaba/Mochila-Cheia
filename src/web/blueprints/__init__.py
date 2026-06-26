"""
Camada de Controle (Controllers / Blueprints) - Mochila Cheia

Cada módulo do sistema é um Blueprint Flask independente. Essa
componentização permite que cada membro da equipe trabalhe no seu módulo sem
conflitar com os demais, e mantém as rotas organizadas por responsabilidade.

Mapa dos módulos e responsáveis:
    home          -> Rodrigo  (exemplo funcional do padrão completo)
    auth          -> Júlio    (cadastro/login/logout)
    itens         -> Júlio    (publicar/buscar/detalhar itens)
    solicitacoes  -> Júlio    (solicitar/aceitar/finalizar doação)
    moderacao     -> Júlio    (fila de moderação: aprovar/recusar)
    mensagens     -> Lucas    (chat entre doador e receptor)
    notificacoes  -> Lucas    (alertas do sistema)
"""

from src.web.blueprints.home import home_bp
from src.web.blueprints.auth import auth_bp
from src.web.blueprints.itens import itens_bp
from src.web.blueprints.solicitacoes import solicitacoes_bp
from src.web.blueprints.moderacao import moderacao_bp
from src.web.blueprints.mensagens import mensagens_bp
from src.web.blueprints.notificacoes import notificacoes_bp


def registrar_blueprints(app) -> None:
    """Registra todos os módulos da aplicação na instância Flask."""
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(itens_bp, url_prefix="/itens")
    app.register_blueprint(solicitacoes_bp, url_prefix="/solicitacoes")
    app.register_blueprint(moderacao_bp, url_prefix="/moderacao")
    app.register_blueprint(mensagens_bp, url_prefix="/mensagens")
    app.register_blueprint(notificacoes_bp, url_prefix="/notificacoes")
