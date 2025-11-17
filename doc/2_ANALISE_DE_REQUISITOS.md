
# 

---

# ANÁLISE DE REQUISITOS

Esta análise fornece uma visão geral da estrutura da base de dados, identificando as principais entidades, os seus atributos, as relações entre elas e algumas restrições.

## 1. Entidades

- Equipamento
- Cliente
- Temperatura


## 2. Atributos/Propriedades

### Equipamento:

- ID (identificador único)
- Número de série
- Cliente associado (NIF do cliente)


### Cliente:

- NIF (Número de Identificação Fiscal)
- Nome
- Morada
- Código postal
- Localidade
- Área
- Zona


### Temperatura:

- ID do equipamento
- Data e hora
- Temperatura 0
- Temperatura 1
- Temperatura 2


## 3. Relações (e propriedades)

- **Equipamento - Cliente:** Um cliente pode ter vários equipamentos, mas cada equipamento pertence a apenas um cliente.
- **Equipamento - Temperatura:** Um equipamento pode ter vários registos de temperatura, mas cada registo de temperatura está associado a apenas um equipamento.


## 4. Restrições (oriundas de regras de negócio)

- O NIF do cliente deve ser único e válido (12 dígitos).
- O número de série do equipamento deve ser único.
- As datas e horas devem ser válidas e não podem ser futuras.
- As temperaturas devem estar dentro de um intervalo razoável (por exemplo, entre -30°C e 100°C).
- Todos os IDs de equipamento referenciados devem existir na tabela de equipamentos.
- Todos os NIFs de clientes referenciados na tabela de equipamentos devem existir na tabela de clientes.

