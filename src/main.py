#!/usr/bin/env python3
"""
Mochila Cheia - Demonstração do Sistema

Este script demonstra o funcionamento das classes principais do MVP
da plataforma Mochila Cheia, que conecta doadores de materiais escolares
a estudantes que precisam desses itens.

Autor: Rodrigo Lima, Julio Cesar
Projeto: Mochila Cheia - Projeto Integrado II (UFCA)
"""

from models import (
    Usuario, TipoUsuario,
    Categoria,
    Item, EstadoConservacao, StatusItem,
    Solicitacao, StatusSolicitacao,
    PontoDeColeta,
    Mensagem, StatusMensagem
)


def linha_separadora(titulo: str = "") -> None:
    """Imprime uma linha separadora com título opcional."""
    print("\n" + "=" * 60)
    if titulo:
        print(f"  {titulo}")
        print("=" * 60)
    print()


def demonstrar_cadastro_usuarios() -> tuple:
    """
    Demonstra o cadastro de usuários no sistema.
    
    Returns:
        Tupla com (doador, receptor, moderador)
    """
    linha_separadora("1. CADASTRO DE USUÁRIOS")
    
    # Criando um doador
    print("Cadastrando um DOADOR...")
    doador = Usuario(
        nome="Maria Silva Santos",
        email="maria.silva@email.com",
        senha="senha123",
        tipo_usuario=TipoUsuario.DOADOR,
        telefone="(85) 99999-1111",
        endereco="Fortaleza, CE - Aldeota"
    )
    doador.cadastrar()
    print(f"   Dados: {doador}")
    
    print()
    
    # Criando um receptor
    print("Cadastrando um RECEPTOR...")
    receptor = Usuario(
        nome="João Pedro Oliveira",
        email="joao.pedro@email.com",
        senha="senha456",
        tipo_usuario=TipoUsuario.RECEPTOR,
        telefone="(85) 99999-2222",
        endereco="Fortaleza, CE - Messejana"
    )
    receptor.cadastrar()
    print(f"   Dados: {receptor}")
    
    print()
    
    # Criando um moderador
    print("Cadastrando um MODERADOR...")
    moderador = Usuario(
        nome="Ana Moderadora",
        email="ana.mod@mochilacheia.com",
        senha="admin123",
        tipo_usuario=TipoUsuario.MODERADOR,
        endereco="Fortaleza, CE - Centro"
    )
    moderador.cadastrar()
    print(f"   Dados: {moderador}")
    
    return doador, receptor, moderador


def demonstrar_categorias() -> list:
    """
    Demonstra a criação de categorias.
    
    Returns:
        Lista de categorias criadas
    """
    linha_separadora("2. CATEGORIAS DO SISTEMA")
    
    print("Criando categorias padrão do sistema...")
    categorias = Categoria.criar_categorias_padrao()
    
    print("\nCategorias disponíveis:")
    for cat in categorias:
        print(f"   • {cat.nome}: {cat.descricao[:50]}...")
    
    return categorias


def demonstrar_cadastro_itens(doador: Usuario, categorias: list) -> list:
    """
    Demonstra o cadastro de itens para doação.
    
    Args:
        doador: Usuário doador
        categorias: Lista de categorias disponíveis
        
    Returns:
        Lista de itens criados
    """
    linha_separadora("3. CADASTRO DE ITENS PARA DOAÇÃO")
    
    itens = []
    
    # Item 1: Mochila
    print("Cadastrando item: Mochila Azul...")
    mochila = Item(
        titulo="Mochila Escolar Azul",
        descricao="Mochila em ótimo estado, pouco usada. Ideal para ensino fundamental.",
        categoria=categorias[0],  # Mochilas
        estado_conservacao=EstadoConservacao.POUCO_USADO,
        doador=doador,
        localizacao="Fortaleza, CE - Aldeota"
    )
    mochila.adicionar_foto("https://exemplo.com/foto_mochila_1.jpg")
    mochila.adicionar_foto("https://exemplo.com/foto_mochila_2.jpg")
    mochila.cadastrar_item()
    itens.append(mochila)
    
    print()
    
    # Item 2: Livros
    print("Cadastrando item: Kit de Livros...")
    livros = Item(
        titulo="Kit Livros 5º Ano - Matemática e Português",
        descricao="Livros didáticos do 5º ano, em bom estado. Algumas anotações a lápis.",
        categoria=categorias[1],  # Livros
        estado_conservacao=EstadoConservacao.USADO,
        doador=doador
    )
    livros.cadastrar_item()
    itens.append(livros)
    
    print()
    
    # Item 3: Estojo
    print("Cadastrando item: Estojo Completo...")
    estojo = Item(
        titulo="Estojo Completo com Material",
        descricao="Estojo novo com lápis, canetas, borracha e apontador. Nunca usado.",
        categoria=categorias[3],  # Estojos
        estado_conservacao=EstadoConservacao.NOVO,
        doador=doador
    )
    estojo.cadastrar_item()
    itens.append(estojo)
    
    return itens


