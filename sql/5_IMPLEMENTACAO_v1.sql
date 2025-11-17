/*
IMPLEMENTAÇÃO
(concretização do modelo físico)

Esta concretização mapeia o modelo físico para um sistema de software específico (SQLite) que será 
utilizado na implementação da base de dados. Define a estrutura das tabelas na base de dados, 
incluindo as chaves primárias, chaves estrangeiras e tipos de dados para cada coluna. 
As relações entre as tabelas são estabelecidas através das chaves estrangeiras, garantindo a 
integridade referencial dos dados.
*/

/* Configurar parâmetros do sistema */
PRAGMA journal_mode = WAL;            -- Ativar o modo de escrita segura
PRAGMA cache_size = -2000;            -- Define o cache para 2MB
PRAGMA busy_timeout = 5000;           -- Define o timeout para 5 segundos
PRAGMA synchronous = NORMAL;          -- Modo de sincronização
PRAGMA mmap_size = 134217728;         -- Tamanho do mapeamento de memória
PRAGMA journal_size_limit = 27103364; -- Limite de tamanho do journal
PRAGMA foreign_keys = ON;             -- Ativar suporte a chaves estrangeiras

DROP TABLE IF EXISTS Cliente;
CREATE TABLE Cliente (
    NIF TEXT PRIMARY KEY NOT NULL,
    Nome TEXT NOT NULL,
    Morada TEXT,
    CodigoPostal TEXT,
    Localidade TEXT,
    Area TEXT,
    Zona TEXT
    CHECK (length(trim(NIF)) > 0 AND length(trim(Nome)) > 0)
);

DROP TABLE IF EXISTS Equipamento;
CREATE TABLE Equipamento (
    ID INTEGER PRIMARY KEY NOT NULL,
    NumeroSerie TEXT NOT NULL,
    Cliente_NIF TEXT NOT NULL,
    FOREIGN KEY (Cliente_NIF) REFERENCES Cliente(NIF) ON DELETE CASCADE,
    CHECK (length(trim(NumeroSerie)) > 0 AND length(trim(Cliente_NIF)) > 0)
);

DROP TABLE IF EXISTS Temperatura;
CREATE TABLE Temperatura (
    Equipamento_ID INTEGER,
    DataHora TIMESTAMP NOT NULL,
    Temp0 REAL,
    Temp1 REAL,
    Temp2 REAL,
    PRIMARY KEY (Equipamento_ID, DataHora),
    FOREIGN KEY (Equipamento_ID) REFERENCES Equipamento(ID) ON DELETE CASCADE,
    CHECK (Temp0 IS NOT NULL OR Temp1 IS NOT NULL OR Temp2 IS NOT NULL) 
);

-- Listar todos os clientes que têm equipamentos associados
CREATE VIEW ClienteEquipamentoView AS
SELECT 
    c.NIF, 
    c.Nome AS NomeCliente, 
    e.ID AS EquipamentoID, 
    e.NumeroSerie
FROM Cliente c
INNER JOIN Equipamento e ON c.NIF = e.Cliente_NIF;

-- Listar todos os clientes que têm equipamentos associados,
-- mostrando leitura de temperaturas 
CREATE VIEW ClienteEquipamentoTemperaturaView AS
SELECT 
    c.NIF, 
    c.Nome AS NomeCliente, 
    e.ID AS EquipamentoID, 
    e.NumeroSerie, 
    t.DataHora, 
    t.Temp0, 
    t.Temp1, 
    t.Temp2
FROM Cliente c
INNER JOIN Equipamento e ON c.NIF = e.Cliente_NIF
INNER JOIN Temperatura t ON e.ID = t.Equipamento_ID;
