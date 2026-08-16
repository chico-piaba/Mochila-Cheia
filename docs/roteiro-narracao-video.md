# Roteiro de Narração — Vídeo Demo Mochila Cheia (1min30s)

Vídeo: `docs/evidencias/demo-mochila-cheia.mp4`

Como gravar: abra o vídeo, dê play e leia cada fala no tempo indicado.
Fale com calma — cada bloco tem folga. Grave o áudio com o app
Gravador de Voz (ou QuickTime > Novo Arquivo de Áudio) e salve como
`narracao.m4a`.

---

## 0:00 – 0:10 — Vitrine (visitante)

> "Este é o Mochila Cheia, nossa plataforma que conecta doadores de
> material escolar a estudantes que precisam. Na tela inicial, qualquer
> pessoa pode ver os itens disponíveis perto de você, com foto,
> categoria e localização."

## 0:10 – 0:25 — Doadora publica um item

> "Agora a Maria, que é doadora, faz login e publica uma doação. Ela
> preenche o título, a categoria, o estado de conservação, uma descrição
> e anexa a foto do item."

## 0:25 – 0:32 — Item pendente de moderação

> "O item publicado fica com status pendente e ainda não aparece na
> vitrine — antes, ele passa por uma moderação, para garantir a
> segurança da plataforma."

## 0:32 – 0:45 — Moderação aprova

> "No painel do moderador, o item entra na fila de revisão. O moderador
> confere a foto, a descrição e os dados do doador, e então aprova a
> publicação."

## 0:45 – 0:55 — Item na vitrine + receptor solicita

> "Aprovado, o item aparece imediatamente na vitrine. O João, que é
> receptor, encontra o item, abre os detalhes e faz a solicitação com
> um toque."

## 0:55 – 1:05 — Solicitações e chat

> "A solicitação fica registrada em 'Minhas Solicitações'. Pelo chat
> interno, doador e receptor combinam a entrega sem precisar expor
> telefone ou endereço."

## 1:05 – 1:20 — Notificações e aceite

> "A doadora recebe uma notificação da nova solicitação e pode aceitar
> direto pela tela de solicitações recebidas."

## 1:20 – 1:30 — Pontos de coleta (encerramento)

> "Por fim, a entrega pode acontecer em um dos pontos de coleta
> parceiros, como escolas e bibliotecas. Esse é o Mochila Cheia:
> tecnologia simples, impacto social real."

---

## Depois de gravar

Junte o áudio com o vídeo (ffmpeg já instalado):

```bash
ffmpeg -i docs/evidencias/demo-mochila-cheia.mp4 -i narracao.m4a \
  -c:v copy -c:a aac -shortest video-final-narrado.mp4
```

Ou me envie o arquivo de áudio aqui na sessão que eu faço a junção e os
ajustes de sincronia.

### Alternativa (tudo de uma vez)

Abra o vídeo em tela cheia e use QuickTime > Novo Arquivo de Tela
com o microfone ligado, narrando enquanto o vídeo roda. Sai pronto,
sem edição.
