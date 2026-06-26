"""
Camada de Repositórios (Data Access) - Mochila Cheia

Os repositórios traduzem entre as linhas do banco (SQLite) e a aplicação,
isolando o SQL em um único lugar. Esta é a fronteira entre a camada de
domínio/serviço e a camada de persistência.

- base_repository.py        -> padrão genérico (Rodrigo)
- estatisticas_repository.py -> exemplo concreto usado na home (Rodrigo)

A implementar pela equipe de Backend (Júlio):
- usuario_repository.py, item_repository.py, solicitacao_repository.py,
  mensagem_repository.py, notificacao_repository.py
"""

from src.web.repositories.base_repository import BaseRepository
from src.web.repositories.estatisticas_repository import EstatisticasRepository

__all__ = ["BaseRepository", "EstatisticasRepository"]
