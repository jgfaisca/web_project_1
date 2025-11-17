# 
# Descr.:
# Importar ficheiro.csv para tabela 
# em base de dados sqlite  
#
# Uso:
# $ python ./script.py <ficheiro.csv> <base_dados.db> <nome_da_tabela>
#
# Via comando sqlite3:
# $ sqlite3 <base_dados.db>
# sqlite>.mode csv
# sqlite>.import --skip 1 <ficheiro.csv> <nome_da_tabela>;
# sqlite>.q
#
# Autor:
# Jose G. Faisca
#
# 

import csv
import sqlite3
import sys

def import_csv_to_db_table(csv_file, db_file, table_name):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        cursor.execute(f"PRAGMA table_info({table_name})")
        sqlite_columns = [info[1] for info in cursor.fetchall()]
        #print("SQLite columns:", sqlite_columns)

        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            csv_columns = next(reader)
            #print("CSV columns:", csv_columns)

            # Check exact column order match
            if csv_columns != sqlite_columns:
                raise ValueError("CSV columns do not match exactly with SQLite table columns.")

            placeholders = ','.join(['?'] * len(sqlite_columns))
            insert_sql = f"INSERT INTO {table_name} ({', '.join(sqlite_columns)}) VALUES ({placeholders})"

            rows = list(reader)
            print(f"Number of rows to insert: {len(rows)}")

            for row in rows:
                #print("Inserting row:", row)
                cursor.execute(insert_sql, row)

            conn.commit()
            print(f"Data successfully imported into '{table_name}'.")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(3)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print(f"Usage: python {sys.argv[0]} <file.csv> <database.db> <table_name>")
        sys.exit(1)

    csv_file = sys.argv[1]
    db_file = sys.argv[2]
    table_name = sys.argv[3]

    import_csv_to_db_table(csv_file, db_file, table_name)
