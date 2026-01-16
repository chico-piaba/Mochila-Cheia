# Entregável Parcial 2 (EP2) - Relatório

**PROJETO INTEGRADO II [ADS0013]**  
**Prof. Allysson Allex Araújo**  
**allysson.araujo@ufca.edu.br**

**DATA DE ENTREGA:** 16/02/2026 às 23h59

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

**Observação:** Conforme relatado no EP1, o projeto foi desenvolvido pelos membros remanescentes após a desistência de 4 integrantes da equipe original.

---

## 1) Explicação de como a equipe atendeu aos requisitos

### a) Definição do Projeto Físico

O **Projeto Físico de Banco de Dados** do Mochila Cheia foi implementado utilizando **SQLite** (desenvolvimento) com compatibilidade para **PostgreSQL** (produção).

#### Diagrama Entidade-Relacionamento (DER)

```
                          ┌──────────────────┐
                          │    CATEGORIA     │
                          ├──────────────────┤
                          │ PK id_categoria  │
                          │    nome          │
                          │    descricao     │
                          └────────┬─────────┘
                                   │ 1
                                   │
                                   │ N
┌──────────────────┐      ┌───────┴──────────┐      ┌──────────────────┐
│     USUARIO      │      │       ITEM       │      │   PONTO_COLETA   │
├──────────────────┤      ├──────────────────┤      ├──────────────────┤
│ PK id_usuario    │──1───│ PK id_item       │───0..1│ PK id_ponto      │
│    nome          │  N   │    titulo        │      │    nome          │
│    email (UQ)    │      │    descricao     │      │    endereco      │
│    senha_hash    │      │    estado        │      │    horario       │
│    telefone      │      │    status        │      │    responsavel   │
│    endereco      │      │ FK fk_id_doador  │      └──────────────────┘
│    tipo_usuario  │      │ FK fk_id_categoria│
│    data_cadastro │      │ FK fk_id_ponto   │
└────────┬─────────┘      │ FK fk_id_moderador│
         │                └────────┬─────────┘
         │ 1                       │ 1
         │                         │
         │ N                       │ N
┌────────┴─────────┐      ┌───────┴──────────┐
│   SOLICITACAO    │──────│    MENSAGEM      │
├──────────────────┤  1   ├──────────────────┤
│ PK id_solicitacao│  N   │ PK id_mensagem   │
│    status        │      │    conteudo      │
│    ordem_fila    │      │    status        │
│    data_solic.   │      │    data_envio    │
│ FK fk_id_item    │      │ FK fk_remetente  │
│ FK fk_id_receptor│      │ FK fk_destinatario│
└──────────────────┘      │ FK fk_solicitacao│
                          └──────────────────┘
                          
                          ┌──────────────────┐
                          │   NOTIFICACAO    │
                          ├──────────────────┤
                          │ PK id_notificacao│
                          │    titulo        │
                          │    mensagem      │
                          │    status        │
                          │ FK fk_id_usuario │
                          │ FK fk_id_item    │
                          │ FK fk_solicitacao│
                          └──────────────────┘

Legenda:
PK = Primary Key (Chave Primária)
FK = Foreign Key (Chave Estrangeira)
UQ = Unique (Único)
1:N = Um para Muitos
0..1 = Zero ou Um (opcional)
```

#### Arquivo schema.sql

O projeto físico completo está no arquivo `database/schema.sql`, contendo:

- **7 tabelas** com todos os atributos
- **Chaves primárias** auto-incremento
- **Chaves estrangeiras** com regras ON DELETE
- **Constraints** CHECK para validação
- **Índices** para otimização de consultas
- **3 Views** para consultas frequentes

### b) Justificativas das Escolhas de Projeto

#### Tabelas e Suas Justificativas

| Tabela | Justificativa |
|--------|---------------|
| **USUARIO** | Centraliza todos os tipos de usuários (doadores, receptores, moderadores) em uma única tabela com coluna `tipo_usuario`, evitando redundância |
| **CATEGORIA** | Tabela separada permite adicionar novas categorias sem alterar código; relacionamento 1:N com ITEM |
| **ITEM** | Entidade principal; possui múltiplas FKs para conectar com doador, categoria e ponto de coleta |
| **SOLICITACAO** | Registra o processo de pedido; conecta receptor a item; impede duplicatas via UNIQUE |
| **MENSAGEM** | Permite chat entre usuários; vinculada à solicitação para contexto |
| **PONTO_COLETA** | Separada de USUARIO pois tem atributos específicos (horário, responsável) |
| **NOTIFICACAO** | Sistema de alertas; FKs opcionais para item/solicitação |

#### Tipos de Dados Escolhidos

| Tipo | Uso | Justificativa |
|------|-----|---------------|
| `INTEGER` | IDs, contadores | Eficiente, suporta AUTO_INCREMENT |
| `VARCHAR(n)` | Textos com limite | Economiza espaço, valida tamanho |
| `TEXT` | Descrições longas | Sem limite fixo, flexibilidade |
| `TIMESTAMP` | Datas com hora | Precisão para rastreamento |
| `BOOLEAN` | Flags (ativo/inativo) | Simples, eficiente |

#### Chaves Primárias

```sql
-- Todas as tabelas usam chave surrogate com auto-incremento
id_usuario INTEGER PRIMARY KEY AUTOINCREMENT
id_item INTEGER PRIMARY KEY AUTOINCREMENT
```

**Justificativa:** 
- Chaves surrogate são independentes do negócio
- Auto-incremento garante unicidade automaticamente
- Inteiros são eficientes para índices e joins

#### Chaves Estrangeiras

