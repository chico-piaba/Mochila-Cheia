"""
Classe Mensagem - Mochila Cheia

Esta classe representa as mensagens trocadas entre usuários no sistema.
O chat permite que doadores e receptores combinem detalhes da entrega.

Princípios de POO aplicados:
- Encapsulamento: Atributos privados com acesso controlado via @property
- Composição: Mensagem contém referências a Usuario
- Abstração: Modelagem do sistema de comunicação
"""

from enum import Enum
from datetime import datetime
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .usuario import Usuario
    from .solicitacao import Solicitacao


class StatusMensagem(Enum):
    """Enumeração para os status de uma mensagem."""
    ENVIADA = "enviada"
    ENTREGUE = "entregue"
    LIDA = "lida"
    ERRO = "erro"


class Mensagem:
    """
    Classe que representa uma mensagem entre usuários.
    
    As mensagens permitem a comunicação entre doadores e receptores
    para combinar detalhes da entrega/retirada dos itens.
    
    Attributes:
        id_mensagem (int): Identificador único da mensagem
        remetente (Usuario): Usuário que enviou a mensagem
        destinatario (Usuario): Usuário que receberá a mensagem
        conteudo (str): Texto da mensagem
        data_envio (datetime): Data e hora do envio
        status (StatusMensagem): Status da mensagem
        solicitacao (Solicitacao): Solicitação relacionada (opcional)
    
    Example:
        >>> msg = Mensagem(
        ...     remetente=doador,
        ...     destinatario=receptor,
        ...     conteudo="Olá! Podemos combinar a entrega?",
        ...     solicitacao=solicitacao_atual
        ... )
        >>> msg.enviar()
    """
    
    # Contador estático para gerar IDs únicos
    _contador_id: int = 0
    
    def __init__(
        self,
        remetente: 'Usuario',
        destinatario: 'Usuario',
        conteudo: str,
        solicitacao: Optional['Solicitacao'] = None,
        id_mensagem: Optional[int] = None,
        status: StatusMensagem = StatusMensagem.ENVIADA,
        data_envio: Optional[datetime] = None
    ):
        """
        Inicializa uma nova mensagem.
        
        Args:
            remetente: Usuário que envia a mensagem
            destinatario: Usuário que recebe a mensagem
            conteudo: Texto da mensagem
            solicitacao: Solicitação relacionada (opcional)
            id_mensagem: ID opcional (gerado automaticamente)
            status: Status inicial da mensagem
            data_envio: Data/hora do envio (usa data atual se não fornecida)
        """
        # Gera ID automaticamente se não fornecido
        if id_mensagem is None:
            Mensagem._contador_id += 1
            self._id_mensagem = Mensagem._contador_id
        else:
            self._id_mensagem = id_mensagem
            if id_mensagem > Mensagem._contador_id:
                Mensagem._contador_id = id_mensagem
        
        # Atributos privados (encapsulamento)
        self._remetente = remetente  # Composição com Usuario
        self._destinatario = destinatario  # Composição com Usuario
        self._conteudo = conteudo
        self._solicitacao = solicitacao  # Composição com Solicitacao
        self._status = status
        self._data_envio = data_envio or datetime.now()
        self._data_leitura: Optional[datetime] = None
    
    # ==================== PROPRIEDADES (GETTERS) ====================
    
    @property
    def id_mensagem(self) -> int:
        """Retorna o ID único da mensagem."""
        return self._id_mensagem
    
    @property
    def remetente(self) -> 'Usuario':
        """Retorna o remetente da mensagem."""
        return self._remetente
    
    @property
    def destinatario(self) -> 'Usuario':
        """Retorna o destinatário da mensagem."""
        return self._destinatario
    
    @property
    def conteudo(self) -> str:
        """Retorna o conteúdo da mensagem."""
        return self._conteudo
    
    @property
    def solicitacao(self) -> Optional['Solicitacao']:
        """Retorna a solicitação relacionada."""
        return self._solicitacao
    
    @property
    def status(self) -> StatusMensagem:
        """Retorna o status da mensagem."""
        return self._status
    
    @property
    def data_envio(self) -> datetime:
        """Retorna a data de envio."""
        return self._data_envio
    
    @property
    def data_leitura(self) -> Optional[datetime]:
        """Retorna a data de leitura."""
        return self._data_leitura
    
    @property
    def foi_lida(self) -> bool:
        """Verifica se a mensagem foi lida."""
        return self._status == StatusMensagem.LIDA
    
    # ==================== MÉTODOS PÚBLICOS ====================
    
    def enviar(self) -> bool:
        """
        Envia a mensagem.
        
        Valida o conteúdo e registra o envio.
        
        Returns:
            True se a mensagem foi enviada, False caso contrário
        """
        # Validações
        if not self._conteudo or len(self._conteudo.strip()) == 0:
            print("❌ Mensagem não pode estar vazia.")
            self._status = StatusMensagem.ERRO
            return False
        
        if self._remetente.id_usuario == self._destinatario.id_usuario:
            print("❌ Não é possível enviar mensagem para si mesmo.")
            self._status = StatusMensagem.ERRO
            return False
        
        self._status = StatusMensagem.ENVIADA
        print(f"✉️ Mensagem enviada com sucesso!")
        print(f"   De: {self._remetente.nome}")
        print(f"   Para: {self._destinatario.nome}")
        
        return True
    
    def marcar_como_entregue(self) -> None:
        """Marca a mensagem como entregue ao destinatário."""
        if self._status == StatusMensagem.ENVIADA:
            self._status = StatusMensagem.ENTREGUE
    
    def marcar_como_lida(self) -> None:
        """Marca a mensagem como lida pelo destinatário."""
        if self._status in [StatusMensagem.ENVIADA, StatusMensagem.ENTREGUE]:
            self._status = StatusMensagem.LIDA
            self._data_leitura = datetime.now()
            print(f"✓✓ Mensagem #{self._id_mensagem} lida por {self._destinatario.nome}")
    
    def obter_preview(self, tamanho: int = 50) -> str:
        """
        Retorna uma prévia do conteúdo da mensagem.
        
        Args:
            tamanho: Número máximo de caracteres na prévia
            
        Returns:
            Prévia do conteúdo com reticências se truncado
        """
        if len(self._conteudo) <= tamanho:
            return self._conteudo
        return self._conteudo[:tamanho-3] + "..."
    
    def formatar_para_exibicao(self) -> str:
        """
        Formata a mensagem para exibição no chat.
        
        Returns:
            String formatada com informações da mensagem
        """
        data_formatada = self._data_envio.strftime("%d/%m/%Y %H:%M")
        status_icon = "✓✓" if self.foi_lida else "✓"
        
        return (
            f"[{data_formatada}] {self._remetente.nome}:\n"
            f"  {self._conteudo}\n"
            f"  {status_icon}"
        )
    
    def to_dict(self) -> dict:
        """
        Converte o objeto para dicionário.
        
        Returns:
            Dicionário com os dados da mensagem
        """
        return {
            "id_mensagem": self._id_mensagem,
            "remetente_id": self._remetente.id_usuario if self._remetente else None,
            "remetente_nome": self._remetente.nome if self._remetente else None,
            "destinatario_id": self._destinatario.id_usuario if self._destinatario else None,
            "destinatario_nome": self._destinatario.nome if self._destinatario else None,
            "conteudo": self._conteudo,
            "solicitacao_id": self._solicitacao.id_solicitacao if self._solicitacao else None,
            "status": self._status.value,
            "data_envio": self._data_envio.isoformat(),
            "data_leitura": self._data_leitura.isoformat() if self._data_leitura else None
        }
    
    def __str__(self) -> str:
        """Representação em string da mensagem."""
        preview = self.obter_preview(30)
        return f"Mensagem(#{self._id_mensagem}, '{preview}')"
    
    def __repr__(self) -> str:
        """Representação técnica do objeto."""
        return (
            f"Mensagem(id={self._id_mensagem}, "
            f"de='{self._remetente.nome}', "
            f"para='{self._destinatario.nome}', "
            f"status={self._status.value})"
        )


