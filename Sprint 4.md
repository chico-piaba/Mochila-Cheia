## Projeto Integrado: Mochila Cheia - Semestre 2

### Sprint 1: Programação Orientada a Objetos

**Período:** 04/11/2025 a 16/12/2025
**Foco:** Aplicar os conceitos de Programação Orientada a Objetos (POO) para modelar e implementar as classes fundamentais do sistema "Mochila Cheia".

---

**Equipe:**
*   Júlio Cesar Batista da Silva
*   Leidson Oliveira Lima
*   Mikael Ramon Tavares Barbosa
*   Nathalia Campos De Castro
*   Pedro Davi Monteiro Bezerra
*   Rodrigo Lima Diôgo (Facilitador da Comunicação)

---

### 🎯 Objetivo da Sprint

O objetivo principal desta sprint é traduzir o modelo conceitual do projeto em uma estrutura de classes coesa e funcional. Ao final, teremos a base do nosso sistema pronta, com as principais entidades e seus comportamentos definidos em código.


---

### 🎁 Entregável Parcial 1 (EP1): Implementação das Classes Principais do MVP

**Data de Entrega:** 15/12/2025

**Descrição:** Desenvolver o código-fonte das classes que representam as entidades centrais da plataforma. A implementação deve incluir atributos, métodos construtores, getters/setters e os principais métodos de negócio de cada classe.

---

### ✅ Requisitos e Critérios de Avaliação do EP1

Para garantir o alinhamento com as expectativas da disciplina, o entregável deve atender aos seguintes pontos:

*   **Código no GitHub:** Todo o código-fonte das classes deve ser versionado e estar disponível em um repositório no GitHub.
*   **Documentação (`README.md`):** O `README` do repositório deve ser bem estruturado e conter:
    *   Uma explicação clara do projeto.
    *   Uma seção obrigatória intitulada **"Possíveis usos da nossa solução"** (Componente Extensionista), detalhando como o projeto poderia ser aplicado em outros contextos.
*   **Relatório Detalhado:** A equipe deve preencher o [documento de relatório do EP1](Relatorio_EP1.md) com as explicações aprofundadas sobre o processo de desenvolvimento, o uso de princípios de POO, as contribuições individuais e as evidências do trabalho em equipe.
*   **Vídeo Explicativo:** Gravar um vídeo de no máximo 5 minutos, onde toda a equipe apresenta o projeto, o funcionamento do código e as respostas do relatório.
*   **Princípios de POO:** O código deve demonstrar o uso adequado de conceitos como Encapsulamento, Abstração e Herança (quando aplicável).

---

### 📋 Planejamento e Estrutura das Classes

Abaixo está a definição das classes a serem implementadas.

#### 1. Classe `Usuario`
Representa qualquer pessoa que interage com o sistema, podendo ser um doador ou um receptor.

*   **Atributos:**
    *   `id_usuario` (int): Identificador único.
    *   `nome` (string): Nome completo.
    *   `email` (string): E-mail para login e contato.
    *   `senha` (string): Senha (deve ser armazenada de forma segura/hash).
    *   `telefone` (string): Telefone para contato.
    *   `endereco` (string): Cidade e bairro para geolocalização.
    *   `tipo_usuario` (enum): 'DOADOR' ou 'RECEPTOR'.

*   **Métodos Principais:**
    *   `cadastrar()`: Realiza o cadastro de um novo usuário.
    *   `login()`: Autentica o usuário no sistema.
    *   `atualizar_perfil()`: Permite a edição das informações do usuário.
    *   `solicitar_item(item)`: Inicia o processo de solicitação de um item.

#### 2. Classe `Item`
Representa um material escolar disponível para doação.

*   **Atributos:**
    *   `id_item` (int): Identificador único.
    *   `titulo` (string): Nome do item (ex: "Mochila Azul Usada").
    *   `descricao` (string): Detalhes sobre o item.
    *   `categoria` (string): (ex: "Mochila", "Livro", "Caderno").
    *   `estado_conservacao` (string): (ex: "Novo", "Pouco Usado", "Usado").
    *   `fotos` (list<string>): Lista de URLs ou caminhos para as imagens do item.
    *   `status` (enum): 'DISPONIVEL', 'RESERVADO', 'DOADO'.
    *   `doador` (Usuario): Objeto do tipo `Usuario` que cadastrou o item.
    *   `data_cadastro` (datetime): Data em que o item foi publicado.

*   **Métodos Principais:**
    *   `cadastrar_item()`: Adiciona um novo item para doação.
    *   `atualizar_status(novo_status)`: Altera o status do item (ex: para 'RESERVADO').
    *   `adicionar_foto(foto_url)`: Inclui uma nova foto ao item.

#### 3. Classe `Solicitacao`
Representa o processo de um usuário (receptor) solicitando um item a outro usuário (doador).

*   **Atributos:**
    *   `id_solicitacao` (int): Identificador único.
    *   `item` (Item): O item que está sendo solicitado.
    *   `solicitante` (Usuario): O usuário que está pedindo o item.
    *   `doador` (Usuario): O usuário que está doando o item.
    *   `status` (enum): 'PENDENTE', 'ACEITA', 'RECUSADA', 'FINALIZADA'.
    *   `data_solicitacao` (datetime): Data da solicitação.

*   **Métodos Principais:**
    *   `criar()`: Inicia uma nova solicitação.
    *   `aceitar()`: Doador aceita a solicitação, o que deve mudar o status do `Item` para 'RESERVADO'.
    *   `recusar()`: Doador recusa a solicitação.
    *   `finalizar()`: Confirma que a entrega foi concluída, mudando o status do `Item` para 'DOADO'.

#### 4. Classe `PontoDeColeta`
Representa um local parceiro onde doadores podem deixar itens e receptores podem retirá-los.

*   **Atributos:**
    *   `id_ponto` (int): Identificador único.
    *   `nome` (string): Nome do estabelecimento parceiro.
    *   `endereco_completo` (string): Endereço do local.
    *   `horario_funcionamento` (string): Horários para entrega e retirada.
    *   `responsavel` (string): Nome do contato no local.

*   **Métodos Principais:**
    *   `cadastrar_ponto()`: Adiciona um novo ponto de coleta ao sistema.
    *   `receber_item(item)`: Registra o recebimento de um item no local.
    *   `entregar_item(item, solicitante)`: Registra a retirada de um item.

---

### 🗓️ Cronograma e Datas Importantes

*   **04/11/2025:** Início da Sprint e Encontro Síncrono #1.
*   **04/11 a 08/12:** Período de desenvolvimento e implementação das classes.
*   **09/12/2025:** Sessão de Tutoria Coletiva #1 para tirar dúvidas.
*   **15/12/2025:** Data limite para a entrega do **Entregável Parcial 1 (EP1)**.
*   **16/12/2025:** Encontro Síncrono #2 e fechamento da Sprint.
