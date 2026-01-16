"""
Testes Unitários - Mochila Cheia

Este módulo contém testes básicos para validar o funcionamento
das classes principais do sistema.

Execute com: pytest tests/test_models.py -v
"""

import sys
import os

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from models import (
    Usuario, TipoUsuario,
    Categoria,
    Item, EstadoConservacao, StatusItem,
    Solicitacao, StatusSolicitacao,
    PontoDeColeta,
    Mensagem, StatusMensagem
)


class TestUsuario:
    """Testes para a classe Usuario."""
    
    def test_criar_usuario_doador(self):
        """Testa criação de um usuário doador."""
        usuario = Usuario(
            nome="Maria Silva",
            email="maria@email.com",
            senha="senha123",
            tipo_usuario=TipoUsuario.DOADOR
        )
        
        assert usuario.nome == "Maria Silva"
        assert usuario.email == "maria@email.com"
        assert usuario.tipo_usuario == TipoUsuario.DOADOR
        assert usuario.ativo == True
    
    def test_criar_usuario_receptor(self):
        """Testa criação de um usuário receptor."""
        usuario = Usuario(
            nome="João Pedro",
            email="joao@email.com",
            senha="senha456",
            tipo_usuario=TipoUsuario.RECEPTOR
        )
        
        assert usuario.nome == "João Pedro"
        assert usuario.tipo_usuario == TipoUsuario.RECEPTOR
    
    def test_login_correto(self):
        """Testa login com credenciais corretas."""
        usuario = Usuario(
            nome="Teste",
            email="teste@email.com",
            senha="minhasenha",
            tipo_usuario=TipoUsuario.DOADOR
        )
        
        assert usuario.login("teste@email.com", "minhasenha") == True
    
    def test_login_incorreto(self):
        """Testa login com credenciais incorretas."""
        usuario = Usuario(
            nome="Teste",
            email="teste@email.com",
            senha="minhasenha",
            tipo_usuario=TipoUsuario.DOADOR
        )
        
        assert usuario.login("teste@email.com", "senhaerrada") == False
    
    def test_atualizar_perfil(self):
        """Testa atualização do perfil."""
        usuario = Usuario(
            nome="Nome Original",
            email="teste@email.com",
            senha="senha",
            tipo_usuario=TipoUsuario.DOADOR
        )
        
        usuario.atualizar_perfil(nome="Nome Atualizado", telefone="99999-9999")
        
        assert usuario.nome == "Nome Atualizado"
        assert usuario.telefone == "99999-9999"


class TestCategoria:
    """Testes para a classe Categoria."""
    
    def test_criar_categoria(self):
        """Testa criação de uma categoria."""
        categoria = Categoria(
            nome="Mochilas",
            descricao="Mochilas escolares"
        )
        
        assert categoria.nome == "Mochilas"
        assert categoria.descricao == "Mochilas escolares"
        assert categoria.ativa == True
    
    def test_criar_categorias_padrao(self):
        """Testa criação das categorias padrão."""
        Categoria.resetar_contador()
        categorias = Categoria.criar_categorias_padrao()
        
        assert len(categorias) == 9
        assert categorias[0].nome == "Mochilas"
        assert categorias[1].nome == "Livros"


class TestItem:
    """Testes para a classe Item."""
    
    def setup_method(self):
        """Configuração inicial para cada teste."""
        self.doador = Usuario(
            nome="Doador Teste",
            email="doador@email.com",
            senha="senha",
            tipo_usuario=TipoUsuario.DOADOR
        )
        
        self.categoria = Categoria(nome="Teste", descricao="Categoria teste")
    
    def test_criar_item(self):
        """Testa criação de um item."""
        item = Item(
            titulo="Mochila Azul",
            descricao="Mochila em bom estado",
            categoria=self.categoria,
            estado_conservacao=EstadoConservacao.POUCO_USADO,
            doador=self.doador
        )
        
        assert item.titulo == "Mochila Azul"
        assert item.status == StatusItem.PENDENTE_MODERACAO
        assert item.doador == self.doador
    
    def test_aprovar_item(self):
        """Testa aprovação de um item."""
        item = Item(
            titulo="Livro Didático",
            descricao="Livro do 5º ano",
            categoria=self.categoria,
            estado_conservacao=EstadoConservacao.USADO,
            doador=self.doador
        )
        
        item.aprovar()
        
        assert item.status == StatusItem.DISPONIVEL
    
    def test_reservar_item(self):
        """Testa reserva de um item."""
        item = Item(
            titulo="Estojo",
            descricao="Estojo completo",
            categoria=self.categoria,
            estado_conservacao=EstadoConservacao.NOVO,
            doador=self.doador
        )
        
        item.aprovar()  # Precisa estar disponível primeiro
        resultado = item.reservar()
        
        assert resultado == True
        assert item.status == StatusItem.RESERVADO
    
    def test_adicionar_foto(self):
        """Testa adição de foto a um item."""
        item = Item(
            titulo="Caderno",
            descricao="Caderno universitário",
            categoria=self.categoria,
            estado_conservacao=EstadoConservacao.NOVO,
            doador=self.doador
        )
        
        item.adicionar_foto("http://exemplo.com/foto.jpg")
        
        assert len(item.fotos) == 1
        assert "http://exemplo.com/foto.jpg" in item.fotos


