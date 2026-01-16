-- ============================================================
-- MOCHILA CHEIA - DADOS DE EXEMPLO (SEED)
-- ============================================================
-- Script para popular o banco de dados com dados de teste
-- Execute após o schema.sql
-- ============================================================

-- ============================================================
-- CATEGORIAS PADRÃO DO SISTEMA
-- ============================================================

INSERT INTO CATEGORIA (nome, descricao, ativa) VALUES
('Mochilas', 'Mochilas escolares de diversos tamanhos e modelos', TRUE),
('Livros', 'Livros didáticos, paradidáticos e literatura infantojuvenil', TRUE),
('Cadernos', 'Cadernos de todas as matérias e quantidades de folhas', TRUE),
('Estojos', 'Estojos para guardar material de escrita', TRUE),
('Material de Escrita', 'Canetas, lápis, borrachas, apontadores, etc.', TRUE),
('Material de Arte', 'Tintas, pincéis, papéis coloridos, tesouras, etc.', TRUE),
('Uniformes', 'Uniformes escolares em bom estado', TRUE),
('Calculadoras', 'Calculadoras científicas e básicas', TRUE),
('Outros', 'Outros materiais escolares não categorizados', TRUE);

-- ============================================================
-- USUÁRIOS DE EXEMPLO
-- ============================================================
-- Senhas são hashes SHA-256 de "senha123"

INSERT INTO USUARIO (nome, email, senha_hash, telefone, endereco, tipo_usuario, ativo) VALUES
-- Doadores
('Maria Silva Santos', 'maria.silva@email.com', 
 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f', 
 '(85) 99999-1111', 'Fortaleza, CE - Aldeota', 'doador', TRUE),

('Carlos Eduardo Lima', 'carlos.lima@email.com', 
 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f', 
 '(85) 99999-2222', 'Fortaleza, CE - Meireles', 'doador', TRUE),

('Ana Paula Ferreira', 'ana.ferreira@email.com', 
 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f', 
 '(85) 99999-3333', 'Fortaleza, CE - Papicu', 'doador', TRUE),

-- Receptores
('João Pedro Oliveira', 'joao.pedro@email.com', 
 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f', 
 '(85) 99999-4444', 'Fortaleza, CE - Messejana', 'receptor', TRUE),

('Francisca Souza', 'francisca.souza@email.com', 
 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f', 
 '(85) 99999-5555', 'Fortaleza, CE - Barra do Ceará', 'receptor', TRUE),

('Pedro Henrique Costa', 'pedro.costa@email.com', 
 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f', 
 '(85) 99999-6666', 'Fortaleza, CE - Jangurussu', 'receptor', TRUE),

-- Moderadores
('Admin Mochila Cheia', 'admin@mochilacheia.com', 
 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f', 
 '(85) 3333-0000', 'Fortaleza, CE - Centro', 'moderador', TRUE),

('Moderador Ana', 'ana.mod@mochilacheia.com', 
 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f', 
 NULL, 'Fortaleza, CE - Centro', 'moderador', TRUE);

-- ============================================================
-- PONTOS DE COLETA
-- ============================================================

INSERT INTO PONTO_COLETA (nome, endereco_completo, horario_funcionamento, responsavel, telefone, email, ativo) VALUES
('Escola Municipal Centro', 
 'Rua Principal, 100 - Centro, Fortaleza/CE, 60000-000',
 'Segunda a Sexta: 8h às 17h',
 'Diretora Maria José', '(85) 3333-1111', 'contato@escolacentro.edu.br', TRUE),

('Igreja São José', 
 'Av. Santos Dumont, 500 - Aldeota, Fortaleza/CE, 60150-160',
 'Segunda a Sábado: 9h às 18h',
 'Padre Antônio', '(85) 3333-2222', 'secretaria@saojose.org.br', TRUE),

('Papelaria Escolar', 
 'Rua Barão de Studart, 300 - Meireles, Fortaleza/CE, 60120-000',
 'Segunda a Sábado: 8h às 20h',
 'José Comerciante', '(85) 3333-3333', 'contato@papelariaescolar.com', TRUE),

