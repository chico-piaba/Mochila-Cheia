# Sprint 3: Modelagem de Dados e Casos de Uso

## 1. Capa e Identificação

- **Curso:** Análise e Desenvolvimento de Sistemas
- **Polo:** Maracanaú
- **Projeto:** Mochila Cheia
- **Disciplina:** Projeto Integrado I – Sprint 3
- **Professor:** Luís Fabrício de Freitas Souza
- **Equipe:**
    - Júlio Cesar Batista da Silva
    - Leidson Oliveira Lima
    - Mikael Ramon Tavares Barbosa
    - Nathalia Campos De Castro
    - Pedro Davi Monteiro Bezerra
    - Rodrigo Lima Diôgo

---

## 2. Resumo da Solução

O projeto "Mochila Cheia" desenvolve uma plataforma web para conectar de forma eficiente e segura doadores de materiais escolares a receptores (estudantes e famílias de baixa renda). As funcionalidades centrais incluem cadastro e moderação de itens, busca geolocalizada, um sistema de solicitação e fila de espera, e um chat para comunicação. A solução visa combater o desperdício, promover a economia circular e reduzir a desigualdade no acesso a recursos educacionais, gerando impacto social e ambiental positivo.

---

## 3. Diagrama de Caso de Uso (UML)

**Atores Identificados:**

- **Usuário:** Ator genérico que pode se cadastrar e navegar.
- **Doador:** Especialização do Usuário que cadastra e gerencia itens para doação.
- **Receptor:** Especialização do Usuário que busca e solicita itens.
- **Moderador:** Usuário com permissões especiais para aprovar ou rejeitar itens cadastrados, garantindo a qualidade e segurança da plataforma.

```mermaid
[COLE O CÓDIGO DO DIAGRAMA DE CASO DE USO AQUI]
```

### Mini-Catálogo de Casos de Uso

1.  **Gerenciar Cadastro:**
    -   **Objetivo:** Permitir que um usuário crie ou atualize suas informações de perfil.
    -   **Pré-condições:** Nenhuma para criar. Para atualizar, o usuário deve estar autenticado.
    -   **Fluxo Básico:** O usuário preenche o formulário com seus dados (nome, e-mail, senha, localização) e salva as informações.
    -   **Resultado Esperado:** A conta do usuário é criada ou atualizada no sistema.

2.  **Cadastrar Item:**
    -   **Objetivo:** Permitir que um Doador anuncie um item para doação.
    -   **Pré-condições:** O usuário deve estar autenticado com o perfil de Doador.
    -   **Fluxo Básico:** O doador preenche um formulário com detalhes do item (título, descrição, categoria, estado, fotos) e confirma a publicação.
    -   **Resultado Esperado:** O item é submetido para a fila de moderação.

3.  **Buscar Itens:**
    -   **Objetivo:** Permitir que qualquer usuário (logado ou não) encontre itens disponíveis.
    -   **Pré-condições:** Nenhuma.
    -   **Fluxo Básico:** O usuário acessa a página de busca, aplica filtros (categoria, localização) e visualiza a lista de itens correspondentes.
    -   **Resultado Esperado:** O sistema exibe os itens que atendem aos critérios de busca.

4.  **Solicitar Item:**
    -   **Objetivo:** Permitir que um Receptor demonstre interesse em receber um item.
    -   **Pré-condições:** O usuário deve estar autenticado como Receptor e o item deve estar com status "Disponível".
    -   **Fluxo Básico:** O receptor clica no botão "Solicitar", confirma sua intenção e entra na fila de espera do item.
    -   **Resultado Esperado:** Uma solicitação é criada, e o Doador é notificado.

5.  **Responder Solicitação:**
    -   **Objetivo:** Permitir que um Doador aceite ou recuse uma solicitação de doação.
    -   **Pré-condições:** O Doador deve ter recebido ao menos uma solicitação para um de seus itens.
    -   **Fluxo Básico:** O Doador visualiza a lista de solicitações, seleciona um receptor e escolhe "Aceitar" ou "Recusar".
    -   **Resultado Esperado:** O status da solicitação é atualizado e o Receptor é notificado da decisão.

6.  **Moderar Itens:**
    -   **Objetivo:** Garantir que os itens cadastrados sigam as regras da plataforma.
    -   **Pré-condições:** O usuário deve estar autenticado como Moderador.
    -   **Fluxo Básico:** O moderador visualiza a fila de itens pendentes, analisa as informações e fotos, e aprova ou reprova o cadastro.
    -   **Resultado Esperado:** O status do item é atualizado para "Disponível" (se aprovado) ou "Recusado".

---

## 4. Diagrama Entidade–Relacionamento (DER)

```mermaid
[COLE O CÓDIGO DO DIAGRAMA ENTIDADE-RELACIONAMENTO AQUI]
```

### Observações sobre Regras de Negócio

-   **Usuário e Documento:** Cada `USUARIO` deve ter um e apenas um `DOCUMENTO` associado para garantir a unicidade.
-   **Item:** Um `ITEM` deve obrigatoriamente pertencer a um `USUARIO` (doador) e a uma `CATEGORIA`. Seu status muda conforme as interações (ex: "Disponível" -> "Solicitado" -> "Doado").
-   **Solicitação:** Uma `SOLICITACAO` só pode ser criada por um `USUARIO` (receptor) para um `ITEM` existente e disponível. Ela conecta um receptor a um item específico.
-   **Mensagem:** As `MENSAGENS` são sempre vinculadas a uma `SOLICITACAO` existente, garantindo que a comunicação ocorra apenas dentro do contexto de uma negociação.
-   **Moderação:** A entidade `ITEM` possui um atributo `status` que será controlado pelo `Moderador`. Itens novos entram com status "Pendente de Moderação".
