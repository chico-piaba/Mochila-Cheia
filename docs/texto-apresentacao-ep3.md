# Texto da Apresentação em Vídeo — EP3 (MVP Web Funcional)

**Duração alvo:** 4min30s (dentro do intervalo de 3 a 5 minutos)
**Formato:** demonstração da aplicação rodando ao vivo, com cada
integrante narrando um bloco. Pode gravar com todos juntos ou cada um
gravar sua parte compartilhando a tela.

## Antes de gravar (checklist rápido)

```bash
cd "Mochila Cheia - Projeto Integrado"
.venv/bin/flask --app run init-db          # banco limpo com dados de exemplo
.venv/bin/flask --app run run --port 5001 --debug
```

Abra `http://127.0.0.1:5001` no navegador em janela estreita (modo
responsivo do Chrome, iPhone 12/390px) — o design é mobile-first e fica
mais bonito assim.

Logins da demonstração (senha de todos: `senha123`):
- Doadora: `maria.silva@email.com`
- Moderador: `admin@mochilacheia.com`
- Receptor: `joao.pedro@email.com`

---

## BLOCO 1 — Abertura e contexto (Rodrigo, ~40s)

*[NA TELA: tela inicial da aplicação com a vitrine de itens]*

> Olá! Somos a equipe do projeto Mochila Cheia, do Projeto Integrado III
> do curso de Análise e Desenvolvimento de Sistemas da UFCA. Eu sou o
> Rodrigo, e junto comigo estão Júlio, Robson, Maria, Gabriela e Lucas.
>
> O Mochila Cheia é uma plataforma web que conecta doadores de material
> escolar a estudantes que precisam desses itens. O problema que
> atacamos é real: o gasto com material escolar impacta o orçamento de
> 85% das famílias brasileiras, enquanto materiais em bom estado são
> descartados todos os dias. Nosso público-alvo são famílias de baixa
> renda, doadores e instituições parceiras que funcionam como pontos de
> coleta.
>
> Agora vamos mostrar o MVP funcionando de ponta a ponta.

## BLOCO 2 — Vitrine e navegação (Rodrigo, ~45s)

> **Nota:** blocos 1 e 2 já gravados pelo Rodrigo (ver
> `docs/gravacao-blocos-1-2.md`). Faltam os blocos 3 a 7.

*[NA TELA: navegar pela home, rolar a lista, filtrar por categoria,
abrir o detalhe de um item]*

> Esta é a tela inicial, a vitrine. Qualquer visitante, mesmo sem
> cadastro, vê os itens disponíveis com foto, categoria, estado de
> conservação e localização — uma decisão de UX para reduzir barreiras
> de entrada.
>
> A interface foi desenhada mobile-first, pensando em quem acessa pelo
> celular, com navegação fixa na parte de baixo da tela: Home,
> Solicitações, Pontos de Coleta, Mensagens e Perfil. Aplicamos
> heurísticas de acessibilidade: alvos de toque grandes, contraste
> adequado e textos alternativos nas imagens.
>
> Abrindo um item, vemos a foto, a descrição, o doador e o botão de
> solicitar.

## BLOCO 3 — Fluxo do doador e moderação (Gabriela, ~50s)

*[NA TELA: login como Maria → Publicar item (preencher formulário e
anexar foto) → "Meus Itens" mostrando status Pendente → logout → login
como admin → fila de moderação → revisar → Aprovar]*

> Agora o fluxo de quem doa. A Maria faz login e publica um item:
> título, categoria, estado de conservação, descrição e a foto, que é
> enviada por upload com validação de tipo de arquivo no servidor.
>
> Reparem que o item entra como "Pendente" e ainda não aparece na
> vitrine. Essa foi uma decisão técnica importante da equipe: todo item
> passa por moderação antes de ser publicado, garantindo a segurança e
> a confiabilidade da plataforma.
>
> Entrando como moderador, o item aparece na fila de revisão, com todos
> os dados e a foto enviada. Ao aprovar... pronto: o item já está
> visível na vitrine para qualquer pessoa.

## BLOCO 4 — Fluxo do receptor, chat e notificações (Lucas, ~50s)

