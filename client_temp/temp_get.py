#
# Descr.: 
# Envia dados de sensor de temperatura para servidor HTTP
# utilizando metodo GET.
#
# Uso:
# $ python ./script.py
#
# Autor:
# Jose G. Faisca
#
#

import requests
from urllib.parse import quote

input_data = '1, 2025-03-21 10:29:39, -10.2, -21.6, 19.7'

# URL encode
data = quote(input_data)

host = "localhost"
port = "9000"

# Pedido GET
url = f"http://{host}:{port}/?data={data}"
response = requests.get(url)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
