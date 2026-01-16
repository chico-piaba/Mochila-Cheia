"""
Classe PontoDeColeta - Mochila Cheia

Esta classe representa um local parceiro onde doadores podem deixar itens
e receptores podem retirá-los. São estabelecimentos que colaboram com
a plataforma (escolas, igrejas, comércios locais, etc.).

Princípios de POO aplicados:
- Encapsulamento: Atributos privados com acesso controlado via @property
- Abstração: Modelagem de locais físicos de coleta/entrega
"""

from datetime import datetime
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .item import Item
    from .usuario import Usuario


class PontoDeColeta:
    """
    Classe que representa um ponto de coleta parceiro.
    
    Pontos de coleta são locais onde os itens podem ser deixados pelos
    doadores e retirados pelos receptores, facilitando a logística
    sem expor endereços residenciais.
    
    Attributes:
        id_ponto (int): Identificador único do ponto
        nome (str): Nome do estabelecimento
        endereco_completo (str): Endereço completo do local
        horario_funcionamento (str): Horários de funcionamento
        responsavel (str): Nome do responsável pelo local
    
    Example:
        >>> ponto = PontoDeColeta(
        ...     nome="Escola Municipal Centro",
        ...     endereco_completo="Rua Principal, 100 - Centro",
        ...     horario_funcionamento="Seg-Sex: 8h às 17h",
        ...     responsavel="Diretora Maria"
        ... )
    """
    
    # Contador estático para gerar IDs únicos
    _contador_id: int = 0
    
    def __init__(
        self,
        nome: str,
        endereco_completo: str,
        horario_funcionamento: str,
        responsavel: str,
        id_ponto: Optional[int] = None,
        telefone: Optional[str] = None,
        email: Optional[str] = None
    ):
        """
        Inicializa um novo ponto de coleta.
        
        Args:
            nome: Nome do estabelecimento parceiro
            endereco_completo: Endereço completo com rua, número, bairro
            horario_funcionamento: Horários de funcionamento
            responsavel: Nome do responsável pelo local
            id_ponto: ID opcional (gerado automaticamente se não fornecido)
            telefone: Telefone para contato
            email: E-mail para contato
        """
        # Gera ID automaticamente se não fornecido
        if id_ponto is None:
            PontoDeColeta._contador_id += 1
            self._id_ponto = PontoDeColeta._contador_id
        else:
            self._id_ponto = id_ponto
            if id_ponto > PontoDeColeta._contador_id:
                PontoDeColeta._contador_id = id_ponto
        
        # Atributos privados (encapsulamento)
        self._nome = nome
        self._endereco_completo = endereco_completo
        self._horario_funcionamento = horario_funcionamento
        self._responsavel = responsavel
        self._telefone = telefone
        self._email = email
        self._ativo = True
        self._data_cadastro = datetime.now()
        
        # Lista de itens atualmente no ponto (para controle)
        self._itens_disponiveis: List['Item'] = []
    
    # ==================== PROPRIEDADES (GETTERS/SETTERS) ====================
    
    @property
    def id_ponto(self) -> int:
        """Retorna o ID único do ponto de coleta."""
        return self._id_ponto
    
    @property
    def nome(self) -> str:
        """Retorna o nome do ponto de coleta."""
        return self._nome
    
    @nome.setter
    def nome(self, valor: str) -> None:
        """Define o nome do ponto de coleta."""
        if not valor or len(valor.strip()) < 3:
            raise ValueError("Nome deve ter pelo menos 3 caracteres")
        self._nome = valor.strip()
    
    @property
    def endereco_completo(self) -> str:
        """Retorna o endereço completo."""
        return self._endereco_completo
    
    @endereco_completo.setter
    def endereco_completo(self, valor: str) -> None:
        """Define o endereço completo."""
        self._endereco_completo = valor.strip() if valor else ""
    
    @property
    def horario_funcionamento(self) -> str:
        """Retorna o horário de funcionamento."""
        return self._horario_funcionamento
    
    @horario_funcionamento.setter
    def horario_funcionamento(self, valor: str) -> None:
        """Define o horário de funcionamento."""
        self._horario_funcionamento = valor
    
    @property
    def responsavel(self) -> str:
        """Retorna o nome do responsável."""
        return self._responsavel
    
    @responsavel.setter
    def responsavel(self, valor: str) -> None:
        """Define o responsável pelo ponto."""
        self._responsavel = valor
    
    @property
    def telefone(self) -> Optional[str]:
        """Retorna o telefone de contato."""
        return self._telefone
    
    @telefone.setter
    def telefone(self, valor: Optional[str]) -> None:
        """Define o telefone de contato."""
        self._telefone = valor
    
    @property
    def email(self) -> Optional[str]:
        """Retorna o e-mail de contato."""
        return self._email
    
    @property
    def ativo(self) -> bool:
        """Retorna se o ponto está ativo."""
        return self._ativo
    
    @property
    def data_cadastro(self) -> datetime:
        """Retorna a data de cadastro."""
        return self._data_cadastro
    
    @property
    def itens_disponiveis(self) -> List['Item']:
        """Retorna a lista de itens disponíveis no ponto."""
        return self._itens_disponiveis.copy()
    
    @property
    def quantidade_itens(self) -> int:
        """Retorna a quantidade de itens no ponto."""
        return len(self._itens_disponiveis)
    
    # ==================== MÉTODOS PÚBLICOS ====================
    
    def cadastrar_ponto(self) -> dict:
        """
        Finaliza o cadastro do ponto de coleta.
        
        Returns:
            Dicionário com os dados do ponto cadastrado
        """
        print(f"✅ Ponto de Coleta '{self._nome}' cadastrado com sucesso!")
        print(f"   Endereço: {self._endereco_completo}")
        print(f"   Horário: {self._horario_funcionamento}")
        print(f"   Responsável: {self._responsavel}")
        return self.to_dict()
    
    def receber_item(self, item: 'Item') -> bool:
        """
        Registra o recebimento de um item no ponto de coleta.
        
        Args:
            item: Item a ser recebido
            
        Returns:
            True se o item foi recebido, False caso contrário
        """
        if item in self._itens_disponiveis:
            print(f"⚠️ Item '{item.titulo}' já está registrado neste ponto.")
            return False
        
        self._itens_disponiveis.append(item)
        print(f"📦 Item '{item.titulo}' recebido no ponto '{self._nome}'.")
        return True
    
    def entregar_item(self, item: 'Item', solicitante: 'Usuario') -> bool:
        """
        Registra a entrega/retirada de um item do ponto de coleta.
        
        Args:
            item: Item a ser entregue
            solicitante: Usuário que está retirando
            
        Returns:
            True se o item foi entregue, False caso contrário
        """
        if item not in self._itens_disponiveis:
            print(f"⚠️ Item '{item.titulo}' não está disponível neste ponto.")
            return False
        
        self._itens_disponiveis.remove(item)
        print(f"🎁 Item '{item.titulo}' entregue para {solicitante.nome}.")
        print(f"   Local: {self._nome}")
        return True
    
    def listar_itens(self) -> List[dict]:
        """
        Lista todos os itens disponíveis no ponto.
        
        Returns:
            Lista de dicionários com informações dos itens
        """
        if not self._itens_disponiveis:
            print(f"📭 Nenhum item disponível no ponto '{self._nome}'.")
            return []
        
        print(f"📋 Itens disponíveis em '{self._nome}':")
        itens_info = []
        for i, item in enumerate(self._itens_disponiveis, 1):
            print(f"   {i}. {item.titulo}")
            itens_info.append(item.to_dict())
        return itens_info
    
    def desativar(self) -> None:
        """Desativa o ponto de coleta."""
        self._ativo = False
        print(f"⚠️ Ponto de Coleta '{self._nome}' desativado.")
    
    def ativar(self) -> None:
        """Reativa o ponto de coleta."""
        self._ativo = True
        print(f"✅ Ponto de Coleta '{self._nome}' ativado.")
    
    def atualizar_informacoes(
        self,
        nome: Optional[str] = None,
        endereco: Optional[str] = None,
        horario: Optional[str] = None,
        responsavel: Optional[str] = None
    ) -> None:
        """
        Atualiza as informações do ponto de coleta.
        
        Args:
            nome: Novo nome (opcional)
            endereco: Novo endereço (opcional)
            horario: Novo horário (opcional)
            responsavel: Novo responsável (opcional)
        """
        if nome:
            self.nome = nome
        if endereco:
            self.endereco_completo = endereco
        if horario:
            self.horario_funcionamento = horario
        if responsavel:
            self.responsavel = responsavel
        
        print(f"✅ Informações do ponto '{self._nome}' atualizadas.")
    
    def to_dict(self) -> dict:
        """
        Converte o objeto para dicionário.
        
        Returns:
            Dicionário com os dados do ponto de coleta
        """
        return {
            "id_ponto": self._id_ponto,
            "nome": self._nome,
            "endereco_completo": self._endereco_completo,
            "horario_funcionamento": self._horario_funcionamento,
            "responsavel": self._responsavel,
            "telefone": self._telefone,
            "email": self._email,
            "ativo": self._ativo,
            "quantidade_itens": self.quantidade_itens,
            "data_cadastro": self._data_cadastro.isoformat()
        }
    
    def __str__(self) -> str:
        """Representação em string do ponto de coleta."""
        status = "Ativo" if self._ativo else "Inativo"
        return f"PontoDeColeta({self._id_ponto}, '{self._nome}', {status})"
    
    def __repr__(self) -> str:
        """Representação técnica do objeto."""
        return (
            f"PontoDeColeta(id={self._id_ponto}, nome='{self._nome}', "
            f"endereco='{self._endereco_completo}')"
        )
