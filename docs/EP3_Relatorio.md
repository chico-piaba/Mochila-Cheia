**Análise e Desenvolvimento de Sistemas (ADS)**  
**Centro de Educação a Distância (CEAD)**

**PROJETO INTEGRADO II [ADS0013]**  
**Prof. Allysson Allex Araújo**  
**allysson.araujo@ufca.edu.br**

**Entregável Parcial 3 (EP3) - Relatório**

**DATA DE ENTREGA: ATÉ 09/03/2026 às 23h59**

## Identificação do Time

| Nome Completo | Matrícula | Situação |
| :--- | :--- | :--- |
| Rodrigo Lima Diôgo | [MATRÍCULA] | ✅ Ativo |
| Júlio Cesar Batista da Silva | [MATRÍCULA] | ✅ Ativo |
| Francisco Robson Paulino Cruz | [MATRÍCULA] | ✅ Ativo |
| Leidson Oliveira Lima | [MATRÍCULA] | ❌ Desistente |
| Mikael Ramon Tavares Barbosa | [MATRÍCULA] | ❌ Desistente |
| Nathalia Campos De Castro | [MATRÍCULA] | ❌ Desistente |
| Pedro Davi Monteiro Bezerra | [MATRÍCULA] | ❌ Desistente |

---

**1) Explique de forma robusta e aprofundada como a equipe compreendeu e atendeu aos requisitos do entregável. Apresente evidências (prints, gifs, etc).**

**a) Apresente o wireframe com a devida documentação associada, incluindo a justificativa sobre as decisões, adesão às boas práticas, princípios adotados, etc. Esclareça como você buscou garantir consistência, usabilidade e acessibilidade.**

**R:** O wireframe do **Mochila Cheia** foi projetado tendo como referência as **10 Heurísticas de Usabilidade de Jakob Nielsen**, garantindo que a interface seja intuitiva, eficiente e agradável para todos os perfis de usuário (doadores, receptores e moderadores).

#### 1. Visibilidade do Status do Sistema

O sistema mantém o usuário informado sobre o que está acontecendo em tempo real:

- **Badges de status nos itens:** Cada item exibe um indicador visual claro do seu estado atual (pendente, disponível, reservado, doado, recusado). As cores seguem convenções universais — verde para disponível, amarelo para pendente, azul para reservado e cinza para inativo.
- **Indicadores de progresso na doação:** O fluxo de doação (Cadastro → Moderação → Disponível → Solicitado → Reservado → Doado) é representado por uma barra de progresso ou indicador de etapas, permitindo que o doador acompanhe em que ponto cada item se encontra.
- **Contadores no dashboard:** A tela inicial do doador exibe cards com números atualizados: "3 itens ativos", "2 solicitações pendentes", "5 doações concluídas".
- **Indicador de mensagens não lidas:** O ícone de mensagens na barra de navegação exibe um badge numérico com a quantidade de conversas não lidas.

#### 2. Correspondência entre o Sistema e o Mundo Real

A interface utiliza linguagem e conceitos familiares ao público-alvo:

- **Vocabulário acessível:** Em vez de termos técnicos como "instância" ou "entidade", usamos "item", "solicitação", "doação" — palavras do cotidiano.
- **Ícones intuitivos:** Ícones representam ações reconhecíveis — lupa para busca, envelope para mensagens, sino para notificações, câmera para foto do item.
- **Fluxo natural:** A sequência de ações segue a lógica do mundo real: primeiro o doador cadastra o item, depois o moderador revisa, então o receptor busca e solicita, e finalmente ambos combinam a entrega.
- **Categorias familiares:** As categorias de materiais (Mochilas, Livros, Cadernos, Material de Escrita, Uniformes) refletem o vocabulário real de materiais escolares.

#### 3. Controle e Liberdade do Usuário

O wireframe garante que o usuário nunca fique "preso" em uma ação:

