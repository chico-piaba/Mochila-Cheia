"""
Camada de Repositórios (Data Access) - Mochila Cheia

Os repositórios traduzem entre as linhas do banco (SQLite) e a aplicação,
isolando o SQL em um único lugar. Esta é a fronteira entre a camada de
domínio/serviço e a camada de persistência.

- base_repository.py         -> padrão genérico (Rodrigo)
- estatisticas_repository.py -> consultas da home (Rodrigo)
- usuario_repository.py      -> cadastro/login (Júlio)
- categoria_repository.py    -> categorias de materiais (Júlio)
- item_repository.py         -> publicação/edição/moderação de itens (Júlio)
- solicitacao_repository.py  -> fluxo de doação, lados receptor e doador (Júlio)
- mensagem_repository.py     -> chat interno (Lucas + Júlio)
- notificacao_repository.py  -> alertas do sistema (Lucas + Júlio)
- ponto_coleta_repository.py -> locais parceiros (Júlio)
"""

from src.web.repositories.base_repository import BaseRepository
from src.web.repositories.estatisticas_repository import EstatisticasRepository
from src.web.repositories.usuario_repository import UsuarioRepository
from src.web.repositories.categoria_repository import CategoriaRepository
from src.web.repositories.item_repository import ItemRepository
from src.web.repositories.solicitacao_repository import SolicitacaoRepository
from src.web.repositories.mensagem_repository import MensagemRepository
from src.web.repositories.notificacao_repository import NotificacaoRepository
from src.web.repositories.ponto_coleta_repository import PontoColetaRepository

__all__ = [
    "BaseRepository",
    "EstatisticasRepository",
    "UsuarioRepository",
    "CategoriaRepository",
    "ItemRepository",
    "SolicitacaoRepository",
    "MensagemRepository",
    "NotificacaoRepository",
    "PontoColetaRepository",
]
