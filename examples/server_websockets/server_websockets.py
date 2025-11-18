#
# Descr.:
# Exemplo de servidor WebSockets.
# A funcao hello gere as conexoes WebSocket recebidas e aguarda uma
# mensagem do cliente, enviando uma resposta de volta.
#
# Uso:
# $ python ./server_websockets.py
#
# Autor:
# Jose G. Faisca
#

import asyncio
import websockets
from websockets import serve

host = "0.0.0.0"
port = 6789

async def hello(websocket):
	client_ip, client_port = websocket.remote_address
	client_net = f"{client_ip}:{client_port}"
	print(f"Cliente conectado: {client_net}")
	try:
		async for in_msg in websocket:
			print(f"{client_net} < {in_msg}")
			out_msg = f"mensage recebida: {in_msg}"
			await websocket.send(out_msg)
			print(f"{client_net} > {out_msg}")
	except websockets.exceptions.ConnectionClosedOK:
		print(f"Conexao terminada normalmennte {client_net}")
	except BrokenPipeError:
		print(f"Broken pipe: {client_net}")	
	except websockets.exceptions.ConnectionClosedError as e:
		print(f"Conexao terminada com erro ({e.code}): {e.reason} - {client_net}")
	except Exception as e:
		print(f"Erro inesperado: {e}")

async def main():
	async with serve(hello, host, port, ping_interval=30, ping_timeout=30):	
		print(f"Servidor iniciado ws://{host}:{port}")
		await asyncio.get_running_loop().create_future()

if __name__ == "__main__":
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		print("Processo interrompido pelo utilizador.")
	finally:
		print("Terminar...") 