class Chat:
    """
    Classe auxiliar para gerenciar conversas entre usuários.
    
    Agrupa mensagens relacionadas a uma solicitação específica.
    """
    
    def __init__(self, solicitacao: 'Solicitacao'):
        """
        Inicializa um chat para uma solicitação.
        
        Args:
            solicitacao: Solicitação associada ao chat
        """
        self._solicitacao = solicitacao
        self._mensagens: list[Mensagem] = []
    
    @property
    def solicitacao(self) -> 'Solicitacao':
        """Retorna a solicitação associada."""
        return self._solicitacao
    
    @property
    def mensagens(self) -> list[Mensagem]:
        """Retorna todas as mensagens do chat."""
        return self._mensagens.copy()
    
    def adicionar_mensagem(self, mensagem: Mensagem) -> None:
        """Adiciona uma mensagem ao chat."""
        self._mensagens.append(mensagem)
    
    def obter_historico(self) -> list[str]:
        """
        Retorna o histórico formatado do chat.
        
        Returns:
            Lista de strings com as mensagens formatadas
        """
        return [msg.formatar_para_exibicao() for msg in self._mensagens]
    
    def exibir_conversa(self) -> None:
        """Exibe a conversa completa no console."""
        print(f"\n{'='*50}")
        print(f"Chat - Solicitação #{self._solicitacao.id_solicitacao}")
        print(f"Item: {self._solicitacao.item.titulo}")
        print(f"{'='*50}\n")
        
        if not self._mensagens:
            print("Nenhuma mensagem ainda.")
            return
        
        for msg in self._mensagens:
            print(msg.formatar_para_exibicao())
            print()
