# Entregável Parcial 1 (EP1) - Relatório

**PROJETO INTEGRADO II [ADS0013]**  
**Prof. Allysson Allex Araújo**  
**allysson.araujo@ufca.edu.br**

**DATA DE ENTREGA:** 15/12/2025 às 23h59

---

## Identificação do Time

| Nome Completo | Matrícula | Situação |
|---------------|-----------|----------|
| Rodrigo Lima Diôgo | [MATRÍCULA] | ✅ Ativo |
| Júlio Cesar Batista da Silva | [MATRÍCULA] | ✅ Ativo |
| Leidson Oliveira Lima | [MATRÍCULA] | ❌ Desistente |
| Mikael Ramon Tavares Barbosa | [MATRÍCULA] | ❌ Desistente |
| Nathalia Campos De Castro | [MATRÍCULA] | ❌ Desistente |
| Pedro Davi Monteiro Bezerra | [MATRÍCULA] | ❌ Desistente |

**Observação importante:** O projeto enfrentou desafios significativos com a desistência de 4 membros da equipe original durante o semestre. Os membros remanescentes (Rodrigo e Julio) assumiram integralmente o desenvolvimento do projeto.

---

## 1) Explicação de como a equipe atendeu aos requisitos

### a) Implementação das Classes Principais

O projeto **Mochila Cheia** foi implementado em **Python 3.10+**, utilizando os conceitos fundamentais de Programação Orientada a Objetos.

#### Estrutura de Classes Implementadas

Foram desenvolvidas **6 classes principais** que representam as entidades centrais do sistema:

##### 1. Classe `Usuario` (`src/models/usuario.py`)

```python
class Usuario:
    """Representa os usuários do sistema (doadores, receptores, moderadores)."""
    
    def __init__(self, nome, email, senha, tipo_usuario, ...):
        self._id_usuario = ...      # Atributo privado
        self._nome = nome
        self._email = email
        self._senha_hash = self._hash_senha(senha)  # Segurança
        self._tipo_usuario = tipo_usuario
        
    @property
    def nome(self):
        """Getter com encapsulamento."""
        return self._nome
    
    def cadastrar(self):
        """Registra o usuário no sistema."""
        ...
    
    def login(self, email, senha):
        """Autentica o usuário."""
        ...
```

**Decisões de projeto:**
- Atributos privados (`_nome`, `_email`) protegem os dados
- Hash de senha para segurança (nunca armazenamos texto plano)
- Enum `TipoUsuario` para garantir valores válidos
- Contador estático para gerar IDs únicos automaticamente

##### 2. Classe `Item` (`src/models/item.py`)

```python
class Item:
    """Representa um material escolar para doação."""
    
    def __init__(self, titulo, descricao, categoria, estado_conservacao, doador, ...):
        self._titulo = titulo
        self._categoria = categoria  # Composição
        self._doador = doador        # Composição
        self._status = StatusItem.PENDENTE_MODERACAO
        
    def aprovar(self):
        """Moderador aprova o item."""
        self.atualizar_status(StatusItem.DISPONIVEL)
    
    def reservar(self):
        """Reserva o item para um receptor."""
        if self.esta_disponivel():
            self.atualizar_status(StatusItem.RESERVADO)
```

**Decisões de projeto:**
- **Composição** com `Usuario` (doador) e `Categoria`
- Fluxo de estados: PENDENTE → DISPONIVEL → RESERVADO → DOADO
- Validações antes de alterações de status

##### 3. Classe `Solicitacao` (`src/models/solicitacao.py`)

```python
class Solicitacao:
    """Representa uma solicitação de doação."""
    
    def __init__(self, item, solicitante, doador, ...):
        self._item = item              # Agregação
        self._solicitante = solicitante # Agregação
        self._status = StatusSolicitacao.PENDENTE
        
    def aceitar(self):
        """Doador aceita a solicitação."""
        self._item.reservar()
        self._status = StatusSolicitacao.ACEITA
    
    def finalizar(self):
        """Conclui a doação."""
        self._item.finalizar_doacao()
        self._status = StatusSolicitacao.FINALIZADA
```

**Decisões de projeto:**
- **Agregação** com `Item` e `Usuario` (objetos independentes)
- Validações impedem operações inválidas (ex: aceitar solicitação já aceita)
- Integração com o status do Item

##### 4. Classe `PontoDeColeta` (`src/models/ponto_coleta.py`)

Gerencia locais parceiros para entrega/retirada de itens.

##### 5. Classe `Categoria` (`src/models/categoria.py`)

Classifica os tipos de materiais escolares (Mochilas, Livros, etc.).

##### 6. Classe `Mensagem` (`src/models/mensagem.py`)

Permite comunicação entre doadores e receptores.

#### Processo de Desenvolvimento

1. **Análise de Requisitos**: Baseado no modelo conceitual das sprints anteriores
2. **Modelagem**: Definição de atributos e métodos de cada classe
3. **Implementação**: Código em Python seguindo boas práticas
4. **Testes**: Validação do funcionamento via script `main.py`
5. **Documentação**: README e comentários no código

### b) Princípios e Práticas de POO Utilizadas