- **Botão "Voltar" em todas as telas:** Navegação hierárquica clara com seta de retorno no cabeçalho.
- **Cancelamento de ações:** O receptor pode cancelar uma solicitação pendente; o doador pode recusar uma solicitação e devolver o item ao estado "disponível".
- **Edição de dados:** O doador pode editar as informações de um item antes da moderação; todos os usuários podem editar seus dados de perfil.
- **Confirmação antes de ações irreversíveis:** Ao finalizar uma doação ou recusar um item, o sistema exibe um diálogo de confirmação ("Tem certeza?").

#### 4. Consistência e Padrões

A interface segue padrões visuais e de interação uniformes:

- **Navegação por barra inferior (bottom tab bar):** Padrão consolidado em aplicativos mobile, com ícones e rótulos para cada seção principal. O número de abas respeita o limite recomendado (4-5 itens).
- **Cards de item padronizados:** Todos os itens são exibidos no mesmo formato de card — foto à esquerda, título e categoria no centro, badge de status à direita — tanto na busca quanto em "Meus Itens".
- **Botões com estilo consistente:** Botões primários (ação principal) em cor de destaque; botões secundários (cancelar, voltar) em estilo outline; botões destrutivos (recusar, excluir) em vermelho.
- **Tipografia hierárquica:** Títulos, subtítulos e corpo de texto seguem uma escala tipográfica consistente em todas as telas.

#### 5. Prevenção de Erros

O design previne problemas antes que ocorram:

- **Validação em tempo real nos formulários:** Campos obrigatórios são marcados com asterisco; o e-mail é validado no formato enquanto o usuário digita; a senha exige mínimo de caracteres com indicador de força.
- **Seleção em vez de digitação:** Campos como "Categoria" e "Estado de Conservação" usam dropdowns ou chips selecionáveis, eliminando erros de digitação.
- **Constraint visual de solicitação única:** Se o receptor já solicitou um item, o botão "Solicitar" é substituído por "Já solicitado" (desabilitado), refletindo a constraint `UNIQUE(fk_id_item, fk_id_receptor)` do banco.
- **Impedimento de auto-mensagem:** O sistema não exibe a opção de chat consigo mesmo, alinhado à constraint `CHECK(fk_id_remetente != fk_id_destinatario)`.

#### 6. Reconhecimento em vez de Memorização

A interface reduz a carga de memória do usuário:

- **Filtros sempre visíveis:** Na tela de busca, os filtros de categoria ficam expostos como chips horizontais no topo, sem necessidade de abrir menus ocultos.
- **Categorias com ícones:** Cada categoria possui um ícone associado (mochila, livro, lápis), facilitando o reconhecimento visual rápido.
- **Histórico de solicitações:** A tela "Minhas Solicitações" exibe todo o histórico com status, eliminando a necessidade de o receptor lembrar o que já solicitou.
- **Informações contextuais:** No chat, o cabeçalho exibe o nome do item relacionado à conversa, evitando que o usuário precise lembrar de qual doação se trata.

#### 7. Flexibilidade e Eficiência de Uso

A interface atende tanto usuários iniciantes quanto experientes:

- **Busca como tela principal do receptor:** A ação mais frequente (buscar itens) é a primeira tela após o login, reduzindo cliques.
- **Acesso rápido a "Cadastrar Item":** Disponível diretamente na barra de navegação do doador, sem necessidade de menus intermediários.
- **Notificações acionáveis:** Cada notificação contém um link direto para o contexto (item aprovado, nova solicitação), eliminando navegação manual.
- **Filtros combinados:** O receptor pode combinar filtros de categoria, localização e estado de conservação em uma única busca.

#### 8. Design Estético e Minimalista

A interface prioriza o essencial:

