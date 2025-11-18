#
# Descr.:
# Exemplo de cliente WebSockets. 
# A funcao hello conecta-se ao servidor WebSocket e envia uma mensagem.
# De seguida, aguarda e imprime a resposta enviada de volta pelo servidor.
#
# Uso:
# $ python ./client_websockets.py
#
# Autor:
# Jose G. Faisca
#

import asyncio
from websockets import connect
import websockets

host = "localhost"
port = 6789

async def hello():
    uri = f"ws://{host}:{port}"
    try:
        async with connect(uri, ping_interval=30, ping_timeout=30) as websocket:
            while True:
                out_msg = input("mensagem? ")
                if not out_msg:
                    break
                try:
                    await websocket.send(out_msg)
                    print(f"> {out_msg}")
                    in_msg = await websocket.recv()
                    print(f"< {in_msg}")
                except websockets.exceptions.ConnectionClosed:
                    print("Conexao terminada pelo servidor ou rede!")
                    break
                except BrokenPipeError:
                    print("Broken pipe - servidor terminou a conexao.")
                    break
    except Exception as e:
        print(f"Erro: {e}")
    
if __name__ == "__main__":
    asyncio.run(hello())
