
# 

---

# MODELO DE NEGÓCIO

## Sistema de Monitorização e Controlo IoT

Sistema abrangente de Internet das Coisas (IoT) para monitorização e controlo, utilizado em ambientes comerciais, onde é necessário acompanhar condições ambientais e eventos específicos associados a equipamentos instalados em diferentes locais ou clientes.

A estrutura temporal dos dados permite análises detalhadas e acompanhamento histórico das condições e eventos.

### Principais Componentes

#### 1. Gestão de Clientes

- Registo detalhado de clientes, incluindo informações como:
    - NIF
    - Nome
    - Morada
    - Código postal
    - Localidade
    - Área
    - Zona


#### 2. Gestão de Equipamentos

- Cada equipamento é associado a um cliente específico
- Os equipamentos são identificados por:
    - ID único
    - Número de série


#### 3. Monitorização de Temperatura

- Registo contínuo de temperaturas em três pontos diferentes para cada equipamento:
    - Temp0
    - Temp1
    - Temp2
- As leituras são registadas com "timestamp" para análise temporal

