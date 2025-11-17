
# 

---

# Comandos SQL para as operações CRUD

## Tabela Cliente

### Criar (Create)

```sql
INSERT INTO Cliente (NIF, Nome, Morada, CodigoPostal, Localidade, Area, Zona)
VALUES ('512345678', 'Marco S/A', 'Rua das Flores, 123', '1234-567', 'Lisboa', 'Centro', 'A00');
```

### Ler (Read)

```sql
SELECT * FROM Cliente WHERE NIF = '512345678';
```

### Atualizar (Update)

```sql
UPDATE Cliente
SET Morada = 'Avenida da Liberdade, 456', CodigoPostal = '2345-678'
WHERE NIF = '512345678';
```

### Eliminar (Delete)

```sql
DELETE FROM Cliente WHERE NIF = '512345678';
```


## Tabela Equipamento

### Criar (Create)

```sql
INSERT INTO Equipamento (NumeroSerie, Cliente_NIF)
VALUES ('EQ001', '512345678');
```

### Ler (Read)

```sql
SELECT * FROM Equipamento WHERE ID = 1;
```

### Atualizar (Update)

```sql
UPDATE Equipamento
SET NumeroSerie = 'EQ002'
WHERE ID = 1;
```

### Eliminar (Delete)

```sql
DELETE FROM Equipamento WHERE ID = 1;
```


## Tabela Temperatura

### Criar (Create)

```sql
INSERT INTO Temperatura (Equipamento_ID, DataHora, Temp0, Temp1, Temp2)
VALUES (1, '2025-03-21 12:00:00', 22.5, 23.0, 21.8);
```

### Ler (Read)

```sql
SELECT * FROM Temperatura WHERE Equipamento_ID = 1 AND DataHora = '2025-03-21 12:00:00';
```

### Atualizar (Update)

```sql
UPDATE Temperatura
SET Temp0 = 23.0, Temp1 = 23.5, Temp2 = 22.0
WHERE Equipamento_ID = 1 AND DataHora = '2025-03-21 12:00:00';
```

### Eliminar (Delete)

```sql
DELETE FROM Temperatura WHERE Equipamento_ID = 1 AND DataHora = '2025-03-21 12:00:00';
```

