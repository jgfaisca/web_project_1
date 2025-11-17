# 
# Descr.:
# Executar scripts sql a partir de ficheiro 
# em base de dados sqlite  
#
# Uso:
# $ python ./script.py <base_dados.db> <ficheiro.sql>
#
# Via comando sqlite3:
# $ sqlite3 <base_dados.db> < <ficheiro.sql>
#
# Autor:
# Jose G. Faisca
#

import sqlite3
import sys

def execute_schema(database_name, sql_file):
    try:
        # Conectar a base de dados SQLite
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        # Ler conteudo do ficheiro .sql
        with open(sql_file, 'r') as file:
            schema_sql = file.read()

        # Executar os comandos SQL do ficheiro sql
        cursor.executescript(schema_sql)
        print(f"Script '{sql_file}' executado com sucesso na base de dados '{database_name}'.")
        
        # Confirmar e terminar conexao
        conn.commit()
    except Exception as e:
        print(f"Erro ao executar: {e}")
        sys.exit(1)
    finally:
        if conn:
           conn.close()

if __name__ == "__main__":
	
    if len(sys.argv) != 3:
        print(f"Uso: python {sys.argv[0]} <base_dados.db> <ficheiro.sql>")
    else:
        database_name = sys.argv[1]
        sql_file = sys.argv[2]
        execute_schema(database_name, sql_file)