def demonstrar_moderacao(itens: list) -> None:
    """
    Demonstra o processo de moderação de itens.
    
    Args:
        itens: Lista de itens para moderar
    """
    linha_separadora("4. MODERAÇÃO DE ITENS")
    
    print("Moderador analisando itens cadastrados...\n")
    
    # Aprovando a mochila
    print(f"Analisando: {itens[0].titulo}")
    print("   → Item verificado, fotos adequadas.")
    itens[0].aprovar()
    
    print()
    
    # Aprovando os livros
    print(f"Analisando: {itens[1].titulo}")
    print("   → Item verificado, descrição clara.")
    itens[1].aprovar()
    
    print()
    
    # Aprovando o estojo
    print(f"Analisando: {itens[2].titulo}")
    print("   → Item novo, bem descrito.")
    itens[2].aprovar()


def demonstrar_solicitacao(item: Item, receptor: Usuario, doador: Usuario) -> Solicitacao:
    """
    Demonstra o processo de solicitação de um item.
    
    Args:
        item: Item a ser solicitado
        receptor: Usuário que solicita
        doador: Usuário que possui o item
        
    Returns:
        Objeto Solicitacao criado
    """
    linha_separadora("5. SOLICITAÇÃO DE ITEM")
    
    print(f"Receptor '{receptor.nome}' está solicitando:")
    print(f"   Item: {item.titulo}")
    print(f"   Doador: {doador.nome}")
    print()
    
    solicitacao = Solicitacao(
        item=item,
        solicitante=receptor,
        doador=doador
    )
    solicitacao.criar()
    
    return solicitacao


def demonstrar_fluxo_doacao(solicitacao: Solicitacao) -> None:
    """
    Demonstra o fluxo completo de uma doação.
    
    Args:
        solicitacao: Solicitação a ser processada
    """
    linha_separadora("6. FLUXO DE DOAÇÃO")
    
    # Doador aceita a solicitação
    print("PASSO 1: Doador analisa a solicitação...")
    print(f"   Solicitante: {solicitacao.solicitante.nome}")
    print(f"   Item: {solicitacao.item.titulo}")
    print()
    
    print("PASSO 2: Doador aceita a solicitação...")
    solicitacao.aceitar()
    
    print()
    
    print("PASSO 3: Confirmação da entrega...")
    print("   O receptor retirou o item com sucesso!")
    solicitacao.finalizar()


def demonstrar_mensagens(doador: Usuario, receptor: Usuario, solicitacao: Solicitacao) -> None:
    """
    Demonstra a troca de mensagens entre usuários.
    
    Args:
        doador: Usuário doador
        receptor: Usuário receptor
        solicitacao: Solicitação relacionada
    """
    linha_separadora("7. CHAT ENTRE USUÁRIOS")
    
    print("Troca de mensagens para combinar a entrega:\n")
    
    # Mensagem do receptor
    msg1 = Mensagem(
        remetente=receptor,
        destinatario=doador,
        conteudo="Olá! Vi sua mochila disponível. Podemos combinar a retirada para amanhã?",
        solicitacao=solicitacao
    )
    msg1.enviar()
    print()
    
    # Resposta do doador
    msg2 = Mensagem(
        remetente=doador,
        destinatario=receptor,
        conteudo="Oi! Claro, pode ser amanhã às 14h no Shopping Iguatemi?",
        solicitacao=solicitacao
    )
    msg2.enviar()
    print()
    
    # Confirmação do receptor
    msg3 = Mensagem(
        remetente=receptor,
        destinatario=doador,
        conteudo="Perfeito! Estarei lá. Muito obrigado pela doação!",
        solicitacao=solicitacao
    )
    msg3.enviar()
    
    # Simula leitura
    msg1.marcar_como_lida()


