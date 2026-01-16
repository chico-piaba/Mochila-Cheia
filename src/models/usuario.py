"""
Classe Usuario - Mochila Cheia

Esta classe representa os usuários do sistema, que podem ser:
- DOADOR: Pessoa que disponibiliza materiais escolares para doação
- RECEPTOR: Estudante ou família que precisa receber materiais
- MODERADOR: Administrador que aprova itens cadastrados

Princípios de POO aplicados:
- Encapsulamento: Atributos privados com acesso via @property
- Abstração: Modelagem de entidades do mundo real
"""

from enum import Enum
from datetime import datetime
from typing import Optional
import hashlib


class TipoUsuario(Enum):
    """Enumeração para os tipos de usuário do sistema."""
    DOADOR = "doador"
    RECEPTOR = "receptor"
    MODERADOR = "moderador"


class Usuario:
    """
    Classe que representa um usuário do sistema Mochila Cheia.
    
    Um usuário pode ser um doador (quem oferece materiais), um receptor
    (quem precisa dos materiais) ou um moderador (administrador).
    
    Attributes:
        id_usuario (int): Identificador único do usuário
        nome (str): Nome completo do usuário
        email (str): E-mail para login e contato
        telefone (str): Telefone para contato
        endereco (str): Cidade e bairro para geolocalização
        tipo_usuario (TipoUsuario): Tipo do perfil do usuário
        data_cadastro (datetime): Data de criação da conta
    
    Example:
        >>> doador = Usuario(
        ...     id_usuario=1,
        ...     nome="Maria Silva",
        ...     email="maria@email.com",
        ...     senha="senha123",
        ...     tipo_usuario=TipoUsuario.DOADOR
        ... )
        >>> doador.nome
        'Maria Silva'
    """
    
    # Contador estático para gerar IDs únicos
    _contador_id: int = 0
    
    def __init__(
        self,
        nome: str,
        email: str,
        senha: str,
        tipo_usuario: TipoUsuario,
        id_usuario: Optional[int] = None,
        telefone: Optional[str] = None,
        endereco: Optional[str] = None,
        data_cadastro: Optional[datetime] = None
    ):
        """
        Inicializa um novo usuário.
        
        Args:
            nome: Nome completo do usuário
            email: E-mail único para login
            senha: Senha em texto plano (será armazenada como hash)
            tipo_usuario: Tipo do perfil (DOADOR, RECEPTOR ou MODERADOR)
            id_usuario: ID opcional (gerado automaticamente se não fornecido)
            telefone: Número de telefone para contato
            endereco: Localização (cidade/bairro)
            data_cadastro: Data de criação (usa data atual se não fornecida)
        """
        # Gera ID automaticamente se não fornecido
        if id_usuario is None:
            Usuario._contador_id += 1
            self._id_usuario = Usuario._contador_id
        else:
            self._id_usuario = id_usuario
            # Atualiza contador se ID fornecido for maior
            if id_usuario > Usuario._contador_id:
                Usuario._contador_id = id_usuario
        
        # Atributos privados (encapsulamento)
        self._nome = nome
        self._email = email
        self._senha_hash = self._hash_senha(senha)
        self._telefone = telefone
        self._endereco = endereco
        self._tipo_usuario = tipo_usuario
        self._data_cadastro = data_cadastro or datetime.now()
        self._ativo = True
    
    # ==================== PROPRIEDADES (GETTERS) ====================
    
    @property
    def id_usuario(self) -> int:
        """Retorna o ID único do usuário."""
        return self._id_usuario
    
    @property
    def nome(self) -> str:
        """Retorna o nome do usuário."""
        return self._nome
    
    @nome.setter
    def nome(self, valor: str) -> None:
        """Define o nome do usuário com validação."""
        if not valor or len(valor.strip()) < 2:
            raise ValueError("Nome deve ter pelo menos 2 caracteres")
        self._nome = valor.strip()
    
    @property
    def email(self) -> str:
        """Retorna o e-mail do usuário."""
        return self._email
    
    @email.setter
    def email(self, valor: str) -> None:
        """Define o e-mail do usuário com validação básica."""
        if not valor or "@" not in valor:
            raise ValueError("E-mail inválido")
        self._email = valor.lower().strip()
    
    @property
    def telefone(self) -> Optional[str]:
        """Retorna o telefone do usuário."""
        return self._telefone
    
    @telefone.setter
    def telefone(self, valor: Optional[str]) -> None:
        """Define o telefone do usuário."""
        self._telefone = valor
    
    @property
    def endereco(self) -> Optional[str]:
        """Retorna o endereço do usuário."""
        return self._endereco
    
    @endereco.setter
    def endereco(self, valor: Optional[str]) -> None:
        """Define o endereço do usuário."""
        self._endereco = valor
    
    @property
    def tipo_usuario(self) -> TipoUsuario:
        """Retorna o tipo do usuário."""
        return self._tipo_usuario
    
    @property
    def data_cadastro(self) -> datetime:
        """Retorna a data de cadastro do usuário."""
        return self._data_cadastro
    
    @property
    def ativo(self) -> bool:
        """Retorna se o usuário está ativo."""
        return self._ativo
    
    # ==================== MÉTODOS PRIVADOS ====================
    
    @staticmethod
    def _hash_senha(senha: str) -> str:
        """
        Gera um hash da senha para armazenamento seguro.
        
        Args:
            senha: Senha em texto plano
            
        Returns:
            Hash SHA-256 da senha
        """
        return hashlib.sha256(senha.encode()).hexdigest()
    
    # ==================== MÉTODOS PÚBLICOS ====================
    
    def cadastrar(self) -> dict:
        """
        Realiza o cadastro do usuário (simulação).
        
        Em uma implementação real, este método persistiria
        os dados no banco de dados.
        
        Returns:
            Dicionário com os dados do usuário cadastrado
        """
        print(f"✅ Usuário '{self._nome}' cadastrado com sucesso!")
        return self.to_dict()
    
    def login(self, email: str, senha: str) -> bool:
        """
        Autentica o usuário no sistema.
        
        Args:
            email: E-mail informado
            senha: Senha informada
            
        Returns:
            True se as credenciais estiverem corretas, False caso contrário
        """
        senha_hash = self._hash_senha(senha)
        if self._email == email.lower() and self._senha_hash == senha_hash:
            print(f"✅ Login realizado com sucesso! Bem-vindo(a), {self._nome}!")
            return True
        print("❌ E-mail ou senha incorretos.")
        return False
    
    def atualizar_perfil(
        self,
        nome: Optional[str] = None,
        telefone: Optional[str] = None,
        endereco: Optional[str] = None
    ) -> None:
        """
        Atualiza as informações do perfil do usuário.
        
        Args:
            nome: Novo nome (opcional)
            telefone: Novo telefone (opcional)
            endereco: Novo endereço (opcional)
        """
        if nome:
            self.nome = nome
        if telefone is not None:
            self.telefone = telefone
        if endereco is not None:
            self.endereco = endereco
        print(f"✅ Perfil de '{self._nome}' atualizado com sucesso!")
    
    def alterar_senha(self, senha_atual: str, nova_senha: str) -> bool:
        """
        Altera a senha do usuário.
        
        Args:
            senha_atual: Senha atual para verificação
            nova_senha: Nova senha desejada
            
        Returns:
            True se a senha foi alterada, False caso contrário
        """
        if self._hash_senha(senha_atual) != self._senha_hash:
            print("❌ Senha atual incorreta.")
            return False
        
        if len(nova_senha) < 6:
            print("❌ A nova senha deve ter pelo menos 6 caracteres.")
            return False
        
        self._senha_hash = self._hash_senha(nova_senha)
        print("✅ Senha alterada com sucesso!")
        return True
    
    def desativar_conta(self) -> None:
        """Desativa a conta do usuário."""
        self._ativo = False
        print(f"⚠️ Conta de '{self._nome}' desativada.")
    
    def to_dict(self) -> dict:
        """
        Converte o objeto para dicionário.
        
        Returns:
            Dicionário com os dados do usuário (exceto senha)
        """
        return {
            "id_usuario": self._id_usuario,
            "nome": self._nome,
            "email": self._email,
            "telefone": self._telefone,
            "endereco": self._endereco,
            "tipo_usuario": self._tipo_usuario.value,
            "data_cadastro": self._data_cadastro.isoformat(),
            "ativo": self._ativo
        }
    
    def __str__(self) -> str:
        """Representação em string do usuário."""
        return f"Usuario({self._id_usuario}, {self._nome}, {self._tipo_usuario.value})"
    
    def __repr__(self) -> str:
        """Representação técnica do objeto."""
        return (
            f"Usuario(id={self._id_usuario}, nome='{self._nome}', "
            f"email='{self._email}', tipo={self._tipo_usuario.value})"
        )