('Centro Comunitário Messejana', 
 'Rua da Paz, 200 - Messejana, Fortaleza/CE, 60841-000',
 'Segunda a Sexta: 7h às 16h',
 'Líder Comunitário Francisco', '(85) 3333-4444', NULL, TRUE);

-- ============================================================
-- ITENS PARA DOAÇÃO
-- ============================================================

-- Itens disponíveis
INSERT INTO ITEM (titulo, descricao, estado_conservacao, status, localizacao, foto_url, 
                  fk_id_doador, fk_id_categoria, fk_id_moderador, data_moderacao) VALUES
('Mochila Escolar Azul',
 'Mochila em ótimo estado, pouco usada. Ideal para ensino fundamental. Tem compartimentos para garrafa e estojo.',
 'pouco_usado', 'disponivel', 'Fortaleza, CE - Aldeota',
 'https://exemplo.com/fotos/mochila_azul.jpg',
 1, 1, 7, CURRENT_TIMESTAMP),

('Kit Livros 5º Ano - Matemática e Português',
 'Livros didáticos do 5º ano em bom estado. Algumas anotações a lápis que podem ser apagadas.',
 'usado', 'disponivel', 'Fortaleza, CE - Aldeota',
 'https://exemplo.com/fotos/livros_5ano.jpg',
 1, 2, 7, CURRENT_TIMESTAMP),

('Estojo Completo com Material',
 'Estojo novo contendo: 12 lápis de cor, 2 lápis preto, 1 borracha, 1 apontador, 2 canetas azuis.',
 'novo', 'disponivel', 'Fortaleza, CE - Meireles',
 'https://exemplo.com/fotos/estojo_completo.jpg',
 2, 4, 7, CURRENT_TIMESTAMP),

('Cadernos Universitários 10 Matérias (3 unidades)',
 'Três cadernos de 200 folhas cada, capa dura. Perfeitos para ensino médio.',
 'novo', 'disponivel', 'Fortaleza, CE - Meireles',
 'https://exemplo.com/fotos/cadernos.jpg',
 2, 3, 8, CURRENT_TIMESTAMP),

('Uniforme Escolar Tamanho M',
 'Uniforme da Escola Municipal Centro: 2 camisas e 1 calça. Tamanho M (10-12 anos).',
 'pouco_usado', 'disponivel', 'Fortaleza, CE - Papicu',
 'https://exemplo.com/fotos/uniforme.jpg',
 3, 7, 8, CURRENT_TIMESTAMP);

-- Item reservado
INSERT INTO ITEM (titulo, descricao, estado_conservacao, status, localizacao, foto_url, 
                  fk_id_doador, fk_id_categoria, fk_id_moderador, data_moderacao) VALUES
('Calculadora Científica Casio',
 'Calculadora científica em perfeito funcionamento. Ideal para ensino médio e vestibular.',
 'usado', 'reservado', 'Fortaleza, CE - Aldeota',
 'https://exemplo.com/fotos/calculadora.jpg',
 1, 8, 7, CURRENT_TIMESTAMP);

-- Item já doado
INSERT INTO ITEM (titulo, descricao, estado_conservacao, status, localizacao, foto_url, 
                  fk_id_doador, fk_id_categoria, fk_id_moderador, data_moderacao) VALUES
('Mochila Rosa Infantil',
 'Mochila pequena para crianças de 4-6 anos. Estampa de personagens.',
 'pouco_usado', 'doado', 'Fortaleza, CE - Meireles',
 'https://exemplo.com/fotos/mochila_rosa.jpg',
 2, 1, 7, CURRENT_TIMESTAMP);

-- Item pendente de moderação
INSERT INTO ITEM (titulo, descricao, estado_conservacao, status, localizacao, foto_url, 
                  fk_id_doador, fk_id_categoria) VALUES
('Dicionário de Inglês-Português',
 'Dicionário escolar em bom estado. Edição 2023.',
 'usado', 'pendente_moderacao', 'Fortaleza, CE - Papicu',
 'https://exemplo.com/fotos/dicionario.jpg',
 3, 2);

