-- ============================================================
-- MOCHILA CHEIA - PROJETO FÍSICO DE BANCO DE DADOS
-- ============================================================
-- Projeto: Mochila Cheia
-- Disciplina: Projeto de Banco de Dados (Projeto Integrado II)
-- Autores: Rodrigo Lima, Julio Cesar
-- Data: Janeiro/2026
-- SGBD: SQLite / PostgreSQL (compatível)
-- ============================================================

-- ============================================================
-- LIMPEZA DAS TABELAS (para recriação)
-- ============================================================
-- Ordem de DROP respeita as dependências (foreign keys)

DROP TABLE IF EXISTS MENSAGEM;
DROP TABLE IF EXISTS NOTIFICACAO;
DROP TABLE IF EXISTS SOLICITACAO;
DROP TABLE IF EXISTS ITEM;
DROP TABLE IF EXISTS PONTO_COLETA;
DROP TABLE IF EXISTS CATEGORIA;
DROP TABLE IF EXISTS USUARIO;

-- ============================================================
-- TABELA: USUARIO
-- ============================================================
-- Armazena todos os usuários do sistema (doadores, receptores, moderadores)
-- 
-- Decisões de projeto:
-- - email é UNIQUE para garantir unicidade no login
-- - senha_hash armazena hash SHA-256 (nunca texto plano)
-- - tipo_usuario usa CHECK constraint para garantir valores válidos
-- - data_cadastro tem valor DEFAULT para registro automático
-- ============================================================

CREATE TABLE USUARIO (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha_hash VARCHAR(255) NOT NULL,
    telefone VARCHAR(20),
    endereco VARCHAR(255),
    tipo_usuario VARCHAR(20) NOT NULL CHECK (tipo_usuario IN ('doador', 'receptor', 'moderador')),
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    
    -- Índice para busca por tipo de usuário
    -- Justificativa: Consultas frequentes filtram por tipo
    CONSTRAINT chk_nome_length CHECK (LENGTH(nome) >= 2),
    CONSTRAINT chk_email_format CHECK (email LIKE '%@%.%')
);

-- Índices adicionais para performance
CREATE INDEX idx_usuario_tipo ON USUARIO(tipo_usuario);
CREATE INDEX idx_usuario_email ON USUARIO(email);
CREATE INDEX idx_usuario_ativo ON USUARIO(ativo);

-- ============================================================
-- TABELA: CATEGORIA
-- ============================================================
-- Categoriza os tipos de materiais escolares
--
-- Decisões de projeto:
-- - Tabela separada permite adicionar novas categorias sem alterar código
-- - Descrição é opcional (TEXT para flexibilidade)
-- ============================================================

CREATE TABLE CATEGORIA (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(50) NOT NULL UNIQUE,
    descricao TEXT,
    ativa BOOLEAN DEFAULT TRUE
);

-- Índice para busca por nome de categoria
CREATE INDEX idx_categoria_nome ON CATEGORIA(nome);

-- ============================================================
-- TABELA: PONTO_COLETA
-- ============================================================
-- Armazena locais parceiros para entrega/retirada de itens
--
-- Decisões de projeto:
-- - Separado de USUARIO pois tem atributos específicos
-- - horario_funcionamento como VARCHAR para flexibilidade de formato
-- ============================================================

