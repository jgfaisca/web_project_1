#!../env_3.11/bin/python
#
# Descr.:
# Criar base de dados e tabelas
#
# Uso:
# $ python ./script.py
#
# Autor:
# Jose G. Faisca
#

import sqlite3
import sys

def create_sqlite_database(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
    PRAGMA journal_mode = WAL;
    PRAGMA cache_size = -2000;
    PRAGMA busy_timeout = 5000;
    PRAGMA synchronous = NORMAL;
    PRAGMA mmap_size = 134217728;
    PRAGMA journal_size_limit = 27103364;

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

    DROP TABLE IF EXISTS Equipamento;
    CREATE TABLE Equipamento (
        ID INTEGER PRIMARY KEY,
        NumeroSerie TEXT,
        Cliente_NIF TEXT,
        FOREIGN KEY (Cliente_NIF) REFERENCES Cliente(NIF)
    );

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
    ''')

    conn.commit()
    conn.close()

def main():
    # create db
    db_name = "../db/test_database.db"
    create_sqlite_database(db_name)   
    # Exit
    sys.exit(0)

if __name__ == "__main__":
    main()