def demonstrar_ponto_coleta(item: Item, receptor: Usuario) -> None:
    """
    Demonstra o uso de um ponto de coleta.
    
    Args:
        item: Item a ser entregue
        receptor: Usuário que retirará
    """
    linha_separadora("8. PONTO DE COLETA")
    
    # Criando um ponto de coleta
    ponto = PontoDeColeta(
        nome="Escola Municipal Centro",
        endereco_completo="Rua Principal, 100 - Centro, Fortaleza/CE",
        horario_funcionamento="Segunda a Sexta: 8h às 17h",
        responsavel="Diretora Maria José",
        telefone="(85) 3333-4444"
    )
    ponto.cadastrar_ponto()
    
    print()
    print("Simulando uso do ponto de coleta:")
    
    # Doador deixa item no ponto
    print("\n1. Doador deixa o item no ponto de coleta...")
    ponto.receber_item(item)
    
    # Listando itens
    print("\n2. Itens disponíveis para retirada:")
    ponto.listar_itens()
    
    # Receptor retira o item
    print("\n3. Receptor retira o item...")
    ponto.entregar_item(item, receptor)


def exibir_resumo(doador: Usuario, receptor: Usuario, itens: list) -> None:
    """
    Exibe um resumo das operações realizadas.
    
    Args:
        doador: Usuário doador
        receptor: Usuário receptor
        itens: Lista de itens cadastrados
    """
    linha_separadora("RESUMO DA DEMONSTRAÇÃO")
    
    print("📊 Estatísticas:")
    print(f"   • Usuários cadastrados: 3 (1 doador, 1 receptor, 1 moderador)")
    print(f"   • Categorias criadas: 9")
    print(f"   • Itens cadastrados: {len(itens)}")
    print(f"   • Solicitações processadas: 1")
    print(f"   • Doações concluídas: 1")
    
    print("\n✅ Demonstração concluída com sucesso!")
    print("\n📚 Este é o MVP do projeto Mochila Cheia.")
    print("   Desenvolvido para o Projeto Integrado II - UFCA")
    print("   Por: Rodrigo Lima e Julio Cesar")


def main():
    """
    Função principal que executa a demonstração completa do sistema.
    """
    print("\n" + "=" * 60)
    print("       🎒 MOCHILA CHEIA - DEMONSTRAÇÃO DO MVP 🎒")
    print("=" * 60)
    print("\nPlataforma de Doação de Materiais Escolares")
    print("Projeto Integrado II - UFCA - ADS")
    
    # 1. Cadastro de usuários
    doador, receptor, moderador = demonstrar_cadastro_usuarios()
    
    # 2. Criação de categorias
    categorias = demonstrar_categorias()
    
    # 3. Cadastro de itens
    itens = demonstrar_cadastro_itens(doador, categorias)
    
    # 4. Moderação
    demonstrar_moderacao(itens)
    
    # 5. Solicitação
    solicitacao = demonstrar_solicitacao(itens[0], receptor, doador)
    
    # 6. Fluxo de doação
    demonstrar_fluxo_doacao(solicitacao)
    
    # 7. Chat
    demonstrar_mensagens(doador, receptor, solicitacao)
    
    # 8. Ponto de coleta (com um novo item)
    demonstrar_ponto_coleta(itens[1], receptor)
    
    # Resumo
    exibir_resumo(doador, receptor, itens)


if __name__ == "__main__":
    main()
