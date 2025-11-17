#!/bin/bash

BASE_URL="http://localhost:8080"

# POST example - sending form data with explicit Content-Type header
curl -X POST ${BASE_URL}/equipamento \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "numero_serie=ABC6543" \
     -d "cliente_nif=PT549108661"

# GET example - listing all equipment
curl ${BASE_URL}/listar_equipamentos

# POST example - sending form data with explicit Content-Type header
curl -X POST ${BASE_URL}/equipamento/json \
     -H "Content-Type: application/json" \
     -d '{"numero_serie": "ABC6543", "cliente_nif": "PT549108661"}'

# GET example - listing all equipment
curl ${BASE_URL}/listar_equipamentos/json
