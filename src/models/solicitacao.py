"""
Classe Solicitacao - Mochila Cheia

Esta classe representa o processo de solicitação de um item por um receptor.
Gerencia o fluxo completo desde o pedido até a finalização da doação.

Princípios de POO aplicados:
- Encapsulamento: Atributos privados com acesso controlado
- Agregação: Solicitacao contém referências a Item e Usuario
- Abstração: Modelagem do processo de doação
"""

from enum import Enum
from datetime import datetime
from typing import Optional, TYPE_CHECKING

# Import condicional para evitar importação circular
if TYPE_CHECKING:
    from .usuario import Usuario
    from .item import Item


class StatusSolicitacao(Enum):
    """Enumeração para os status de uma solicitação."""
    PENDENTE = "pendente"
    ACEITA = "aceita"
    RECUSADA = "recusada"
    CANCELADA = "cancelada"
    FINALIZADA = "finalizada"
    EXPIRADA = "expirada"


class Solicitacao:
    """
    Classe que representa uma solicitação de doação.
    
    Uma solicitação é criada quando um receptor demonstra interesse
    em receber um item. O doador pode então aceitar ou recusar.
    
    Attributes:
        id_solicitacao (int): Identificador único da solicitação
        item (Item): Item sendo solicitado
        solicitante (Usuario): Usuário que está pedindo o item (receptor)
        doador (Usuario): Usuário que possui o item (doador)
        status (StatusSolicitacao): Status atual da solicitação
        data_solicitacao (datetime): Data em que a solicitação foi criada
        ordem_fila (int): Posição na fila de espera do item
    
    Example:
        >>> solicitacao = Solicitacao(
        ...     item=item_mochila,
        ...     solicitante=usuario_receptor,
        ...     doador=usuario_doador
        ... )
        >>> solicitacao.criar()
    """
    
    # Contador estático para gerar IDs únicos
    _contador_id: int = 0
    
    def __init__(
        self,
        item: 'Item',
        solicitante: 'Usuario',
        doador: 'Usuario',
        id_solicitacao: Optional[int] = None,
        status: StatusSolicitacao = StatusSolicitacao.PENDENTE,
        data_solicitacao: Optional[datetime] = None,
        ordem_fila: int = 1
    ):
        """
        Inicializa uma nova solicitação.
        
        Args:
            item: Item sendo solicitado
            solicitante: Usuário que está pedindo (receptor)
            doador: Usuário que possui o item (doador)
            id_solicitacao: ID opcional (gerado automaticamente)
            status: Status inicial (padrão: PENDENTE)
            data_solicitacao: Data da solicitação (usa data atual se não fornecida)
            ordem_fila: Posição na fila de espera
        """
        # Gera ID automaticamente se não fornecido
        if id_solicitacao is None:
            Solicitacao._contador_id += 1
            self._id_solicitacao = Solicitacao._contador_id
        else:
            self._id_solicitacao = id_solicitacao
            if id_solicitacao > Solicitacao._contador_id:
                Solicitacao._contador_id = id_solicitacao
        
        # Atributos privados (encapsulamento)
        self._item = item  # Agregação com Item
        self._solicitante = solicitante  # Agregação com Usuario
        self._doador = doador  # Agregação com Usuario
        self._status = status
        self._data_solicitacao = data_solicitacao or datetime.now()
        self._ordem_fila = ordem_fila
        self._data_resposta: Optional[datetime] = None
        self._data_finalizacao: Optional[datetime] = None
        self._observacoes: str = ""
    
    # ==================== PROPRIEDADES (GETTERS) ====================
    
    @property
    def id_solicitacao(self) -> int:
        """Retorna o ID único da solicitação."""
        return self._id_solicitacao
    
    @property
    def item(self) -> 'Item':
        """Retorna o item solicitado."""
        return self._item
    
    @property
    def solicitante(self) -> 'Usuario':
        """Retorna o solicitante (receptor)."""
        return self._solicitante
    
    @property
    def doador(self) -> 'Usuario':
        """Retorna o doador."""
        return self._doador
    
    @property
    def status(self) -> StatusSolicitacao:
        """Retorna o status atual da solicitação."""
        return self._status
    
    @property
    def data_solicitacao(self) -> datetime:
        """Retorna a data da solicitação."""
        return self._data_solicitacao
    
    @property
    def data_resposta(self) -> Optional[datetime]:
        """Retorna a data da resposta do doador."""
        return self._data_resposta
    
    @property
    def data_finalizacao(self) -> Optional[datetime]:
        """Retorna a data de finalização da doação."""
        return self._data_finalizacao
    
    @property
    def ordem_fila(self) -> int:
        """Retorna a posição na fila de espera."""
        return self._ordem_fila
    
    @property
    def observacoes(self) -> str:
        """Retorna as observações da solicitação."""
        return self._observacoes
    
    @observacoes.setter
    def observacoes(self, valor: str) -> None:
        """Define as observações da solicitação."""
        self._observacoes = valor
    
    # ==================== MÉTODOS PÚBLICOS ====================
    
    def criar(self) -> dict:
        """
        Cria/registra a solicitação no sistema.
        
        Verifica se o item está disponível antes de criar a solicitação.
        
        Returns:
            Dicionário com os dados da solicitação criada
        """
        # Verifica se o item está disponível
        if not self._item.esta_disponivel():
            print(f"❌ Item '{self._item.titulo}' não está disponível para solicitação.")
            return {}
        
        # Verifica se solicitante não é o próprio doador
        if self._solicitante.id_usuario == self._doador.id_usuario:
            print(f"❌ Você não pode solicitar seu próprio item.")
            return {}
        
        print(f"✅ Solicitação #{self._id_solicitacao} criada com sucesso!")
        print(f"   Item: {self._item.titulo}")
        print(f"   Solicitante: {self._solicitante.nome}")
        print(f"   Doador: {self._doador.nome}")
        print(f"   Status: {self._status.value}")
        
        return self.to_dict()
    
    def aceitar(self) -> bool:
        """
        Doador aceita a solicitação.
        
        Ao aceitar, o item é reservado para o solicitante.
        
        Returns:
            True se a solicitação foi aceita, False caso contrário
        """
        if self._status != StatusSolicitacao.PENDENTE:
            print(f"⚠️ Solicitação não está pendente (status: {self._status.value}).")
            return False
        
        # Reserva o item
        if not self._item.reservar():
            print(f"❌ Não foi possível reservar o item.")
            return False
        
        self._status = StatusSolicitacao.ACEITA
        self._data_resposta = datetime.now()
        
        print(f"✅ Solicitação #{self._id_solicitacao} ACEITA!")
        print(f"   {self._solicitante.nome} pode retirar '{self._item.titulo}'")
        
        return True
    
    def recusar(self, motivo: str = "") -> bool:
        """
        Doador recusa a solicitação.
        
        Args:
            motivo: Motivo opcional da recusa
            
        Returns:
            True se a solicitação foi recusada, False caso contrário
        """
        if self._status != StatusSolicitacao.PENDENTE:
            print(f"⚠️ Solicitação não está pendente (status: {self._status.value}).")
            return False
        
        self._status = StatusSolicitacao.RECUSADA
        self._data_resposta = datetime.now()
        if motivo:
            self._observacoes = f"Motivo da recusa: {motivo}"
        
        print(f"❌ Solicitação #{self._id_solicitacao} RECUSADA.")
        if motivo:
            print(f"   Motivo: {motivo}")
        
        return True
    
    def cancelar(self) -> bool:
        """
        Solicitante cancela a solicitação.
        
        Returns:
            True se a solicitação foi cancelada, False caso contrário
        """
        if self._status not in [StatusSolicitacao.PENDENTE, StatusSolicitacao.ACEITA]:
            print(f"⚠️ Solicitação não pode ser cancelada (status: {self._status.value}).")
            return False
        
        # Se já estava aceita, libera a reserva do item
        if self._status == StatusSolicitacao.ACEITA:
            self._item.liberar_reserva()
        
        self._status = StatusSolicitacao.CANCELADA
        
        print(f"🚫 Solicitação #{self._id_solicitacao} cancelada pelo solicitante.")
        
        return True
    
    def finalizar(self) -> bool:
        """
        Finaliza a solicitação após a entrega ser concluída.
        
        Marca tanto a solicitação quanto o item como finalizados/doados.
        
        Returns:
            True se a solicitação foi finalizada, False caso contrário
        """
        if self._status != StatusSolicitacao.ACEITA:
            print(f"⚠️ Solicitação deve estar aceita para ser finalizada.")
            return False
        
        # Finaliza a doação do item
        self._item.finalizar_doacao()
        
        self._status = StatusSolicitacao.FINALIZADA
        self._data_finalizacao = datetime.now()
        
        print(f"🎉 Solicitação #{self._id_solicitacao} FINALIZADA!")
        print(f"   '{self._item.titulo}' foi doado com sucesso!")
        print(f"   Doador: {self._doador.nome}")
        print(f"   Receptor: {self._solicitante.nome}")
        
        return True
    
    def esta_pendente(self) -> bool:
        """Verifica se a solicitação está pendente."""
        return self._status == StatusSolicitacao.PENDENTE
    
    def esta_aceita(self) -> bool:
        """Verifica se a solicitação foi aceita."""
        return self._status == StatusSolicitacao.ACEITA
    
    def esta_finalizada(self) -> bool:
        """Verifica se a solicitação foi finalizada."""
        return self._status == StatusSolicitacao.FINALIZADA
    
    def to_dict(self) -> dict:
        """
        Converte o objeto para dicionário.
        
        Returns:
            Dicionário com os dados da solicitação
        """
        return {
            "id_solicitacao": self._id_solicitacao,
            "item_id": self._item.id_item if self._item else None,
            "item_titulo": self._item.titulo if self._item else None,
            "solicitante_id": self._solicitante.id_usuario if self._solicitante else None,
            "solicitante_nome": self._solicitante.nome if self._solicitante else None,
            "doador_id": self._doador.id_usuario if self._doador else None,
            "doador_nome": self._doador.nome if self._doador else None,
            "status": self._status.value,
            "ordem_fila": self._ordem_fila,
            "data_solicitacao": self._data_solicitacao.isoformat(),
            "data_resposta": self._data_resposta.isoformat() if self._data_resposta else None,
            "data_finalizacao": self._data_finalizacao.isoformat() if self._data_finalizacao else None,
            "observacoes": self._observacoes
        }
    
    def __str__(self) -> str:
        """Representação em string da solicitação."""
        return f"Solicitacao(#{self._id_solicitacao}, {self._status.value})"
    
    def __repr__(self) -> str:
        """Representação técnica do objeto."""
        return (
            f"Solicitacao(id={self._id_solicitacao}, "
            f"item='{self._item.titulo}', "
            f"solicitante='{self._solicitante.nome}', "
            f"status={self._status.value})"
        )
