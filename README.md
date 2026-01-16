# 🎒 Projeto Mochila Cheia

O **Mochila Cheia** é uma plataforma digital (aplicativo web) que visa conectar doadores de materiais escolares a estudantes que necessitam desses itens. A solução busca combater o desperdício, promover a sustentabilidade e gerar impacto social positivo, facilitando o acesso a recursos educacionais para famílias de baixa renda.

> **Projeto Integrado II** - Análise e Desenvolvimento de Sistemas (ADS)  
> Universidade Federal do Cariri (UFCA) - Centro de Educação a Distância (CEAD)

---

## 📋 Índice

- [Objetivo](#-objetivo)
- [Funcionalidades Principais](#-funcionalidades-principais-mvp)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Como Executar](#-como-executar)
- [Classes do Sistema](#-classes-do-sistema)
- [Banco de Dados](#-banco-de-dados)
- [Possíveis Usos da Nossa Solução](#-componente-extensionista-possíveis-usos-da-nossa-solução)
- [O que é Projeto Físico de Banco de Dados](#-componente-extensionista-o-que-é-projeto-físico-de-banco-de-dados)
- [Equipe](#-equipe)
- [Licença](#-licença)

---

## 🎯 Objetivo

Criar uma ponte eficiente e confiável entre quem tem materiais para doar e quem precisa, oferecendo um processo com logística simples, seguro e que garanta a privacidade dos usuários.

### O Problema

- **85% das famílias** têm o orçamento impactado pelos gastos com material escolar
- Em favelas, esse número chega a **89%** das famílias
- A falta de recursos básicos contribui para a **evasão escolar**
- Materiais em bom estado são descartados desnecessariamente

### A Solução

Uma plataforma que conecta:
- **Doadores**: Pessoas com materiais escolares em bom estado para doar
- **Receptores**: Estudantes e famílias que precisam desses materiais
- **Pontos de Coleta**: Locais parceiros que facilitam a logística

---

## ✨ Funcionalidades Principais (MVP)

| Funcionalidade | Descrição |
|----------------|-----------|
| **Cadastro de Usuários** | Perfis para Doadores, Receptores e Moderadores |
| **Publicação de Itens** | Cadastro de materiais com fotos, descrição e estado |
| **Busca Inteligente** | Filtros por categoria, localização e disponibilidade |
| **Sistema de Moderação** | Aprovação de itens antes de ficarem disponíveis |
| **Solicitação de Itens** | Receptores podem solicitar itens disponíveis |
| **Chat Integrado** | Comunicação entre doadores e receptores |
| **Notificações** | Alertas sobre solicitações e atualizações |

---

## 🔧 Tecnologias Utilizadas

| Tecnologia | Uso |
|------------|-----|
| **Python 3.10+** | Linguagem principal de programação |
| **SQLite** | Banco de dados para desenvolvimento |
| **PostgreSQL** | Banco de dados para produção (opcional) |
| **Git/GitHub** | Controle de versão e repositório |

### Dependências Python

```
dataclasses-json>=0.6.0
python-dateutil>=2.8.2
bcrypt>=4.0.0
pytest>=7.4.0
```

---

## 📁 Estrutura do Projeto

```
mochila-cheia/
├── README.md                 # Este arquivo
├── requirements.txt          # Dependências Python
├── src/
│   ├── __init__.py
│   ├── models/               # Classes de domínio
│   │   ├── __init__.py
│   │   ├── usuario.py        # Classe Usuario
│   │   ├── item.py           # Classe Item
│   │   ├── solicitacao.py    # Classe Solicitacao
│   │   ├── ponto_coleta.py   # Classe PontoDeColeta
│   │   ├── categoria.py      # Classe Categoria
│   │   └── mensagem.py       # Classe Mensagem
│   └── main.py               # Demonstração do sistema
├── database/
│   ├── schema.sql            # DDL - Projeto Físico
│   └── seed.sql              # Dados de exemplo
├── docs/
│   ├── EP1_Relatorio.md      # Relatório EP1 (POO)
│   └── EP2_Relatorio.md      # Relatório EP2 (Banco)
└── tests/
    └── test_models.py        # Testes unitários
```

---

## 🚀 Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/mochila-cheia.git
cd mochila-cheia
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a demonstração

```bash
cd src
python main.py
```

### 5. (Opcional) Configure o banco de dados

```bash
cd database
sqlite3 mochila_cheia.db < schema.sql
sqlite3 mochila_cheia.db < seed.sql
```

---

## 📦 Classes do Sistema

### Diagrama de Classes Simplificado

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Usuario   │     │  Categoria  │     │ PontoColeta │
├─────────────┤     ├─────────────┤     ├─────────────┤
│ id_usuario  │     │ id_categoria│     │ id_ponto    │
│ nome        │     │ nome        │     │ nome        │
│ email       │     │ descricao   │     │ endereco    │
│ tipo_usuario│     └─────────────┘     │ horario     │
└─────────────┘             │           └─────────────┘
      │                     │
      │        ┌────────────┴────────────┐
      │        │                         │
      ▼        ▼                         │
┌─────────────────┐                      │
│      Item       │◄─────────────────────┘
├─────────────────┤
│ id_item         │
│ titulo          │
│ estado          │
│ status          │
│ doador          │──────► Usuario (composição)
│ categoria       │──────► Categoria (composição)
└─────────────────┘
        │
        │
        ▼
┌─────────────────┐     ┌─────────────────┐
│   Solicitacao   │     │    Mensagem     │
├─────────────────┤     ├─────────────────┤
│ id_solicitacao  │     │ id_mensagem     │
│ item            │     │ remetente       │
│ solicitante     │     │ destinatario    │
│ doador          │     │ conteudo        │
│ status          │     │ solicitacao     │
└─────────────────┘     └─────────────────┘
```

### Princípios de POO Aplicados

| Princípio | Aplicação no Projeto |
|-----------|---------------------|
| **Encapsulamento** | Atributos privados (`_nome`) com acesso via `@property` |
| **Abstração** | Classes modelam entidades do mundo real (Usuario, Item) |
| **Composição** | Item contém referência a Usuario (doador) e Categoria |
| **Agregação** | Solicitação referencia Item e Usuario (podem existir independentemente) |

---

## 🗄️ Banco de Dados

### Modelo Entidade-Relacionamento

```
USUARIO (1) ──────────────── (N) ITEM
    │                              │
    │                              │
    └─── (1) ─── SOLICITACAO ─── (N) ───┘
                     │
                     │
                MENSAGEM (N)
```

### Tabelas Principais

| Tabela | Descrição |
|--------|-----------|
| `USUARIO` | Doadores, receptores e moderadores |
| `CATEGORIA` | Tipos de materiais escolares |
| `ITEM` | Materiais disponíveis para doação |
| `SOLICITACAO` | Pedidos de itens por receptores |
| `MENSAGEM` | Chat entre usuários |
| `PONTO_COLETA` | Locais parceiros |
| `NOTIFICACAO` | Alertas do sistema |

---

## 🌍 [Componente Extensionista] Possíveis Usos da Nossa Solução

A plataforma **Mochila Cheia** foi idealizada para a doação de material escolar, mas seu modelo de intermediação logística pode ser expandido para resolver outros problemas reais, beneficiando diversas comunidades e negócios.

### 1. Apoio a Vítimas de Desastres Naturais

Em situações de emergência, como enchentes ou deslizamentos, a plataforma poderia ser adaptada para se tornar um canal centralizado de doações de itens essenciais (roupas, alimentos não perecíveis, água, kits de higiene). ONGs e a Defesa Civil poderiam atuar como "Pontos de Coleta" verificados, garantindo que as doações cheguem rapidamente a quem mais precisa e evitando o caos logístico comum nessas situações.

### 2. Logística Reversa para Pequenos Negócios

Pequenas empresas e e-commerces enfrentam altos custos com a logística reversa (devolução de produtos). A plataforma poderia ser usada para criar uma rede de "pontos de devolução" em comércios locais (padarias, farmácias). Um cliente que precisa devolver um produto poderia simplesmente deixá-lo no ponto mais próximo, e a plataforma notificaria a empresa para organizar a coleta de múltiplos itens de uma só vez, otimizando rotas e reduzindo custos de transporte.

### 3. Doação de Equipamentos para ONGs e Escolas Públicas

Escolas e organizações sociais frequentemente precisam de equipamentos específicos (computadores, projetores, instrumentos musicais) que empresas ou pessoas físicas têm disponíveis para doação. A plataforma poderia ter uma área dedicada para "listas de desejos", onde instituições publicam suas necessidades. Doadores poderiam consultar essas listas e oferecer exatamente o que é preciso, garantindo que a ajuda seja direcionada e efetiva.

### 4. Banco de Livros Comunitário

Bibliotecas comunitárias e escolas públicas poderiam usar a plataforma para criar um sistema de empréstimo e doação de livros. Moradores doariam livros que não usam mais, e estudantes poderiam solicitá-los para leitura ou pesquisa, devolvendo depois para que outros também possam usar.

> Esses exemplos demonstram o potencial da solução como uma ferramenta flexível para fortalecer a **economia circular** e as **redes de solidariedade**.

---

## 📚 [Componente Extensionista] O que é Projeto Físico de Banco de Dados

### Para quem está começando a programar

O **Projeto Físico de Banco de Dados** é a etapa onde transformamos o modelo conceitual (aqueles diagramas com caixas e linhas) em algo que o computador realmente entende: tabelas, colunas e regras.

### Analogia Simples

Imagine que você vai construir uma casa:

1. **Modelo Conceitual** = O rascunho no papel (quantos quartos, onde fica a cozinha)
2. **Modelo Lógico** = A planta técnica (medidas, posição das portas)
3. **Modelo Físico** = A construção real (tijolos, cimento, encanamento)

No banco de dados, o **Projeto Físico** é como construir a casa de verdade. Definimos:

- **Tabelas**: Como organizar os dados (como as divisões dos cômodos)
- **Tipos de dados**: Se um campo guarda texto, número ou data
- **Chaves primárias**: O "CPF" de cada registro (identificação única)
- **Chaves estrangeiras**: Como as tabelas se conectam
- **Índices**: Atalhos para encontrar dados mais rápido

### Por que isso é importante?

| Motivo | Explicação |
|--------|------------|
| **Performance** | Um banco bem projetado responde rápido |
| **Segurança** | Regras impedem dados errados ou duplicados |
| **Manutenção** | Código organizado é mais fácil de atualizar |
| **Escalabilidade** | O sistema cresce sem quebrar |

### Exemplo Prático

No nosso projeto, a tabela `ITEM` precisa saber quem é o doador. Em vez de repetir o nome do doador em cada item (o que seria um desperdício), usamos uma **chave estrangeira** que aponta para a tabela `USUARIO`:

```sql
CREATE TABLE ITEM (
    id_item INTEGER PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    fk_id_doador INTEGER REFERENCES USUARIO(id_usuario)
);
```

Assim, se o doador mudar de nome, atualizamos em um único lugar!

> **Dica para estudantes**: Pratique criando pequenos bancos de dados para seus projetos pessoais. Comece simples e vá adicionando complexidade conforme aprende.

---

## 👥 Equipe

| Nome | Função | Contribuição |
|------|--------|--------------|
| **Rodrigo Lima Diôgo** | Desenvolvedor Principal | Arquitetura, código das classes, banco de dados, documentação |
| **Júlio Cesar Batista da Silva** | Desenvolvedor | Revisão de código, testes, documentação |

### Nota sobre a Equipe

O projeto inicialmente contava com 6 membros, mas enfrentou desafios significativos devido a **desistências e evasão** ao longo do semestre. Os membros Leidson, Mikael, Nathalia e Pedro Davi não puderam continuar participando ativamente.

Apesar das dificuldades, **Rodrigo e Julio** assumiram a responsabilidade de entregar o projeto completo, demonstrando comprometimento e resiliência diante dos obstáculos.

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos como parte do **Projeto Integrado II** do curso de Análise e Desenvolvimento de Sistemas da UFCA.

---