-- ============================================================
-- SOLICITAÇÕES
-- ============================================================

-- Solicitação pendente
INSERT INTO SOLICITACAO (status, ordem_fila, fk_id_item, fk_id_receptor) VALUES
('pendente', 1, 1, 4);

-- Solicitação aceita (item reservado)
INSERT INTO SOLICITACAO (status, ordem_fila, fk_id_item, fk_id_receptor, data_resposta) VALUES
('aceita', 1, 6, 5, CURRENT_TIMESTAMP);

-- Solicitação finalizada (item doado)
INSERT INTO SOLICITACAO (status, ordem_fila, fk_id_item, fk_id_receptor, data_resposta, data_finalizacao) VALUES
('finalizada', 1, 7, 6, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- ============================================================
-- MENSAGENS DE EXEMPLO
-- ============================================================

-- Conversa sobre a mochila azul
INSERT INTO MENSAGEM (conteudo, status, fk_id_remetente, fk_id_destinatario, fk_id_solicitacao) VALUES
('Olá! Vi sua mochila azul disponível. Meu filho precisa muito para a escola. Podemos combinar a retirada?',
 'lida', 4, 1, 1),

('Oi João! Claro, fico feliz em ajudar. Podemos combinar para amanhã às 14h no Shopping Iguatemi?',
 'lida', 1, 4, 1),

('Perfeito! Estarei lá. Muito obrigado pela doação, vai ajudar muito!',
 'enviada', 4, 1, 1);

-- Conversa sobre a calculadora
INSERT INTO MENSAGEM (conteudo, status, fk_id_remetente, fk_id_destinatario, fk_id_solicitacao) VALUES
('Bom dia! Tenho interesse na calculadora. Estou no 3º ano do ensino médio e preciso para as aulas de física.',
 'lida', 5, 1, 2),

('Olá Francisca! A calculadora está em ótimo estado. Você pode retirar na Escola Municipal Centro, deixei lá.',
 'lida', 1, 5, 2);

-- ============================================================
-- NOTIFICAÇÕES DE EXEMPLO
-- ============================================================

INSERT INTO NOTIFICACAO (titulo, mensagem, status, fk_id_usuario_destino, fk_id_item, fk_id_solicitacao) VALUES
('Nova solicitação recebida!',
 'João Pedro Oliveira solicitou seu item "Mochila Escolar Azul".',
 'lida', 1, 1, 1),

('Sua solicitação foi aceita!',
 'Maria Silva Santos aceitou sua solicitação para "Calculadora Científica Casio". Entre em contato para combinar a retirada.',
 'lida', 5, 6, 2),

('Item aprovado pela moderação',
 'Seu item "Mochila Escolar Azul" foi aprovado e já está disponível para doação!',
 'lida', 1, 1, NULL),

('Nova mensagem recebida',
 'Você recebeu uma nova mensagem de João Pedro Oliveira.',
 'nao_lida', 1, NULL, 1);

-- ============================================================
-- VERIFICAÇÃO DOS DADOS
-- ============================================================
-- Consultas para verificar se os dados foram inseridos corretamente

-- SELECT 'Usuários cadastrados:' AS info, COUNT(*) AS total FROM USUARIO;
-- SELECT 'Categorias cadastradas:' AS info, COUNT(*) AS total FROM CATEGORIA;
-- SELECT 'Pontos de coleta:' AS info, COUNT(*) AS total FROM PONTO_COLETA;
-- SELECT 'Itens cadastrados:' AS info, COUNT(*) AS total FROM ITEM;
-- SELECT 'Solicitações:' AS info, COUNT(*) AS total FROM SOLICITACAO;
-- SELECT 'Mensagens:' AS info, COUNT(*) AS total FROM MENSAGEM;
-- SELECT 'Notificações:' AS info, COUNT(*) AS total FROM NOTIFICACAO;

-- Visualizar itens disponíveis
-- SELECT * FROM vw_itens_disponiveis;

-- Visualizar estatísticas
-- SELECT * FROM vw_estatisticas;