CREATE TABLE PONTO_COLETA (
    id_ponto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    endereco_completo VARCHAR(255) NOT NULL,
    horario_funcionamento VARCHAR(100),
    responsavel VARCHAR(100),
    telefone VARCHAR(20),
    email VARCHAR(100),
    ativo BOOLEAN DEFAULT TRUE,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para busca de pontos ativos
CREATE INDEX idx_ponto_ativo ON PONTO_COLETA(ativo);

-- ============================================================
-- TABELA: ITEM
-- ============================================================
-- Armazena os materiais escolares disponíveis para doação
--
-- Decisões de projeto:
-- - estado_conservacao e status usam CHECK para validar valores
-- - foto_url armazena URL da foto principal (pode ser expandido para tabela separada)
-- - fk_id_doador referencia quem cadastrou o item
-- - fk_id_categoria classifica o item
-- - fk_id_ponto_coleta indica onde o item está (opcional)
-- - fk_id_moderador registra quem aprovou/recusou
-- ============================================================

CREATE TABLE ITEM (
    id_item INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(100) NOT NULL,
    descricao TEXT,
    estado_conservacao VARCHAR(20) NOT NULL CHECK (
        estado_conservacao IN ('novo', 'pouco_usado', 'usado', 'necessita_reparo')
    ),
    status VARCHAR(30) NOT NULL DEFAULT 'pendente_moderacao' CHECK (
        status IN ('pendente_moderacao', 'disponivel', 'reservado', 'doado', 'recusado', 'inativo')
    ),
    localizacao VARCHAR(255),
    foto_url VARCHAR(500),
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_moderacao TIMESTAMP,
    
    -- Chaves estrangeiras
    fk_id_doador INTEGER NOT NULL,
    fk_id_categoria INTEGER NOT NULL,
    fk_id_ponto_coleta INTEGER,
    fk_id_moderador INTEGER,
    
    -- Constraints de integridade referencial
    CONSTRAINT fk_item_doador FOREIGN KEY (fk_id_doador) 
        REFERENCES USUARIO(id_usuario) ON DELETE CASCADE,
    CONSTRAINT fk_item_categoria FOREIGN KEY (fk_id_categoria) 
        REFERENCES CATEGORIA(id_categoria) ON DELETE RESTRICT,
    CONSTRAINT fk_item_ponto FOREIGN KEY (fk_id_ponto_coleta) 
        REFERENCES PONTO_COLETA(id_ponto) ON DELETE SET NULL,
    CONSTRAINT fk_item_moderador FOREIGN KEY (fk_id_moderador) 
        REFERENCES USUARIO(id_usuario) ON DELETE SET NULL,
    
    -- Validação do título
    CONSTRAINT chk_titulo_length CHECK (LENGTH(titulo) >= 3)
);

-- Índices para otimização de consultas frequentes
CREATE INDEX idx_item_status ON ITEM(status);
CREATE INDEX idx_item_doador ON ITEM(fk_id_doador);
CREATE INDEX idx_item_categoria ON ITEM(fk_id_categoria);
CREATE INDEX idx_item_data ON ITEM(data_cadastro);

-- ============================================================
-- TABELA: SOLICITACAO
-- ============================================================
-- Registra as solicitações de itens por receptores
--
-- Decisões de projeto:
-- - Conecta um receptor (solicitante) a um item específico
-- - ordem_fila permite gerenciar múltiplas solicitações por item
-- - Datas separadas para solicitação, resposta e finalização
-- ============================================================

CREATE TABLE SOLICITACAO (
    id_solicitacao INTEGER PRIMARY KEY AUTOINCREMENT,
    status VARCHAR(20) NOT NULL DEFAULT 'pendente' CHECK (
        status IN ('pendente', 'aceita', 'recusada', 'cancelada', 'finalizada', 'expirada')
    ),
    ordem_fila INTEGER DEFAULT 1,
    data_solicitacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_resposta TIMESTAMP,
    data_finalizacao TIMESTAMP,
    observacoes TEXT,
    
    -- Chaves estrangeiras
    fk_id_item INTEGER NOT NULL,
    fk_id_receptor INTEGER NOT NULL,
    
    -- Constraints de integridade referencial
    CONSTRAINT fk_solicitacao_item FOREIGN KEY (fk_id_item) 
        REFERENCES ITEM(id_item) ON DELETE CASCADE,
    CONSTRAINT fk_solicitacao_receptor FOREIGN KEY (fk_id_receptor) 
        REFERENCES USUARIO(id_usuario) ON DELETE CASCADE,
    
    -- Impede que o mesmo receptor solicite o mesmo item duas vezes
    CONSTRAINT uq_solicitacao_receptor_item UNIQUE (fk_id_item, fk_id_receptor)
);

-- Índices para consultas de solicitações
CREATE INDEX idx_solicitacao_status ON SOLICITACAO(status);
CREATE INDEX idx_solicitacao_item ON SOLICITACAO(fk_id_item);
CREATE INDEX idx_solicitacao_receptor ON SOLICITACAO(fk_id_receptor);
CREATE INDEX idx_solicitacao_data ON SOLICITACAO(data_solicitacao);

-- ============================================================
-- TABELA: MENSAGEM
-- ============================================================
-- Armazena mensagens trocadas entre usuários
--
-- Decisões de projeto:
-- - Vinculada a uma solicitação para contexto
-- - Permite rastrear status (enviada, lida)
-- - Remetente e destinatário são ambos usuários
-- ============================================================

CREATE TABLE MENSAGEM (
    id_mensagem INTEGER PRIMARY KEY AUTOINCREMENT,
    conteudo TEXT NOT NULL,
    status VARCHAR(20) DEFAULT 'enviada' CHECK (
        status IN ('enviada', 'entregue', 'lida', 'erro')
    ),
    data_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_leitura TIMESTAMP,
    
    -- Chaves estrangeiras
    fk_id_remetente INTEGER NOT NULL,
    fk_id_destinatario INTEGER NOT NULL,
    fk_id_solicitacao INTEGER,
    
    -- Constraints de integridade referencial
    CONSTRAINT fk_mensagem_remetente FOREIGN KEY (fk_id_remetente) 
        REFERENCES USUARIO(id_usuario) ON DELETE CASCADE,
    CONSTRAINT fk_mensagem_destinatario FOREIGN KEY (fk_id_destinatario) 
        REFERENCES USUARIO(id_usuario) ON DELETE CASCADE,
    CONSTRAINT fk_mensagem_solicitacao FOREIGN KEY (fk_id_solicitacao) 
        REFERENCES SOLICITACAO(id_solicitacao) ON DELETE SET NULL,
    
    -- Impede enviar mensagem para si mesmo
    CONSTRAINT chk_remetente_destinatario CHECK (fk_id_remetente != fk_id_destinatario)
);

-- Índices para busca de mensagens
CREATE INDEX idx_mensagem_remetente ON MENSAGEM(fk_id_remetente);
CREATE INDEX idx_mensagem_destinatario ON MENSAGEM(fk_id_destinatario);
CREATE INDEX idx_mensagem_solicitacao ON MENSAGEM(fk_id_solicitacao);
CREATE INDEX idx_mensagem_data ON MENSAGEM(data_envio);

-- ============================================================
-- TABELA: NOTIFICACAO
-- ============================================================
-- Armazena notificações enviadas aos usuários
--
-- Decisões de projeto:
-- - Notificações podem ser sobre itens ou solicitações
-- - link_destino permite navegação direta ao contexto
-- ============================================================

CREATE TABLE NOTIFICACAO (
    id_notificacao INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(100) NOT NULL,
    mensagem TEXT NOT NULL,
    status VARCHAR(20) DEFAULT 'nao_lida' CHECK (
        status IN ('nao_lida', 'lida', 'arquivada')
    ),
    link_destino VARCHAR(255),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_leitura TIMESTAMP,
    
    -- Chaves estrangeiras
    fk_id_usuario_destino INTEGER NOT NULL,
    fk_id_item INTEGER,
    fk_id_solicitacao INTEGER,
    
    -- Constraints de integridade referencial
    CONSTRAINT fk_notificacao_usuario FOREIGN KEY (fk_id_usuario_destino) 
        REFERENCES USUARIO(id_usuario) ON DELETE CASCADE,
    CONSTRAINT fk_notificacao_item FOREIGN KEY (fk_id_item) 
        REFERENCES ITEM(id_item) ON DELETE SET NULL,
    CONSTRAINT fk_notificacao_solicitacao FOREIGN KEY (fk_id_solicitacao) 
        REFERENCES SOLICITACAO(id_solicitacao) ON DELETE SET NULL
);

-- Índices para busca de notificações
CREATE INDEX idx_notificacao_usuario ON NOTIFICACAO(fk_id_usuario_destino);
CREATE INDEX idx_notificacao_status ON NOTIFICACAO(status);
CREATE INDEX idx_notificacao_data ON NOTIFICACAO(data_criacao);

-- ============================================================
-- VIEWS ÚTEIS
-- ============================================================
-- Views facilitam consultas complexas frequentes

-- View: Itens disponíveis com informações do doador
CREATE VIEW vw_itens_disponiveis AS
SELECT 
    i.id_item,
    i.titulo,
    i.descricao,
    i.estado_conservacao,
    i.localizacao,
    i.foto_url,
    i.data_cadastro,
    c.nome AS categoria,
    u.nome AS doador_nome,
    u.email AS doador_email
FROM ITEM i
JOIN CATEGORIA c ON i.fk_id_categoria = c.id_categoria
JOIN USUARIO u ON i.fk_id_doador = u.id_usuario
WHERE i.status = 'disponivel'
ORDER BY i.data_cadastro DESC;

-- View: Solicitações pendentes para doadores
CREATE VIEW vw_solicitacoes_pendentes AS
SELECT 
    s.id_solicitacao,
    s.data_solicitacao,
    i.titulo AS item_titulo,
    i.foto_url AS item_foto,
    receptor.nome AS receptor_nome,
    receptor.email AS receptor_email,
    doador.id_usuario AS doador_id,
    doador.nome AS doador_nome
FROM SOLICITACAO s
JOIN ITEM i ON s.fk_id_item = i.id_item
JOIN USUARIO receptor ON s.fk_id_receptor = receptor.id_usuario
JOIN USUARIO doador ON i.fk_id_doador = doador.id_usuario
WHERE s.status = 'pendente'
ORDER BY s.data_solicitacao ASC;

-- View: Estatísticas gerais do sistema
CREATE VIEW vw_estatisticas AS
SELECT
    (SELECT COUNT(*) FROM USUARIO WHERE tipo_usuario = 'doador' AND ativo = 1) AS total_doadores,
    (SELECT COUNT(*) FROM USUARIO WHERE tipo_usuario = 'receptor' AND ativo = 1) AS total_receptores,
    (SELECT COUNT(*) FROM ITEM WHERE status = 'disponivel') AS itens_disponiveis,
    (SELECT COUNT(*) FROM ITEM WHERE status = 'doado') AS itens_doados,
    (SELECT COUNT(*) FROM SOLICITACAO WHERE status = 'finalizada') AS doacoes_concluidas,
    (SELECT COUNT(*) FROM PONTO_COLETA WHERE ativo = 1) AS pontos_ativos;

-- ============================================================
-- COMENTÁRIOS SOBRE O PROJETO FÍSICO
-- ============================================================
-- 
-- 1. TIPOS DE DADOS ESCOLHIDOS:
--    - INTEGER para IDs (autoincremento)
--    - VARCHAR com tamanhos adequados para cada campo
--    - TEXT para campos sem limite fixo (descrições)
--    - TIMESTAMP para datas com hora
--    - BOOLEAN para flags simples
--
-- 2. CHAVES PRIMÁRIAS:
--    - Todas as tabelas usam chave primária surrogate (id_*)
--    - Autoincremento garante unicidade
--
-- 3. CHAVES ESTRANGEIRAS:
--    - ON DELETE CASCADE: Remove registros dependentes
--    - ON DELETE SET NULL: Mantém registro mas remove referência
--    - ON DELETE RESTRICT: Impede exclusão se houver dependentes
--
-- 4. ÍNDICES:
--    - Criados nas colunas mais usadas em WHERE e JOIN
--    - Balanceamento entre performance de leitura e escrita
--
-- 5. CONSTRAINTS:
--    - CHECK para validar valores de enumerações
--    - UNIQUE para garantir unicidade de campos como email
--    - NOT NULL para campos obrigatórios
--
-- ============================================================