- **Informação progressiva:** O card de item na busca mostra apenas título, categoria, estado e foto. Os detalhes completos (descrição, doador, ponto de coleta) ficam na tela de detalhes.
- **Espaçamento generoso:** Uso de whitespace para separar seções e evitar poluição visual.
- **Paleta de cores reduzida:** Cor primária para ações, cor secundária para destaques, tons neutros para fundo e texto — sem excesso de cores competindo pela atenção.
- **Tipografia limpa:** Fonte sans-serif em toda a interface, com apenas 3 tamanhos de peso (regular, medium, bold).

#### 9. Ajudar os Usuários a Reconhecer, Diagnosticar e Recuperar-se de Erros

O sistema comunica erros de forma clara e construtiva:

- **Mensagens de erro em linguagem simples:** Em vez de "Erro 400 — Bad Request", o sistema exibe "O e-mail informado já está cadastrado. Tente fazer login ou use outro e-mail."
- **Campos com erro destacados:** Inputs com erro recebem borda vermelha e uma mensagem explicativa abaixo.
- **Ações de recuperação:** Telas de estado vazio ("Nenhum item encontrado") incluem sugestões: "Tente buscar por outra categoria" ou "Amplie a área de busca".
- **Tela offline:** Quando não há conexão, o app exibe uma mensagem amigável com botão "Tentar novamente".

#### 10. Ajuda e Documentação

O wireframe prevê suporte ao usuário:

- **Onboarding para novos usuários:** Sequência de 3 telas introdutórias na primeira utilização, explicando os fluxos de doação e recebimento.
- **Tooltips contextuais:** Ícones de "?" ao lado de campos como "Estado de Conservação" exibem uma explicação breve ao serem tocados.
- **Seção de FAQ:** Acessível a partir do perfil, com respostas às dúvidas mais comuns.

**Acessibilidade — Diretrizes WCAG 2.1**

O wireframe também foi projetado seguindo as diretrizes da **WCAG 2.1** (Web Content Accessibility Guidelines) do W3C, organizadas nos quatro princípios fundamentais: Perceptível, Operável, Compreensível e Robusto (POUR).

**Princípio 1 — Perceptível**

- **Contraste de cores (WCAG 1.4.3 — Nível AA):** Razão de contraste mínima de 4.5:1 entre texto e fundo para texto normal e 3:1 para texto grande. Badges de status utilizam não apenas cor, mas rótulos textuais ("Disponível", "Pendente"), garantindo que usuários com daltonismo identifiquem o estado.
- **Texto alternativo (WCAG 1.1.1 — Nível A):** Fotos de itens possuem `alt` descritivo; ícones decorativos são `aria-hidden="true"`; ícones funcionais possuem `aria-label`.
- **Conteúdo adaptável (WCAG 1.3.1 — Nível A):** Hierarquia de títulos sequencial (h1 → h2 → h3); formulários com `<label>` associados via `for/id`; listas com marcação semântica.

**Princípio 2 — Operável**

- **Navegação por teclado (WCAG 2.1.1 — Nível A):** Todos os elementos interativos acessíveis via Tab; ordem de tabulação segue a ordem visual; indicadores de foco visíveis (contorno de 2px na cor primária).
- **Tamanho de alvos de toque (WCAG 2.5.5 — Nível AAA):** Dimensão mínima de 48x48dp; espaçamento entre alvos adjacentes de no mínimo 8dp.
- **Tempo suficiente (WCAG 2.2.1 — Nível A):** Notificações toast permanecem visíveis por pelo menos 5 segundos e podem ser descartadas manualmente.

**Princípio 3 — Compreensível**

- **Linguagem clara (WCAG 3.1.1 — Nível A):** Atributo `lang="pt-BR"` definido; linguagem simples e direta, adequada ao público-alvo.
- **Prevenção de erros em formulários (WCAG 3.3.1 e 3.3.3 — Nível A/AA):** Campos obrigatórios com `aria-required="true"`; mensagens de erro via `aria-describedby`; tela de revisão antes de ações críticas.
- **Navegação previsível (WCAG 3.2.3 — Nível AA):** Barra de navegação inferior consistente; botão "Voltar" previsível; alterações de contexto apenas por ação explícita.

