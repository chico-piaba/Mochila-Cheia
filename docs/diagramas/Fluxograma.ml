graph TD
    subgraph "Início e Autenticação"
        A[Início] --> B{Usuário já possui cadastro?};
        B -- Não --> C[1. Realizar Cadastro];
        C --> D[2. Fazer Login];
        B -- Sim --> D;
    end

    subgraph "Jornada do Usuário"
        D --> E{Qual ação deseja realizar?};
    end

    subgraph "Fluxo de Doação"
        E -- Quero Doar --> F[3a. Cadastrar novo Item];
        F --> G[4a. Associar a uma Categoria];
        G --> H[5a. Publicar o Item];
        H --> I[6a. Aguardar Solicitações];
    end

    subgraph "Fluxo de Solicitação"
        E -- Quero Receber --> J[3b. Buscar Itens disponíveis];
        J --> K[4b. Selecionar Item desejado];
        K --> L[5b. Criar Solicitação];
        L --> M[6b. Sistema Notifica Doador];
        M --> N{Doador aceita a solicitação?};
        N -- Sim --> O[7b. Doador e Receptor trocam Mensagens];
        O --> P[8b. Combinar e realizar a entrega];
        N -- Não --> Q[Solicitação Recusada];
        Q --> J;
    end

    subgraph "Finalização"
        P --> R[9. Processo Finalizado];
        R --> S[Fim];
    end