class TestSolicitacao:
    """Testes para a classe Solicitacao."""
    
    def setup_method(self):
        """Configuração inicial para cada teste."""
        self.doador = Usuario(
            nome="Doador",
            email="doador@email.com",
            senha="senha",
            tipo_usuario=TipoUsuario.DOADOR
        )
        
        self.receptor = Usuario(
            nome="Receptor",
            email="receptor@email.com",
            senha="senha",
            tipo_usuario=TipoUsuario.RECEPTOR
        )
        
        self.categoria = Categoria(nome="Teste", descricao="Teste")
        
        self.item = Item(
            titulo="Item Teste",
            descricao="Descrição",
            categoria=self.categoria,
            estado_conservacao=EstadoConservacao.USADO,
            doador=self.doador
        )
        self.item.aprovar()
    
    def test_criar_solicitacao(self):
        """Testa criação de uma solicitação."""
        solicitacao = Solicitacao(
            item=self.item,
            solicitante=self.receptor,
            doador=self.doador
        )
        
        resultado = solicitacao.criar()
        
        assert solicitacao.status == StatusSolicitacao.PENDENTE
        assert resultado != {}  # Retorna dicionário não vazio
    
    def test_aceitar_solicitacao(self):
        """Testa aceitação de uma solicitação."""
        solicitacao = Solicitacao(
            item=self.item,
            solicitante=self.receptor,
            doador=self.doador
        )
        solicitacao.criar()
        
        resultado = solicitacao.aceitar()
        
        assert resultado == True
        assert solicitacao.status == StatusSolicitacao.ACEITA
        assert self.item.status == StatusItem.RESERVADO
    
    def test_finalizar_solicitacao(self):
        """Testa finalização de uma solicitação."""
        solicitacao = Solicitacao(
            item=self.item,
            solicitante=self.receptor,
            doador=self.doador
        )
        solicitacao.criar()
        solicitacao.aceitar()
        
        resultado = solicitacao.finalizar()
        
        assert resultado == True
        assert solicitacao.status == StatusSolicitacao.FINALIZADA
        assert self.item.status == StatusItem.DOADO


class TestPontoDeColeta:
    """Testes para a classe PontoDeColeta."""
    
    def test_criar_ponto(self):
        """Testa criação de um ponto de coleta."""
        ponto = PontoDeColeta(
            nome="Escola Municipal",
            endereco_completo="Rua Principal, 100",
            horario_funcionamento="8h às 17h",
            responsavel="Diretor João"
        )
        
        assert ponto.nome == "Escola Municipal"
        assert ponto.ativo == True
    
    def test_receber_item(self):
        """Testa recebimento de item no ponto."""
        ponto = PontoDeColeta(
            nome="Ponto Teste",
            endereco_completo="Endereço",
            horario_funcionamento="8h às 17h",
            responsavel="Responsável"
        )
        
        doador = Usuario(
            nome="Doador",
            email="d@email.com",
            senha="s",
            tipo_usuario=TipoUsuario.DOADOR
        )
        categoria = Categoria(nome="Cat", descricao="")
        item = Item(
            titulo="Item",
            descricao="",
            categoria=categoria,
            estado_conservacao=EstadoConservacao.NOVO,
            doador=doador
        )
        
        resultado = ponto.receber_item(item)
        
        assert resultado == True
        assert ponto.quantidade_itens == 1


class TestMensagem:
    """Testes para a classe Mensagem."""
    
    def setup_method(self):
        """Configuração inicial."""
        self.usuario1 = Usuario(
            nome="Usuario 1",
            email="u1@email.com",
            senha="s",
            tipo_usuario=TipoUsuario.DOADOR
        )
        
        self.usuario2 = Usuario(
            nome="Usuario 2",
            email="u2@email.com",
            senha="s",
            tipo_usuario=TipoUsuario.RECEPTOR
        )
    
    def test_enviar_mensagem(self):
        """Testa envio de mensagem."""
        msg = Mensagem(
            remetente=self.usuario1,
            destinatario=self.usuario2,
            conteudo="Olá, tudo bem?"
        )
        
        resultado = msg.enviar()
        
        assert resultado == True
        assert msg.status == StatusMensagem.ENVIADA
    
    def test_marcar_como_lida(self):
        """Testa marcação de mensagem como lida."""
        msg = Mensagem(
            remetente=self.usuario1,
            destinatario=self.usuario2,
            conteudo="Mensagem de teste"
        )
        msg.enviar()
        
        msg.marcar_como_lida()
        
        assert msg.status == StatusMensagem.LIDA
        assert msg.foi_lida == True


# Execução direta dos testes
if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
