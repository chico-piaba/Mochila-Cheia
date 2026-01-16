graph TD
    subgraph "1. Entidades Fundamentais (Dados mestres)"
        A(Início da Criação de Dados) --> B["DOCUMENTO<br>(CPF ou CNPJ)"];
        A --> C["CATEGORIA<br>- ID_CATEGORIA (PK)<br>- NOME<br>- DESCRICAO"];
        B --> D["USUÁRIO<br>- ID_USUARIO (PK)<br>- FK_ID_DOCUMENTO (FK)<br>- NOME<br>- EMAIL<br>- SENHA<br>- TIPO_PERFIL"];
    end

    subgraph "2. Entidade de Conteúdo (O que é ofertado)"
        D --"É o Doador"--> E;
        C --"Define o Tipo"--> E["ITEM<br>- ID_ITEM (PK)<br>- FK_ID_DOADOR (FK)<br>- FK_ID_CATEGORIA (FK)<br>- TITULO<br>- DESCRICAO<br>- STATUS"];
    end

    subgraph "3. Entidades de Transação (Ações e interações)"
        D --"É o Receptor"--> F;
        E --"É o Objeto"--> F["SOLICITAÇÃO<br>- ID_SOLICITACAO (PK)<br>- FK_ID_RECEPTOR (FK)<br>- FK_ID_ITEM (FK)<br>- STATUS<br>- ORDEM_FILA"];
    end

    subgraph "4. Entidades de Comunicação (Eventos do sistema)"
        F --"Origina a Conversa"--> G["MENSAGEM<br>- ID_MENSAGEM (PK)<br>- FK_ID_REMETENTE (FK)<br>- FK_ID_DESTINATARIO (FK)<br>- FK_ID_SOLICITACAO (FK)<br>- CONTEUDO"];
        D --"Envia/Recebe"--> G;
        
        D --"Recebe o Alerta"--> H["NOTIFICAÇÃO<br>- ID_NOTIFICACAO (PK)<br>- FK_ID_USUARIO_DESTINO (FK)<br>- FK_ID_SOLICITACAO (FK, Opcional)<br>- FK_ID_ITEM (FK, Opcional)<br>- MENSAGEM<br>- STATUS"];
        F --"Dispara Alerta Sobre (Opcional)"--> H;
        E --"Dispara Alerta Sobre (Opcional)"--> H;
    end

    G --> Z(Fim do Fluxo de Dados);
    H --> Z;