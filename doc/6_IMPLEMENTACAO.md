
# 

---

# IMPLEMENTAÇÃO

(concretização do modelo físico)

Esta concretização mapeia o modelo físico para um sistema de software específico (SQLite) que será utilizado na implementação da base de dados. Define a estrutura das tabelas na base de dados, incluindo as chaves primárias, chaves estrangeiras e tipos de dados para cada coluna. As relações entre as tabelas são estabelecidas através das chaves estrangeiras, garantindo a integridade referencial dos dados.

## Configuração dos parâmetros do sistema

```sql
PRAGMA journal_mode = WAL;            -- Ativar o modo de escrita segura
PRAGMA cache_size = -2000;            -- Define o cache para 2MB
PRAGMA busy_timeout = 5000;           -- Define o timeout para 5 segundos
PRAGMA synchronous = NORMAL;          -- Modo de sincronização
PRAGMA mmap_size = 134217728;         -- Tamanho do mapeamento de memória
PRAGMA journal_size_limit = 27103364; -- Limite de tamanho do journal
```

## Criação das tabelas

### Tabela Cliente

```sql
DROP TABLE IF EXISTS Cliente;
CREATE TABLE Cliente (
    NIF TEXT PRIMARY KEY,
    Nome TEXT,
    Morada TEXT,
    CodigoPostal TEXT,
    Localidade TEXT,
    Area TEXT,
    Zona TEXT
);
```

### Tabela Equipamento

Versão sem AUTOINCREMENT explícito (recomendada):

```sql
DROP TABLE IF EXISTS Equipamento;
CREATE TABLE Equipamento (
    ID INTEGER PRIMARY KEY,
    NumeroSerie TEXT,
    Cliente_NIF TEXT,
    FOREIGN KEY (Cliente_NIF) REFERENCES Cliente(NIF)
);
```

### Tabela Temperatura

```sql
DROP TABLE IF EXISTS Temperatura;
CREATE TABLE Temperatura (
    Equipamento_ID INTEGER,
    DataHora TIMESTAMP,
    Temp0 REAL,
    Temp1 REAL,
    Temp2 REAL,
    PRIMARY KEY (Equipamento_ID, DataHora),
    FOREIGN KEY (Equipamento_ID) REFERENCES Equipamento(ID) 
);
```
