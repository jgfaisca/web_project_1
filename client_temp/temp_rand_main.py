# 
# Descr.:
# Gera marca temporal (timestamp) e valores alatorios 
# de temperatura e envia para o servidor. 
#
# Uso:
# $ python ./temp_rand_main.py <ID_do_equipamento>
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
import requests

# Definir limite de temperaturas (x e y)
x_0 = -10.00; y_0 = -12.00
x_1 = -20.00; y_1 = -22.00
x_2 =  18.00; y_2 =  20.00

# Definir pausa em segundos (s)
s = 10

# ID do equipmento
equipment_id = None

host = "localhost"
port = "8080"
url = f"http://{host}:{port}/temperatura"

def main():
	try:
		while True:
			# Obter marca temporal (timestamp)
			current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

			# Gerar temperaturas aleatorias
			temp0 = round(random.uniform(x_0, y_0), 1)
			temp1 = round(random.uniform(x_1, y_1), 1)
			temp2 = round(random.uniform(x_2, y_2), 1)

			# Agregar dados a enviar
			input_data = f"{equipment_id},{current_time},{temp0},{temp1},{temp2}"

			# Imprimir dados a enviar
			print(input_data)

			# Enviar dados via metodo POST
			response = requests.post(url, data=input_data)

			# Imprimir resposta 
			print(f"Status Code: {response.status_code}")
			print(f"Response: {response.text}")

			# Pausa
			time.sleep(s)

	# Terminar ciclo
	except KeyboardInterrupt:
		print("Processo interrompido pelo utilizador.")
	finally:
		print("Terminar...")    

if __name__ == "__main__":

	if len(sys.argv) != 2:
		print(f"Uso: python {sys.argv[0]} <ID_do_equipamento>")
		sys.exit(1)
	else:
		equipment_id = sys.argv[1]
		main()