**Princípio 4 — Robusto**

- **Compatibilidade com tecnologias assistivas (WCAG 4.1.2 — Nível A):** Componentes com `role`, `name` e `value` adequados; `autocomplete` em formulários; `aria-live` regions para mudanças de estado.
- **HTML semântico:** Estrutura com `<header>`, `<nav>`, `<main>`, `<footer>`; botões como `<button>`, links como `<a>`.

| Critério | Nível | Aplicação no Wireframe |
| :--- | :--- | :--- |
| 1.1.1 Texto alternativo | A | Alt em fotos de itens, aria-label em ícones |
| 1.3.1 Informação e relações | A | Hierarquia de títulos, labels em formulários |
| 1.4.3 Contraste mínimo | AA | Ratio 4.5:1 texto/fundo |
| 1.4.11 Contraste não textual | AA | Ícones e bordas com contraste 3:1 |
| 2.1.1 Teclado | A | Tab navega todos os elementos interativos |
| 2.4.3 Ordem de foco | A | Tabulação segue ordem visual |
| 2.4.6 Cabeçalhos e rótulos | AA | Títulos descritivos em cada seção |
| 2.5.5 Tamanho do alvo | AAA | Mínimo 48x48dp em alvos de toque |
| 3.1.1 Idioma da página | A | lang="pt-BR" definido |
| 3.2.3 Navegação consistente | AA | Bottom tab bar fixa por perfil |
| 3.3.1 Identificação de erro | A | Mensagens de erro por campo |
| 3.3.2 Rótulos ou instruções | A | Labels associados a todos os inputs |
| 4.1.2 Nome, função, valor | A | Roles e aria adequados em componentes |

---

**b) Apresente o sitemap com a devida documentação associada, incluindo a justificativa sobre as decisões, adesão às boas práticas, princípios adotados, etc.**

**R:** O sitemap completo está documentado em `docs/EP3_Sitemap.md` e contempla **22 telas** organizadas em **3 fluxos** distintos (Doador, Receptor e Moderador), com diagrama Mermaid de navegação completa, tabela de navegação global (bottom tab bar) e relação Sitemap × Banco de Dados.

---

*c) [Componente Extensionista] Atualizar README de forma explicativa com orientações sobre como prototipar um wireframe. Discuta, com suas palavras, sobre como design centrado no usuário ajuda a melhorar a qualidade de sistemas usados pelas pessoas no dia a dia. Objetivo: promover uma consciência sobre o impacto da interface humano-computador na sociedade.*

**R:** O Design Centrado no Usuário (UCD - *User-Centered Design*) é uma abordagem que inverte a lógica tradicional do desenvolvimento de software. Em vez de criar um sistema baseado no que é mais fácil para o programador codificar, o UCD foca nas necessidades, limitações e contextos reais das pessoas que utilizarão a ferramenta, focado não somente em linhas de códigos mas sim em um objetivo factual, final.

No dia-a-dia, essa abordagem melhora drasticamente a qualidade de vida da sociedade. Sistemas com boa Interface Humano-Computador (IHC) reduzem a carga cognitiva, evitam frustrações e economizam tempo, muitas vezes o simples é o mais sofisticado. Quando uma pessoa consegue pagar uma conta no aplicativo do banco em segundos, ou um idoso consegue agendar uma consulta médica pelo celular sem pedir ajuda, estamos vendo o impacto de uma IHC bem planejada. O bom design torna a tecnologia "invisível", permitindo que o usuário foque no seu objetivo final, e não na ferramenta em si.

No contexto do nosso projeto, o **Mochila Cheia**, o Design Centrado no Usuário não é apenas uma questão de estética, mas de **inclusão social e empatia**. Nossos usuários (os "Receptores") muitas vezes são famílias de baixa renda, que podem acessar a plataforma através de celulares mais antigos (notadamente Android), com conexões de internet limitadas e níveis variados de letramento digital. Se a nossa interface for confusa, pesada ou usar jargões técnicos, nós criaremos uma barreira tecnológica que impedirá a doação de chegar a quem precisa. Ou seja, a plataforma deixa de ser facilitadora por falta de empatia com a realidade do público alvo.

