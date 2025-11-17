

# 

---

# DESENHO FÍSICO

(definição de dados)

Este desenho mapeia o modelo lógico numa visão geral em formato de tabela.
Define a estrutura das tabelas na base de dados, incluindo as chaves primárias e os tipos de dados para cada coluna.
Esta representação ajuda a entender a estrutura da base de dados antes da sua implementação.

## Tabela Cliente

| cid | name | type | notnull | dflt_value | pk |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 0 | NIF | TEXT | 0 |  | 1 |
| 1 | Nome | TEXT | 0 |  | 0 |
| 2 | Morada | TEXT | 0 |  | 0 |
| 3 | CodigoPostal | TEXT | 0 |  | 0 |
| 4 | Localidade | TEXT | 0 |  | 0 |
| 5 | Area | TEXT | 0 |  | 0 |
| 6 | Zona | TEXT | 0 |  | 0 |

## Tabela Equipamento

| cid | name | type | notnull | dflt_value | pk |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 0 | ID | INTEGER | 0 |  | 1 |
| 1 | NumeroSerie | TEXT | 0 |  | 0 |
| 2 | Cliente_NIF | TEXT | 0 |  | 0 |

## Tabela Temperatura

| cid | name | type | notnull | dflt_value | pk |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 0 | Equipamento_ID | INTEGER | 0 |  | 1 |
| 1 | DataHora | TIMESTAMP | 0 |  | 2 |
| 2 | Temp0 | REAL | 0 |  | 0 |
| 3 | Temp1 | REAL | 0 |  | 0 |
| 4 | Temp2 | REAL | 0 |  | 0 |

