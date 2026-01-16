"""
Classe Item - Mochila Cheia

Esta classe representa um material escolar disponível para doação.
Cada item possui informações sobre seu estado, categoria, fotos e status.

Princípios de POO aplicados:
- Encapsulamento: Atributos privados com acesso controlado
- Composição: Item contém referência ao Usuario (doador) e Categoria
- Abstração: Modelagem de materiais escolares do mundo real
"""

from enum import Enum
from datetime import datetime
from typing import Optional, List, TYPE_CHECKING

# Import condicional para evitar importação circular
if TYPE_CHECKING:
    from .usuario import Usuario
    from .categoria import Categoria


class EstadoConservacao(Enum):
    """Enumeração para os estados de conservação de um item."""
    NOVO = "novo"
    POUCO_USADO = "pouco_usado"
    USADO = "usado"
    NECESSITA_REPARO = "necessita_reparo"


class StatusItem(Enum):
    """Enumeração para os status de um item no sistema."""
    PENDENTE_MODERACAO = "pendente_moderacao"
    DISPONIVEL = "disponivel"
    RESERVADO = "reservado"
    DOADO = "doado"
    RECUSADO = "recusado"
    INATIVO = "inativo"


class Item:
    """
    Classe que representa um item disponível para doação.
    
    Um item é um material escolar que um doador cadastra no sistema
    para ser doado a um receptor que necessite.
    
    Attributes:
        id_item (int): Identificador único do item
        titulo (str): Nome/título do item
        descricao (str): Descrição detalhada do item
        categoria (Categoria): Categoria do item
        estado_conservacao (EstadoConservacao): Estado físico do item
        fotos (List[str]): Lista de URLs das fotos do item
        status (StatusItem): Status atual do item
        doador (Usuario): Usuário que cadastrou o item
        localizacao (str): Localização para retirada
        data_cadastro (datetime): Data de cadastro do item
    
    Example:
        >>> item = Item(
        ...     titulo="Mochila Azul",
        ...     descricao="Mochila escolar em ótimo estado",
        ...     categoria=cat_mochilas,
        ...     estado_conservacao=EstadoConservacao.POUCO_USADO,
        ...     doador=usuario_doador
        ... )
    """
    
    # Contador estático para gerar IDs únicos
    _contador_id: int = 0
    
    def __init__(
        self,
        titulo: str,
        descricao: str,
        categoria: 'Categoria',
        estado_conservacao: EstadoConservacao,
        doador: 'Usuario',
        id_item: Optional[int] = None,
        fotos: Optional[List[str]] = None,
        status: StatusItem = StatusItem.PENDENTE_MODERACAO,
        localizacao: Optional[str] = None,
        data_cadastro: Optional[datetime] = None
    ):
        """
        Inicializa um novo item para doação.
        
        Args:
            titulo: Nome/título do item
            descricao: Descrição detalhada
            categoria: Categoria do item
            estado_conservacao: Estado físico do item
            doador: Usuário que está doando
            id_item: ID opcional (gerado automaticamente se não fornecido)
            fotos: Lista de URLs das fotos
            status: Status inicial (padrão: PENDENTE_MODERACAO)
            localizacao: Local para retirada
            data_cadastro: Data de cadastro (usa data atual se não fornecida)
        """
        # Gera ID automaticamente se não fornecido
        if id_item is None:
            Item._contador_id += 1
            self._id_item = Item._contador_id
        else:
            self._id_item = id_item
            if id_item > Item._contador_id:
                Item._contador_id = id_item
        
        # Atributos privados (encapsulamento)
        self._titulo = titulo
        self._descricao = descricao
        self._categoria = categoria  # Composição com Categoria
        self._estado_conservacao = estado_conservacao
        self._doador = doador  # Composição com Usuario
        self._fotos = fotos or []
        self._status = status
        self._localizacao = localizacao or doador.endereco
        self._data_cadastro = data_cadastro or datetime.now()
        self._data_moderacao: Optional[datetime] = None
    
    # ==================== PROPRIEDADES (GETTERS) ====================
    
    @property
    def id_item(self) -> int:
        """Retorna o ID único do item."""
        return self._id_item
    
    @property
    def titulo(self) -> str:
        """Retorna o título do item."""
        return self._titulo
    
    @titulo.setter
    def titulo(self, valor: str) -> None:
        """Define o título do item com validação."""
        if not valor or len(valor.strip()) < 3:
            raise ValueError("Título deve ter pelo menos 3 caracteres")
        self._titulo = valor.strip()
    
    @property
    def descricao(self) -> str:
        """Retorna a descrição do item."""
        return self._descricao
    
    @descricao.setter
    def descricao(self, valor: str) -> None:
        """Define a descrição do item."""
        self._descricao = valor.strip() if valor else ""
    
    @property
    def categoria(self) -> 'Categoria':
        """Retorna a categoria do item."""
        return self._categoria
    
    @categoria.setter
    def categoria(self, valor: 'Categoria') -> None:
        """Define a categoria do item."""
        self._categoria = valor
    
    @property
    def estado_conservacao(self) -> EstadoConservacao:
        """Retorna o estado de conservação do item."""
        return self._estado_conservacao
    
    @property
    def doador(self) -> 'Usuario':
        """Retorna o doador do item."""
        return self._doador
    
    @property
    def fotos(self) -> List[str]:
        """Retorna a lista de fotos do item."""
        return self._fotos.copy()  # Retorna cópia para proteger a lista original
    
    @property
    def status(self) -> StatusItem:
        """Retorna o status atual do item."""
        return self._status
    
    @property
    def localizacao(self) -> Optional[str]:
        """Retorna a localização do item."""
        return self._localizacao
    
    @localizacao.setter
    def localizacao(self, valor: str) -> None:
        """Define a localização do item."""
        self._localizacao = valor
    
    @property
    def data_cadastro(self) -> datetime:
        """Retorna a data de cadastro do item."""
        return self._data_cadastro
    
    @property
    def data_moderacao(self) -> Optional[datetime]:
        """Retorna a data de moderação do item."""
        return self._data_moderacao
    
    # ==================== MÉTODOS PÚBLICOS ====================
    
    def cadastrar_item(self) -> dict:
        """
        Finaliza o cadastro do item.
        
        Em uma implementação real, este método persistiria
        os dados no banco de dados.
        
        Returns:
            Dicionário com os dados do item cadastrado
        """
        print(f"✅ Item '{self._titulo}' cadastrado com sucesso!")
        print(f"   Status: {self._status.value}")
        print(f"   Aguardando moderação...")
        return self.to_dict()
    
    def atualizar_status(self, novo_status: StatusItem) -> None:
        """
        Atualiza o status do item.
        
        Args:
            novo_status: Novo status a ser definido
        """
        status_anterior = self._status
        self._status = novo_status
        
        # Registra data de moderação quando aprovado ou recusado
        if novo_status in [StatusItem.DISPONIVEL, StatusItem.RECUSADO]:
            self._data_moderacao = datetime.now()
        
        print(f"📝 Status do item '{self._titulo}' alterado:")
        print(f"   {status_anterior.value} → {novo_status.value}")
    
    def aprovar(self) -> None:
        """Aprova o item, tornando-o disponível para doação."""
        if self._status != StatusItem.PENDENTE_MODERACAO:
            print(f"⚠️ Item não está pendente de moderação.")
            return
        self.atualizar_status(StatusItem.DISPONIVEL)
        print(f"✅ Item '{self._titulo}' aprovado e disponível para doação!")
    
    def recusar(self, motivo: str = "") -> None:
        """
        Recusa o item na moderação.
        
        Args:
            motivo: Motivo da recusa
        """
        if self._status != StatusItem.PENDENTE_MODERACAO:
            print(f"⚠️ Item não está pendente de moderação.")
            return
        self.atualizar_status(StatusItem.RECUSADO)
        print(f"❌ Item '{self._titulo}' recusado.")
        if motivo:
            print(f"   Motivo: {motivo}")
    
    def reservar(self) -> bool:
        """
        Reserva o item para um receptor.
        
        Returns:
            True se o item foi reservado, False caso contrário
        """
        if self._status != StatusItem.DISPONIVEL:
            print(f"⚠️ Item '{self._titulo}' não está disponível para reserva.")
            return False
        self.atualizar_status(StatusItem.RESERVADO)
        print(f"🔒 Item '{self._titulo}' reservado!")
        return True
    
    def liberar_reserva(self) -> None:
        """Libera a reserva do item, tornando-o disponível novamente."""
        if self._status == StatusItem.RESERVADO:
            self.atualizar_status(StatusItem.DISPONIVEL)
            print(f"🔓 Reserva do item '{self._titulo}' liberada.")
    
    def finalizar_doacao(self) -> None:
        """Marca o item como doado (processo concluído)."""
        if self._status == StatusItem.RESERVADO:
            self.atualizar_status(StatusItem.DOADO)
            print(f"🎉 Doação do item '{self._titulo}' finalizada com sucesso!")
    
    def adicionar_foto(self, foto_url: str) -> None:
        """
        Adiciona uma foto ao item.
        
        Args:
            foto_url: URL da foto a ser adicionada
        """
        if foto_url and foto_url not in self._fotos:
            self._fotos.append(foto_url)
            print(f"📷 Foto adicionada ao item '{self._titulo}'.")
    
    def remover_foto(self, foto_url: str) -> bool:
        """
        Remove uma foto do item.
        
        Args:
            foto_url: URL da foto a ser removida
            
        Returns:
            True se a foto foi removida, False caso contrário
        """
        if foto_url in self._fotos:
            self._fotos.remove(foto_url)
            print(f"🗑️ Foto removida do item '{self._titulo}'.")
            return True
        return False
    
    def esta_disponivel(self) -> bool:
        """
        Verifica se o item está disponível para solicitação.
        
        Returns:
            True se o item está disponível, False caso contrário
        """
        return self._status == StatusItem.DISPONIVEL
    
    def to_dict(self) -> dict:
        """
        Converte o objeto para dicionário.
        
        Returns:
            Dicionário com os dados do item
        """
        return {
            "id_item": self._id_item,
            "titulo": self._titulo,
            "descricao": self._descricao,
            "categoria": self._categoria.to_dict() if self._categoria else None,
            "estado_conservacao": self._estado_conservacao.value,
            "status": self._status.value,
            "fotos": self._fotos,
            "localizacao": self._localizacao,
            "doador_id": self._doador.id_usuario if self._doador else None,
            "doador_nome": self._doador.nome if self._doador else None,
            "data_cadastro": self._data_cadastro.isoformat(),
            "data_moderacao": self._data_moderacao.isoformat() if self._data_moderacao else None
        }
    
    def __str__(self) -> str:
        """Representação em string do item."""
        return f"Item({self._id_item}, '{self._titulo}', {self._status.value})"
    
    def __repr__(self) -> str:
        """Representação técnica do objeto."""
        return (
            f"Item(id={self._id_item}, titulo='{self._titulo}', "
            f"categoria='{self._categoria.nome}', status={self._status.value})"
        )
