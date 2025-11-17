import requests

# Base server URL
BASE_URL = "http://localhost:8080"

# POST example - inserting new equipment
payload = {
    "numero_serie": "ABC6543",
    "cliente_nif": "PT549108661"
    # "id": 10  # optional
}

response = requests.post(f"{BASE_URL}/equipamento/json", json=payload)
print("POST Status Code:", response.status_code)
print("Response:", response.json())

# GET example - listing all equipment
response = requests.get(f"{BASE_URL}/listar_equipamentos/json")
print("GET Status Code:", response.status_code)
print("Equipamentos:", response.json())