| Princípio | Aplicação no Projeto | Exemplo |
|-----------|---------------------|---------|
| **Encapsulamento** | Todos os atributos são privados (`_atributo`) com acesso via `@property` | `self._nome` → `usuario.nome` |
| **Abstração** | Classes modelam entidades do mundo real | `Usuario`, `Item`, `Solicitacao` |
| **Composição** | Item contém Usuario (doador) e Categoria | `self._doador = doador` |
| **Agregação** | Solicitação referencia Item e Usuario | Objetos existem independentemente |

#### Exemplos de Encapsulamento

```python
class Usuario:
    def __init__(self, nome, ...):
        self._nome = nome  # Atributo privado
    
    @property
    def nome(self):
        """Getter - controla acesso de leitura."""
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        """Setter - valida antes de alterar."""
        if len(valor) < 2:
            raise ValueError("Nome muito curto")
        self._nome = valor
```

#### Exemplo de Composição

```python
class Item:
    def __init__(self, ..., doador: Usuario, categoria: Categoria):
        # Item "contém" Usuario e Categoria
        # Se Item for destruído, a referência é perdida
        self._doador = doador
        self._categoria = categoria
```

### c) [Componente Extensionista] Possíveis Usos da Solução

A seção **"Possíveis usos da nossa solução"** foi criada no README.md do repositório, detalhando 4 cenários de aplicação:

1. **Apoio a Vítimas de Desastres Naturais** - Doações emergenciais
2. **Logística Reversa para Pequenos Negócios** - Pontos de devolução
3. **Doação de Equipamentos para ONGs** - Listas de desejos
4. **Banco de Livros Comunitário** - Sistema de empréstimo

> [Link para a seção no README](../README.md#-componente-extensionista-possíveis-usos-da-nossa-solução)

---

## 2) Link do Vídeo Explicativo

**Link do vídeo no Google Drive:**

`[INSERIR LINK DO VÍDEO AQUI]`

**Conteúdo do vídeo (até 5 minutos):**
- Apresentação da equipe (Rodrigo e Julio)
- Demonstração do código funcionando (`python main.py`)
- Explicação dos princípios de POO aplicados
- Tour pelo repositório GitHub
- Discussão sobre os desafios enfrentados

---

## 3) Link do Repositório no GitHub

**Link do repositório:**

`[INSERIR LINK DO REPOSITÓRIO AQUI]`

**Estrutura do repositório:**
```
mochila-cheia/
├── README.md           ✅ Documentação completa
├── requirements.txt    ✅ Dependências
├── src/models/         ✅ Classes implementadas
├── database/           ✅ Scripts SQL
└── docs/               ✅ Relatórios
```

---

## 4) Contribuição de Cada Membro

### Membros Ativos

| Membro | Contribuições |
|--------|---------------|
| **Rodrigo Lima Diôgo** | - Arquitetura do sistema<br>- Implementação de todas as 6 classes<br>- Script de demonstração (main.py)<br>- Projeto físico do banco de dados<br>- Documentação (README, relatórios)<br>- Coordenação do time |
| **Júlio Cesar Batista da Silva** | - Revisão de código<br>- Testes de funcionamento<br>- Contribuições na documentação<br>- Feedback sobre a estrutura das classes |

### Membros Desistentes

| Membro | Situação |
|--------|----------|
| Leidson Oliveira Lima | Desistiu durante o semestre |
| Mikael Ramon Tavares Barbosa | Desistiu durante o semestre |
| Nathalia Campos De Castro | Desistiu durante o semestre |
| Pedro Davi Monteiro Bezerra | Desistiu durante o semestre |

---

## 5) Evidências das Contribuições

### Evidências Coletivas

**Commits no GitHub:**
- [Screenshot dos commits mostrando contribuições]

**Discussões de desenvolvimento:**
- [Screenshot de conversas sobre decisões técnicas]

### Evidências Individuais

**Rodrigo Lima:**
- Autor dos principais commits
- Responsável pela arquitetura

**Julio Cesar:**
- Revisões de código
- Testes de funcionalidade

### Desafios Enfrentados

1. **Desistência de membros:** 4 dos 6 membros deixaram o projeto
2. **Sobrecarga de trabalho:** Todo o desenvolvimento ficou com 2 pessoas
3. **Reorganização:** Necessidade de replanejar escopo e cronograma
4. **Comunicação:** Dificuldade de alinhar com membros que desistiram

> Apesar das dificuldades, o projeto foi entregue com todas as funcionalidades planejadas, demonstrando o comprometimento dos membros remanescentes.

---

## 6) Formulário de Autoavaliação

☑️ Ciência de que cada membro deve responder individualmente ao [formulário de autoavaliação](https://forms.gle/mvCiEaW11LgpUHjf9) após a entrega.

---

## Conclusão

O **Entregável Parcial 1** foi concluído com sucesso, incluindo:

- ✅ 6 classes principais implementadas em Python
- ✅ Princípios de POO aplicados (encapsulamento, abstração, composição)
- ✅ Código disponível no GitHub
- ✅ README com documentação completa
- ✅ Seção extensionista sobre possíveis usos
- ✅ Script de demonstração funcionando

O projeto demonstra a aplicação prática dos conceitos de Programação Orientada a Objetos em um cenário real de impacto social.
