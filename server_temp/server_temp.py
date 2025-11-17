#
# Descr.:
# Servidor HTTP que recebe dados relativos a temperaturas e 
# regista na tabela 'Temperatura'.
#
# Uso:
# $ python ./script.py
#
# Autor:
# Jose G. Faisca
#

from http.server import HTTPServer, BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse
import sqlite3

# Nome da base de dados
database = '../db/test_database.db'

# Conectar a SQLite db
conn = sqlite3.connect(database, check_same_thread=False)
cursor = conn.cursor()

# Variaveis do servidor
servername = 'server_temp'
host = '0.0.0.0'
port = 9000

def insert_temperature(input_data):
	try:
		data = [x.strip() for x in input_data.strip().split(',')]
		if len(data) != 5:
			return False

		equipment_id, current_time, temp0, temp1, temp2 = data

		cursor.execute('''INSERT INTO Temperatura 
			(Equipamento_ID, DataHora, Temp0, Temp1, Temp2) 
			VALUES (?, ?, ?, ?, ?)''', 
			(equipment_id.strip(), current_time.strip(), 
			float(temp0), float(temp1), float(temp2))
		)
		conn.commit()
		return True
	except Exception as e:
		return False

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

	def send_response_ok(self):    
			self.send_response(200)
			self.send_header('Content-Type', 'text/plain; charset=utf-8')
			self.send_header('Server', servername)
			self.end_headers()
			self.wfile.write(b'Dados inseridos com successo.')

	def send_response_bad_request(self):  
			self.send_response(400)
			self.send_header('Content-Type', 'text/plain; charset=utf-8')
			self.send_header('Server', servername)
			self.end_headers()
			self.wfile.write(b'Formato de dados invalido.')

	def do_POST(self):
			content_length = int(self.headers['Content-Length'])
			post_data = self.rfile.read(content_length).decode('utf-8')                
			self.handle_data(post_data)
			
	def do_GET(self):
			query = urlparse(self.path).query
			params = parse_qs(query)
			get_data = params.get('data', [None])[0]
			if get_data:
				self.handle_data(get_data)
			else:
				self.send_response_bad_request()	

	def handle_data(self, input_data):
			if insert_temperature(input_data):
				self.send_response_ok()
			else:
				self.send_response_bad_request()

def main():			
	httpd = ThreadingHTTPServer((host, port), SimpleHTTPRequestHandler)
	print(f"Servidor a executar em http://{host}:{port}")
	httpd.serve_forever()

if __name__ == "__main__":
    main() 
