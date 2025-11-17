# 
# Descr.:
# Gera marca temporal (timestamp) e valores alatorios de temperatura 
# e esrever para tabela 'Temperatura' na base de dados. 
#
# Uso:
# $ python ./temp_rand_db.py <ID_do_equipamento>
#
# Autor:
# Jose G. Faisca
#
#

import sys
import random
import time
import sqlite3
from datetime import datetime

# Nome da base de dados
database = '../db/test_database.db'

# Definir limite de temperaturas (x e y)
x_0 = -10.00; y_0 = -12.00
x_1 = -20.00; y_1 = -22.00
x_2 =  18.00; y_2 =  20.00

# Definir pausa em segundos (s)
s = 10

# ID do equipmento
equipment_id = None

def main():
	try:
		# Conectar a SQLite db
		conn = sqlite3.connect(database)
		cursor = conn.cursor()

		while True:
			# Obter marca temporal (timestamp)
			current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			
			# Gerar temperaturas aleatorias
			temp0 = round(random.uniform(x_0, y_0), 1)
			temp1 = round(random.uniform(x_1, y_1), 1)
			temp2 = round(random.uniform(x_2, y_2), 1)
			
			# Inserir dados na bd
			cursor.execute('''INSERT INTO Temperatura 
			     (Equipamento_ID, DataHora, Temp0, Temp1, Temp2) 
			     VALUES (?, ?, ?, ?, ?)''', 
			     (equipment_id, current_time, 
			     temp0, temp1, temp2)
			)
			
			# Executar commit
			conn.commit()
				
			# Imprimir dados inseridos na bd 
			print(f"{equipment_id}, {current_time}, {temp0}, {temp1}, {temp2}")
			
			# Pausa
			time.sleep(s)

	# Terminar conexao
	except KeyboardInterrupt:
		print("Processo interrompido pelo utilizador.")
	finally:
		cursor.close()
		conn.close()
		print("Conexao terminada.")    

if __name__ == "__main__":

	if len(sys.argv) != 2:
		print(f"Uso: python {sys.argv[0]} <ID_do_equipamento>")
		sys.exit(1)
	else:
		equipment_id = sys.argv[1]
		main()