| FK | Regra ON DELETE | Justificativa |
|----|-----------------|---------------|
| `fk_id_doador` → USUARIO | CASCADE | Se doador é excluído, seus itens também são |
| `fk_id_categoria` → CATEGORIA | RESTRICT | Impede excluir categoria com itens |
| `fk_id_ponto` → PONTO_COLETA | SET NULL | Item pode existir sem ponto de coleta |
| `fk_id_moderador` → USUARIO | SET NULL | Mantém histórico mesmo sem moderador |

#### Índices Criados

```sql
-- Índices para otimização de consultas frequentes
CREATE INDEX idx_item_status ON ITEM(status);
CREATE INDEX idx_item_doador ON ITEM(fk_id_doador);
CREATE INDEX idx_solicitacao_status ON SOLICITACAO(status);
CREATE INDEX idx_usuario_email ON USUARIO(email);
```

**Justificativa:**
- Consultas por status são muito frequentes
- Busca por doador é comum na listagem
- E-mail é usado no login (UNIQUE já cria índice)

#### Constraints CHECK

```sql
-- Validação de enumerações via CHECK
tipo_usuario VARCHAR(20) CHECK (tipo_usuario IN ('doador', 'receptor', 'moderador'))
status VARCHAR(30) CHECK (status IN ('pendente_moderacao', 'disponivel', ...))
```

**Justificativa:**
- Garante integridade dos dados
- Evita valores inválidos
- Substituição de ENUM (compatibilidade SQLite/PostgreSQL)

### c) [Componente Extensionista] Explicação do Projeto Físico

A seção **"O que é Projeto Físico de Banco de Dados"** foi adicionada ao README.md com uma explicação acessível para estudantes iniciantes.

**Conteúdo da seção:**
- Analogia com construção de casa
- Explicação de tabelas, tipos, chaves e índices
- Por que é importante (performance, segurança, manutenção)
- Exemplo prático do nosso projeto

> [Link para a seção no README](../README.md#-componente-extensionista-o-que-é-projeto-físico-de-banco-de-dados)

**Trecho da explicação:**

> O **Projeto Físico de Banco de Dados** é a etapa onde transformamos o modelo conceitual em algo que o computador realmente entende: tabelas, colunas e regras.
>
> Imagine que você vai construir uma casa:
> 1. **Modelo Conceitual** = O rascunho no papel
> 2. **Modelo Lógico** = A planta técnica
> 3. **Modelo Físico** = A construção real

---

## 2) Link do Vídeo Explicativo

**Link do vídeo no Google Drive:**

`[INSERIR LINK DO VÍDEO AQUI]`

**Conteúdo do vídeo (até 5 minutos):**
- Apresentação do projeto físico
- Explicação do diagrama ER
- Demonstração do schema.sql
- Justificativas das decisões técnicas
- Execução do script com dados de exemplo

---

## 3) Link do Repositório no GitHub

**Link do repositório:**

`[INSERIR LINK DO REPOSITÓRIO AQUI]`

**Arquivos relevantes para EP2:**
```
database/
├── schema.sql   ✅ DDL completo (CREATE TABLE, INDEX, VIEW)
└── seed.sql     ✅ Dados de exemplo
```

---

## 4) Contribuição de Cada Membro

### Membros Ativos

| Membro | Contribuições no EP2 |
|--------|----------------------|
| **Rodrigo Lima Diôgo** | - Modelagem do projeto físico<br>- Criação do schema.sql<br>- Definição de índices e constraints<br>- Script seed.sql<br>- Documentação das justificativas |
| **Júlio Cesar Batista da Silva** | - Revisão do modelo<br>- Testes de integridade<br>- Contribuições na documentação |

### Membros Desistentes

Os mesmos 4 membros que desistiram no EP1 permaneceram ausentes: Leidson, Mikael, Nathalia e Pedro Davi.

---

## 5) Evidências das Contribuições

### Evidências do Trabalho

**Arquivo schema.sql:**
- 7 tabelas criadas
- 15+ índices para otimização
- 3 views para consultas frequentes
- Comentários explicativos em todo o código

**Arquivo seed.sql:**
- 8 usuários de exemplo
- 4 pontos de coleta
- 8 itens em diferentes estados
- Solicitações e mensagens de exemplo

**Teste de funcionamento:**
```bash
# Criação do banco
sqlite3 mochila_cheia.db < schema.sql

# População com dados
sqlite3 mochila_cheia.db < seed.sql

# Consulta de teste
sqlite3 mochila_cheia.db "SELECT * FROM vw_itens_disponiveis;"
```

---

## 6) Formulário de Autoavaliação

☑️ Ciência de que cada membro deve responder individualmente ao [formulário de autoavaliação](https://forms.gle/mvCiEaW11LgpUHjf9) após a entrega.

---

## Conclusão

O **Entregável Parcial 2** foi concluído com sucesso, incluindo:

- ✅ Projeto físico completo (schema.sql)
- ✅ 7 tabelas com relacionamentos definidos
- ✅ Chaves primárias, estrangeiras e índices
- ✅ Constraints para validação de dados
- ✅ Views para consultas frequentes
- ✅ Dados de exemplo (seed.sql)
- ✅ Seção extensionista no README
- ✅ Documentação das justificativas

O banco de dados foi projetado para suportar todas as funcionalidades do MVP do Mochila Cheia, com foco em **integridade, performance e manutenibilidade**.

---

## Anexo: Estatísticas do Schema

| Elemento | Quantidade |
|----------|------------|
| Tabelas | 7 |
| Chaves Primárias | 7 |
| Chaves Estrangeiras | 11 |
| Índices | 16 |
| Constraints CHECK | 8 |
| Views | 3 |
