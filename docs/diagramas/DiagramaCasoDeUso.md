# Diagrama de Caso de Uso Corrigido

O código abaixo utiliza a sintaxe `usecase` do Mermaid, que é a correta para criar Diagramas de Caso de Uso UML. A sintaxe `graph TD` que estava sendo usada anteriormente é para fluxogramas genéricos e não consegue interpretar corretamente os atores e relacionamentos UML.

## Código Corrigido

```mermaid
usecase "Sistema Mochila Cheia"
    actor Usuário
    actor Doador
    actor Receptor
    actor Moderador

    Usuário <|-- Doador
    Usuário <|-- Receptor
    
    rectangle "Funcionalidades do Sistema" {
        Usuário -- (Gerenciar Cadastro)
        Usuário -- (Buscar Itens)

        Doador -- (Cadastrar Item)
        Doador -- (Gerenciar Meus Itens)
        Doador -- (Responder Solicitação)

        Receptor -- (Solicitar Item)
        
        Doador -- (Trocar Mensagens)
        Receptor -- (Trocar Mensagens)
        
        Moderador -- (Moderar Itens)
        
        (Gerenciar Cadastro) .> (Autenticar-se) : <<include>>
        (Cadastrar Item) .> (Autenticar-se) : <<include>>
        (Gerenciar Meus Itens) .> (Autenticar-se) : <<include>>
        (Responder Solicitação) .> (Autenticar-se) : <<include>>
        (Solicitar Item) .> (Autenticar-se) : <<include>>
        (Moderar Itens) .> (Autenticar-se) : <<include>>
        (Trocar Mensagens) .> (Autenticar-se) : <<include>>
    }
```

### Principais Correções e Melhorias:

1.  **`usecase "Título"`**: Define o tipo de diagrama correto.
2.  **`actor Nome`**: Cria corretamente os atores como "stick figures".
3.  **`Usuário <|-- Doador`**: Usa a seta `<|--` para indicar herança (Doador *é um tipo de* Usuário).
4.  **`rectangle "..."`**: Cria a "caixa" que representa os limites do sistema.
5.  **`Ator -- (Caso de Uso)`**: É a sintaxe padrão para ligar um ator a um caso de uso.
6.  **`(CasoDeUso1) .> (CasoDeUso2) : <<include>>`**: É a forma correta de mostrar a relação de inclusão.

Este código deve renderizar perfeitamente no seu visualizador.
