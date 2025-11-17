#!/bin/bash
#
# Descr.:
# Executar scripts sql (DDL ou DML) a partir de ficheiro 
# em base de dados sqlite  
#
# Dependencias:
# $ sudo apt install sqlite3
# $ sudo apt-get install sqlitebrowser (opcional)
#
# Uso:
# $ ./script.sh <base_dados.db> <ficheiro.sql>
#
# Autor:
# Jose G. Faisca
#
#

# Verificar argumentos
if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <base_dados.db> <ficheiro.sql>"
    exit 1
fi

# Ficheiro base de dados
DB_NAME="$1"

# Ficheiro sql
SQL_FILE="$2"

sqlite3 "$DB_NAME" < "$SQL_FILE"
