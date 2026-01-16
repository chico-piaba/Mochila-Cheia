"""
Módulo de Modelos - Mochila Cheia

Este módulo contém as classes de domínio do sistema:
- Usuario: Representa doadores e receptores
- Item: Materiais escolares disponíveis para doação
- Solicitacao: Processo de pedido de doação
- PontoDeColeta: Locais parceiros para entrega/retirada
- Categoria: Classificação dos itens
- Mensagem: Comunicação entre usuários
"""

from .usuario import Usuario, TipoUsuario
from .categoria import Categoria
from .item import Item, EstadoConservacao, StatusItem
from .solicitacao import Solicitacao, StatusSolicitacao
from .ponto_coleta import PontoDeColeta
from .mensagem import Mensagem, StatusMensagem

__all__ = [
    'Usuario',
    'TipoUsuario',
    'Item',
    'EstadoConservacao',
    'StatusItem',
    'Solicitacao',
    'StatusSolicitacao',
    'PontoDeColeta',
    'Categoria',
    'Mensagem',
    'StatusMensagem'
]
