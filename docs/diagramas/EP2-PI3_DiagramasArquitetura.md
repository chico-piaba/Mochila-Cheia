# Diagramas Arquiteturais — EP2 (PI3) · Mochila Cheia

Diagramas do modelo arquitetural do MVP Web. Renderizam diretamente no GitHub
(Mermaid). Complementam o documento `docs/EP2-PI3_Arquitetura.md`.

---

## 1. Diagrama de Camadas

Mostra a divisão em quatro camadas e o sentido das dependências.

```mermaid
flowchart TD
    A["🖥️ APRESENTAÇÃO (View)<br/>Templates Jinja2 + CSS/JS"]
    B["🔀 CONTROLE (Controller)<br/>Blueprints Flask"]
    C["🧠 DOMÍNIO / SERVIÇO (Model)<br/>Classes POO (regras de negócio)"]
    D["🗄️ PERSISTÊNCIA (Data)<br/>database.py + Repositories → SQLite"]

    A -- "requisição HTTP" --> B
    B -- "chamadas de método" --> C
    C -- "padrão Repository" --> D
    D -- "dados" --> C
    C -- "objetos" --> B
    B -- "HTML (render_template)" --> A
```

---

## 2. Diagrama de Componentes

Detalha os módulos da aplicação e suas comunicações.

```mermaid
flowchart LR
    subgraph Cliente
        NAV["Navegador<br/>(Doador/Receptor/Moderador)"]
    end
    subgraph Servidor["Servidor Flask (Application Factory)"]
        FAC["create_app()"]
        AUTH["Autenticação"]
        ITENS["Itens"]
        SOLIC["Solicitações"]
        MOD["Moderação"]
        MSG["Mensagens (Chat)"]
        NOT["Notificações"]
        DOM["Domínio POO"]
        REPO["Repositories"]
    end
    DB[("SQLite<br/>mochila_cheia.db")]

    NAV -- HTTP --> FAC
    FAC --> AUTH & ITENS & SOLIC & MOD & MSG & NOT
    AUTH & ITENS & SOLIC & MOD & MSG & NOT --> DOM
    DOM --> REPO
    REPO --> DB
```

---

## 3. Fluxo de uma Requisição (exemplo: página inicial)

Sequência de uma requisição atravessando todas as camadas.

```mermaid
sequenceDiagram
    participant U as Usuário (navegador)
    participant C as Controller (home.index)
    participant R as EstatisticasRepository
    participant DB as SQLite
    participant V as Template (index.html)

    U->>C: GET /
    C->>R: resumo() e itens_disponiveis()
    R->>DB: SELECT (views vw_estatisticas / vw_itens_disponiveis)
    DB-->>R: linhas (sqlite3.Row)
    R-->>C: dados prontos
    C->>V: render_template(resumo, itens)
    V-->>U: HTML renderizado
```

---

## 4. Fluxo de Doação (visão de negócio)

Os estados do item ao longo do processo, controlados pela camada de domínio.

```mermaid
stateDiagram-v2
    [*] --> Pendente: Doador publica item
    Pendente --> Disponivel: Moderador aprova
    Pendente --> Recusado: Moderador recusa
    Disponivel --> Reservado: Doador aceita solicitação
    Reservado --> Doado: Doação finalizada
    Reservado --> Disponivel: Reserva liberada
    Doado --> [*]
    Recusado --> [*]
```