*[NA TELA: login como João → abrir o item aprovado → Solicitar Item →
Minhas Solicitações → Mensagens (enviar uma mensagem no chat) → logout
→ login como Maria → Notificações → Solicitações Recebidas → Aceitar]*

> Do lado de quem precisa: o João encontra o item na vitrine e faz a
> solicitação com um toque. Ela fica registrada em "Minhas
> Solicitações", com o status acompanhado em tempo real.
>
> A combinação da entrega acontece pelo chat interno da plataforma —
> doador e receptor conversam sem expor telefone ou endereço, outra
> decisão da equipe pensada na privacidade de famílias em situação de
> vulnerabilidade.
>
> A doadora recebe uma notificação da nova solicitação e pode aceitar
> na tela de Solicitações Recebidas. A entrega pode ser combinada em um
> dos pontos de coleta parceiros, como escolas e bibliotecas, que têm
> tela própria com endereço, horário e contato.

## BLOCO 5 — Arquitetura e tecnologias (Júlio, ~50s)

*[NA TELA: VS Code ou GitHub mostrando a árvore de pastas src/web/
(blueprints, repositories, templates, static) e o database/schema.sql]*

> Sobre a arquitetura: a aplicação é feita em Python com Flask,
> organizada no padrão MVC com app factory. As rotas ficam em oito
> blueprints — autenticação, home, itens, solicitações, moderação,
> mensagens, notificações e pontos de coleta — cada um cuidando de um
> domínio do sistema.
>
> O acesso a dados fica isolado numa camada de repositórios: os
> controllers não escrevem SQL, só chamam métodos como "listar
> pendentes" ou "buscar detalhe". O banco é SQLite, criado por scripts
> de schema e seed versionados no repositório — escolhemos SQLite pela
> simplicidade de configuração no MVP, com caminho aberto para
> PostgreSQL em produção.
>
> As telas usam templates Jinja2 com Tailwind CSS. Senhas são
> protegidas com hash bcrypt, as entradas dos formulários são validadas
> no servidor e os erros retornam mensagens amigáveis, como vimos na
> tela de login.

## BLOCO 6 — Repositório, testes e boas práticas (Maria, ~40s)

*[NA TELA: página do repositório no GitHub — histórico de commits,
README rolando pelas seções, pasta docs/evidencias com os prints]*

> Todo o desenvolvimento está versionado no GitHub. O histórico de
> commits mostra a evolução por etapas: protótipos das telas, backend
> do fluxo de doação, integração do frontend e a fase de testes.
>
> O README documenta o projeto completo: objetivo, tecnologias com
> justificativas, estrutura de pastas, passo a passo de instalação e a
> seção "Como utilizar a aplicação", do componente extensionista.
>
> Sobre qualidade: o projeto tem 18 testes unitários com pytest e um
> teste de ponta a ponta com Playwright que navega o fluxo real no
> navegador e valida 20 verificações, gerando automaticamente os prints
> de evidência que estão na pasta docs.

## BLOCO 7 — Decisões técnicas e encerramento (Robson, ~35s)

*[NA TELA: voltar para a vitrine da aplicação]*

> Resumindo nossas principais decisões técnicas: moderação obrigatória
> antes da publicação, chat interno para proteger a privacidade,
> arquitetura em camadas para o time trabalhar em paralelo sem
> conflitos, e testes automatizados como critério de pronto.
>
> O Mochila Cheia mostra que uma solução tecnicamente simples pode
> gerar impacto social real: menos material desperdiçado, mais crianças
> com o que precisam para estudar. Obrigado por assistir!

---

## Dicas de gravação

- **Tela + voz:** QuickTime → Arquivo → Nova Gravação de Tela, com o
  microfone ligado. Grave em janela do navegador no modo responsivo.
- **Todos os integrantes:** cada um pode gravar seu bloco separado
  (tela + voz) e juntar na ordem; ou gravar uma chamada do Meet com
  compartilhamento de tela e todos presentes.
- Ao publicar no YouTube, use visibilidade **"Não listado"** e cole o
  link no relatório PDF da Sprint 3.
- Se passar de 5 minutos, corte primeiro os tempos de navegação entre
  telas (dá para acelerar trechos sem fala em 1,5x no editor).
