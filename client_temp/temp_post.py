#!/bin/bash
#
# Descr.: 
# Envia dados de sensor de temperatura para servidor HTTP
# utilizando metodo POST.
#
# Uso:
# $ python ./script.py
#
# Autor:
# Jose G. Faisca
#
#

import requests

host = "localhost"
port = "9000"

url = f"http://{host}:{port}"
input_data = "3, 2025-03-21 10:21:59, -10.2, -21.6, 19.7"

response = requests.post(url, data=input_data)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
