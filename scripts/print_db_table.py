#!../env_3.11/bin/python
#
# Descr.:
# Imprime tabela da base de dados
#
# Usage:
# $ python ./script.py 
#
# Autor:
# Jose G. Faisca
#
#

import sqlite3
import sys

def print_table_contents(db_name, table_name):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Execute a SELECT query
        cursor.execute(f"SELECT * FROM {table_name}")

        # Fetch all rows
        rows = cursor.fetchall()

        # Get column names
        column_names = [description[0] for description in cursor.description]

        # Print column names
        print(" | ".join(column_names))
        print("-" * (len(" | ".join(column_names))))

        # Print rows
        for row in rows:
            print(" | ".join(str(item) for item in row))

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        if conn:
            conn.close()

def main():
    db_name = "../db/test_database.db"
    table_name = "Cliente"
    print_table_contents(db_name, table_name)
    # Exit
    sys.exit(0)

if __name__ == "__main__":
    main()