Por outro lado, para o "Doador", a interface precisa ser ágil e recompensadora. Se o processo de cadastrar um material escolar exigir muitos cliques ou formulários complexos, a pessoa pode desistir no meio do caminho.

Portanto, desenvolver **wireframes** e pensar na **usabilidade e acessibilidade** é garantir que a tecnologia atue como uma ponte (facilitador), e não como um muro. A IHC deixa de ser apenas uma disciplina técnica para se tornar uma ferramenta fundamental de democratização do acesso a serviços, informação e oportunidades na sociedade digital.

---

**2) Insira abaixo link do vídeo explicativo no Google Drive (lembre-se de deixar o acesso aberto) abaixo o link do vídeo apresentando explicando a questão 1. Todos os membros do time devem contribuir e agregar com explicações no vídeo. O vídeo deve ter no máximo 5 minutos. Lembre-se de demonstrar o wireframe e o sitemap funcionando, a documentação associada e apresentar evidências sobre os critérios e requisitos solicitados.**

**R:** [INSERIR LINK DO VÍDEO APÓS GRAVAÇÃO]

---

**3) Link do repositório no GitHub ([exemplo](https://github.com/avjinder/Minimal-Todo) de referência).**

**R:** https://github.com/chico-piaba/Mochila-Cheia.git

**Arquivos relevantes para EP3:**

```
docs/
├── EP3_Relatorio.md       ← Este relatório
├── EP3_Sitemap.md         ← Sitemap com fluxo de navegação
├── EP3_Roteiro_Video.md   ← Roteiro do vídeo
└── EP3_Prompt_Wireframe.md ← Prompts do wireframe
```

---

**4) Detalhe como cada membro da equipe contribuiu para o desenvolvimento do entregável?**

**R:**

* **Rodrigo Lima Diôgo:** Elaboração do Sitemap completo; redação das justificativas de usabilidade (1a) e acessibilidade; organização do repositório GitHub; roteiro e edição do vídeo.
* **Júlio Cesar Batista da Silva:** Desenvolvimento do wireframe funcional; geração de evidências visuais (GIFs e prints); demonstração prática das telas no vídeo.
* **Francisco Robson Paulino Cruz:** Guia do README sobre wireframes; artigo reflexivo sobre Design Centrado no Usuário (1c); gestão de evidências e registros de reuniões.

Os mesmos 4 membros que desistiram nos EPs anteriores permaneceram ausentes: Leidson, Mikael, Nathalia e Pedro Davi.

---

**5) Insira abaixo evidências das contribuições coletivas (fotos de reuniões, etc) e individuais (que demonstrem o que cada membro fez).**

**R:**

**Sitemap (docs/EP3_Sitemap.md):**
- 22 telas mapeadas
- 3 fluxos detalhados (Doador, Receptor, Moderador)
- Diagrama Mermaid com navegação completa
- Tabela de navegação global (bottom tab bar)
- Relação Sitemap × Banco de Dados

**Wireframe:**
- [INSERIR NÚMERO] telas prototipadas
- [INSERIR FERRAMENTA UTILIZADA — ex.: Figma, Balsamiq]
- [INSERIR LINK DO PROTÓTIPO]

**Repositório GitHub:**
- Estrutura reorganizada (diagramas em `docs/diagramas/`)
- `.gitignore` atualizado
- README atualizado com seção EP3

**Evidências de reuniões:**
- [INSERIR PRINTS/FOTOS DE REUNIÕES]

---

**6) Após enviar o presente relatório no AVA, cada membro deve responder ao [formulário de autoavaliação do time](https://forms.gle/mvCiEaW11LgpUHjf9). Tal formulário deverá ser respondido somente após a conclusão da sprint.**
