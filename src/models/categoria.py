"""
Classe Categoria - Mochila Cheia

Esta classe representa as categorias de itens disponíveis para doação,
como: Mochilas, Livros, Cadernos, Estojos, Material de Escrita, etc.

Princípios de POO aplicados:
- Encapsulamento: Atributos privados com acesso controlado via @property
- Abstração: Representa a classificação de materiais escolares
"""

from typing import Optional, List


class Categoria:
    """
    Classe que representa uma categoria de materiais escolares.
    
    As categorias organizam os itens do sistema, facilitando a busca
    e a navegação pelos materiais disponíveis para doação.
    
    Attributes:
        id_categoria (int): Identificador único da categoria
        nome (str): Nome da categoria (ex: "Mochila", "Livro")
        descricao (str): Descrição detalhada da categoria
    
    Example:
        >>> cat_mochilas = Categoria(
        ...     nome="Mochilas",
        ...     descricao="Mochilas escolares de todos os tamanhos"
        ... )
        >>> print(cat_mochilas.nome)
        'Mochilas'
    """
    
    # Contador estático para gerar IDs únicos
    _contador_id: int = 0
    
    # Lista de categorias padrão do sistema
    CATEGORIAS_PADRAO = [
        ("Mochilas", "Mochilas escolares de diversos tamanhos e modelos"),
        ("Livros", "Livros didáticos, paradidáticos e literatura infantojuvenil"),
        ("Cadernos", "Cadernos de todas as matérias e quantidades de folhas"),
        ("Estojos", "Estojos para guardar material de escrita"),
        ("Material de Escrita", "Canetas, lápis, borrachas, apontadores, etc."),
        ("Material de Arte", "Tintas, pincéis, papéis coloridos, tesouras, etc."),
        ("Uniformes", "Uniformes escolares em bom estado"),
        ("Calculadoras", "Calculadoras científicas e básicas"),
        ("Outros", "Outros materiais escolares não categorizados")
    ]
    
    def __init__(
        self,
        nome: str,
        descricao: Optional[str] = None,
        id_categoria: Optional[int] = None
    ):
        """
        Inicializa uma nova categoria.
        
        Args:
            nome: Nome da categoria
            descricao: Descrição opcional da categoria
            id_categoria: ID opcional (gerado automaticamente se não fornecido)
        """
        # Gera ID automaticamente se não fornecido
        if id_categoria is None:
            Categoria._contador_id += 1
            self._id_categoria = Categoria._contador_id
        else:
            self._id_categoria = id_categoria
            if id_categoria > Categoria._contador_id:
                Categoria._contador_id = id_categoria
        
        # Atributos privados (encapsulamento)
        self._nome = nome
        self._descricao = descricao or ""
        self._ativa = True
    
    # ==================== PROPRIEDADES (GETTERS/SETTERS) ====================
    
    @property
    def id_categoria(self) -> int:
        """Retorna o ID único da categoria."""
        return self._id_categoria
    
    @property
    def nome(self) -> str:
        """Retorna o nome da categoria."""
        return self._nome
    
    @nome.setter
    def nome(self, valor: str) -> None:
        """Define o nome da categoria com validação."""
        if not valor or len(valor.strip()) < 2:
            raise ValueError("Nome da categoria deve ter pelo menos 2 caracteres")
        self._nome = valor.strip()
    
    @property
    def descricao(self) -> str:
        """Retorna a descrição da categoria."""
        return self._descricao
    
    @descricao.setter
    def descricao(self, valor: str) -> None:
        """Define a descrição da categoria."""
        self._descricao = valor.strip() if valor else ""
    
    @property
    def ativa(self) -> bool:
        """Retorna se a categoria está ativa."""
        return self._ativa
    
    # ==================== MÉTODOS DE CLASSE ====================
    
    @classmethod
    def criar_categorias_padrao(cls) -> List['Categoria']:
        """
        Cria e retorna a lista de categorias padrão do sistema.
        
        Returns:
            Lista de objetos Categoria com as categorias padrão
        """
        categorias = []
        for nome, descricao in cls.CATEGORIAS_PADRAO:
            categorias.append(cls(nome=nome, descricao=descricao))
        return categorias
    
    @classmethod
    def resetar_contador(cls) -> None:
        """Reseta o contador de IDs (útil para testes)."""
        cls._contador_id = 0
    
    # ==================== MÉTODOS PÚBLICOS ====================
    
    def desativar(self) -> None:
        """Desativa a categoria."""
        self._ativa = False
        print(f"⚠️ Categoria '{self._nome}' desativada.")
    
    def ativar(self) -> None:
        """Reativa a categoria."""
        self._ativa = True
        print(f"✅ Categoria '{self._nome}' ativada.")
    
    def to_dict(self) -> dict:
        """
        Converte o objeto para dicionário.
        
        Returns:
            Dicionário com os dados da categoria
        """
        return {
            "id_categoria": self._id_categoria,
            "nome": self._nome,
            "descricao": self._descricao,
            "ativa": self._ativa
        }
    
    def __str__(self) -> str:
        """Representação em string da categoria."""
        return f"Categoria({self._id_categoria}, {self._nome})"
    
    def __repr__(self) -> str:
        """Representação técnica do objeto."""
        return f"Categoria(id={self._id_categoria}, nome='{self._nome}')"
    
    def __eq__(self, other) -> bool:
        """Compara duas categorias pelo ID."""
        if isinstance(other, Categoria):
            return self._id_categoria == other._id_categoria
        return False
    
    def __hash__(self) -> int:
        """Retorna o hash da categoria (baseado no ID)."""
        return hash(self._id_categoria)
