
# 

---

# DESENHO CONCEPTUAL

## Modelo Entidade-Relação (MER)

O MER fornece uma representação conceptual da estrutura da base de dados, mostrando as entidades principais, os seus atributos-chave e as relações entre elas.

Num diagrama visual, as entidades, atributos e relações seriam representadas de acordo com alguma das conhecidas notações, tais como as de Peter Chen, ou James Martin. 

### Entidades:

#### EQUIPAMENTO (entidade forte)

- ID (chave primária)
- Número de série


#### CLIENTE (entidade forte)

- NIF (chave primária)
- Nome
- Morada
- Código postal
- Localidade
- Área
- Zona


#### TEMPERATURA (entidade fraca)

- Data e hora
- Temperatura 0
- Temperatura 1
- Temperatura 2


### Relações:

#### POSSUI (entre CLIENTE e EQUIPAMENTO)

- Cardinalidade: 1:N (Um cliente possui vários equipamentos)


#### MEDE_TEMPERATURA (entre EQUIPAMENTO e TEMPERATURA)

- Cardinalidade: 1:N (Um equipamento mede várias temperaturas)


### Notas adicionais:

- As entidades fracas (TEMPERATURA) são identificadas pela sua relação com EQUIPAMENTO e pela data e hora.
- A chave primária de EQUIPAMENTO (ID) é uma chave estrangeira em TEMPERATURA.
- A chave primária de CLIENTE (NIF) é uma chave estrangeira em EQUIPAMENTO.

