# Mochila Cheia — Plataforma Web de Doação de Material Escolar

**UNIVERSIDADE FEDERAL DO CARIRI (UFCA)**
Centro de Educação a Distância (CEAD) — Análise e Desenvolvimento de Sistemas (ADS)

**Disciplina:** [ADS 0015] Desenvolvimento para Web
**Professor:** Prof. Jayr Alencar Pereira
**Atividade:** [PF1] — Definição do Tema do Projeto
**Vencimento:** segunda-feira, 29 de junho de 2026, 23:59

---

## 1. Nome do Projeto

**Mochila Cheia** — Plataforma Web de Doação de Material Escolar.

O projeto dá continuidade, no ambiente Web, à solução desenvolvida pela equipe na disciplina de **Projeto Integrado III**, transformando o protótipo de alta fidelidade e o backend orientado a objetos já existentes em um site funcional e navegável.

## 2. Integrantes da Equipe

| Nome | Matrícula |
|------|-----------|
| Rodrigo Lima Diôgo | 2025014780 |
| Júlio César Batista da Silva | 2025014645 |
| Francisco Robson Paulino Cruz | 2025014458 |
| Maria da Conceição Freitas Lopes | 2023011420 |
| Lucas do Nascimento Souza | 2023011395 |

A equipe é, preferencialmente, a mesma formada em Projeto Integrado III, mantendo o mesmo projeto como base, conforme orientado na atividade.

## 3. Objetivo do Projeto

Desenvolver uma aplicação Web que conecte, de forma simples, segura e confiável, **pessoas que possuem materiais escolares para doar** a **estudantes e famílias que necessitam desses itens**. O sistema utiliza **pontos de coleta parceiros** como apoio logístico, reduzindo barreiras de contato direto e transmitindo confiança a todo o processo de doação.

Como objetivo específico desta disciplina, busca-se materializar na Web a interface projetada em Projeto Integrado III: traduzir os wireframes e o protótipo do Figma em páginas reais (HTML/CSS/JS), integradas à lógica de domínio e ao banco de dados já modelados, entregando uma experiência de uso acessível e intuitiva.

## 4. Justificativa

O custo dos materiais escolares é um obstáculo concreto para grande parte das famílias brasileiras:

- **85% das famílias** têm o orçamento impactado pelos gastos com material escolar; em favelas, esse número chega a **89%**.
- A falta de recursos básicos contribui diretamente para a **evasão escolar**.
- Ao mesmo tempo, uma grande quantidade de **materiais em bom estado é descartada** desnecessariamente todos os anos.

Existe, portanto, um descompasso entre quem tem itens ociosos e quem precisa deles. Uma plataforma Web é o meio mais adequado para resolver esse problema em escala: é acessível a partir de qualquer dispositivo com navegador, dispensa instalação, permite atualização imediata de conteúdo e centraliza a comunicação entre as partes. Justifica-se assim a construção de uma interface Web acessível e responsiva, que dê forma utilizável à solução concebida no Projeto Integrado III e amplie seu alcance social.

## 5. Motivações para a Escolha do Tema

- **Impacto social real:** o tema enfrenta um problema concreto e mensurável (custo do material escolar e evasão), com potencial de beneficiar famílias em situação de vulnerabilidade.
- **Sustentabilidade e economia circular:** ao dar nova utilidade a materiais que seriam descartados, o projeto combate o desperdício e fortalece redes de solidariedade.
- **Continuidade e aproveitamento de trabalho prévio:** a equipe já produziu, no Projeto Integrado III, o modelo de domínio (classes em Python), o projeto físico do banco de dados, os wireframes e o protótipo de alta fidelidade no Figma. A disciplina de Web é a oportunidade natural de transformar esse projeto em um produto funcional.
- **Aprendizado técnico aplicado:** o tema permite exercitar, com propósito, todo o conteúdo da disciplina — estruturação de páginas, estilização, interatividade, formulários, autenticação e integração com banco de dados.

## 6. Público-Alvo

A plataforma atende a três perfis principais de usuário, além de um perfil de apoio:

