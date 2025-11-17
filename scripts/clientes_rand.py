#
# Descr.:
# Gera ficheiro .csv com valores aleatorios da tabela 'Cliente'.
#
# Uso:
# $ python ./script.py
#
# Autor:
# Jose G. Faisca
#

import random
from faker import Faker
import csv

# Configurar o Faker para português de Portugal
fake = Faker('pt_PT')

# Lista de zonas 
zonas = ['B10', 'A10', 'C01', 'C10', 'B08', 'D00', 'A06', 'D05', 'C09']
areas = [
    'Centro', 'Centro Histórico', 'Centro Comercial', 'Zona Comercial',
    'Periferia', 'Zona Residencial', 'Área Metropolitana', 'Centro Empresarial'
]

# Gerar n clientes aleatórios
n = 12
clientes = []
for _ in range(n):
    # Gerar NIF que começa com 5
    nif = '5' + ''.join([str(random.randint(0, 9)) for _ in range(7)])
    # Cálculo do dígito de controlo (módulo 11)
    soma = sum(int(nif[i]) * (9 - i) for i in range(8))
    resto = soma % 11
    if resto == 0 or resto == 1:
        digito_controlo = 0
    else:
        digito_controlo = 11 - resto
    nif += str(digito_controlo)
    nif = "PT" + nif

    cliente = {
        'NIF': nif,
        'Nome': fake.company(),
        'Morada': fake.street_address(),
        'CodigoPostal': fake.postcode(),
        'Localidade': fake.city(),
        'Area': random.choice(areas), 
        'Zona': random.choice(zonas)
    }
    clientes.append(cliente)

# Escrever resultados em ficheiro CSV
with open('clientes.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['NIF', 'Nome', 'Morada', 'CodigoPostal', 
    'Localidade', 'Area', 'Zona'],quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for cliente in clientes:
        writer.writerow(cliente)
        
print("Ficheiro CSV 'clientes.csv' gerado com sucesso.")