- **Doadores:** pessoas físicas (ou instituições) que possuem materiais escolares em bom estado e desejam doá-los.
- **Receptores:** estudantes e famílias de baixa renda que buscam materiais escolares.
- **Moderadores:** responsáveis por revisar e aprovar os itens publicados, garantindo a qualidade e a segurança da plataforma.
- **Pontos de Coleta (parceiros):** locais (escolas, comércios, ONGs) que facilitam a logística de entrega e retirada dos itens.

Um cuidado central de projeto é a **acessibilidade**: como parte do público pode ter baixo letramento digital, a interface prioriza linguagem clara, alto contraste e navegação intuitiva, para que a doação ou a solicitação possa ser concluída sem barreiras tecnológicas.

## 7. Visão Geral do Sistema Web

O **Mochila Cheia** será um site responsivo que funciona como a camada de interação direta com os usuários, conectando-se ao trabalho desenvolvido em Projeto Integrado III. A relação entre as disciplinas se dá da seguinte forma:

- **Apresentação (foco desta disciplina):** páginas em **HTML, CSS e JavaScript**, construídas a partir dos wireframes e do protótipo do Figma já validados em Projeto Integrado III.
- **Lógica de negócio:** servida por uma aplicação **Python/Flask**, reaproveitando as classes de domínio já implementadas (`Usuario`, `Item`, `Solicitacao`, `PontoDeColeta`, `Categoria`, `Mensagem`).
- **Persistência:** banco de dados **SQLite** (com possibilidade de PostgreSQL em produção), a partir do projeto físico já modelado.

Dessa forma, o site não apenas **apresenta o projeto**, mas oferece a **funcionalidade central** da proposta: permite cadastrar-se, publicar itens, buscar materiais, solicitar doações e conversar com a outra parte. A interface Web é o elo que torna a solução do Projeto Integrado III utilizável pelo público real, dando rosto e usabilidade a toda a estrutura técnica construída anteriormente.

A navegação será organizada por perfil de usuário, com fluxos distintos para doadores, receptores e moderadores, seguindo princípios de usabilidade (Heurísticas de Nielsen) e de acessibilidade (WCAG 2.1) já adotados no protótipo.

## 8. Descrição Inicial das Principais Páginas e Funcionalidades

A seguir, as páginas e funcionalidades previstas para o desenvolvimento ao longo da disciplina. O conjunto poderá ser refinado nas próximas etapas do projeto.

| Página / Seção | Funcionalidade prevista |
|----------------|-------------------------|
| **Página Inicial / Apresentação** | Apresenta a proposta do Mochila Cheia, dados do problema e chamadas de ação ("Quero doar" / "Quero receber"). |
| **Cadastro e Login** | Criação de conta para os perfis de doador e receptor, com autenticação segura (senha com hash) e validação de formulários. |
| **Busca de Itens** | Lista de materiais disponíveis com filtros por categoria, localização e disponibilidade. Página principal do receptor. |
| **Detalhes do Item** | Exibe foto, descrição, estado de conservação e ponto de coleta; permite solicitar o item. |
| **Publicar Item** | Formulário para o doador cadastrar um material (foto, descrição, categoria, estado). |
| **Meus Itens / Minhas Solicitações** | Painéis para acompanhar o status das doações e solicitações (badges de status: pendente, disponível, reservado, doado). |
| **Mensagens (Chat)** | Comunicação entre doador e receptor para combinar a entrega. |
| **Pontos de Coleta** | Lista de locais parceiros com endereço e horário de funcionamento. |
| **Painel de Moderação** | Fila de itens aguardando aprovação, com revisão e liberação pelo moderador. |
| **Notificações** | Alertas sobre solicitações recebidas e atualizações de status. |

### Funcionalidades transversais

- **Design responsivo**, adequado a celulares e computadores.
- **Acessibilidade** (contraste adequado, textos alternativos, hierarquia de títulos, alvos de toque confortáveis).
- **Validação imediata de formulários**, prevenindo erros do usuário.
- **Feedback visual claro** por meio de badges e mensagens de confirmação.

---

> **Síntese:** a interface Web do Mochila Cheia dará continuidade direta ao Projeto Integrado III, transformando o protótipo e o backend já existentes em um sistema funcional, acessível e de impacto social, contribuindo simultaneamente para as duas disciplinas.
