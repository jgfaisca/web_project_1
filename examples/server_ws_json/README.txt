Exemplo de API REST JSON
---------------------------------------------------

Descrição:
O servidor fornece uma API RESTful simples para gerir uma lista de itens, utilizando JSON como formato de entrada e saída.

Rotas (Endpoints) da API:

1. GET /items
    - Retorna: Array JSON com todos os itens.
2. POST /items
    - Adiciona um novo item.
    - Necessário: Corpo JSON no pedido POST.
    - Importante: Defina o cabeçalho HTTP:
Content-Type: application/json
    - Exemplo de corpo JSON:
{
"name": "banana",
"price": 1.85
}
    - Retorna: O item adicionado em JSON com status 201.
3. PUT /items/<índice>
    - Atualiza o item no índice (base zero) especificado.
    - Necessário: Corpo JSON com o item atualizado.
    - Mesmo cabeçalho Content-Type do POST.
    - Retorna: Item atualizado em JSON.
4. DELETE /items/<índice>
    - Elimina o item no índice especificado.
    - Retorna: Item eliminado em JSON.

Testes com um cliente Rest (ex: extensão RESTED no Firefox):

- Selecione o método HTTP (GET, POST, PUT, DELETE).
- Indique a URL: p.ex., http://localhost:8000/items ou http://localhost:8000/items/0
- Para POST e PUT:
    - Clique no separador "Headers".
    - Adicione o cabeçalho: Content-Type = application/json
    - Vá ao separador Body.
    - Selecione "Raw" e insira o JSON (exemplo: {"name":"banana","price":2.99}).
- Envie o pedido.
- Receberá a resposta JSON no separador de resposta.

Exemplo de comando curl para POST:

curl -X POST http://localhost:8000/items \
    -H "Content-Type: application/json" \
    -d '{"name":"banana","price":2.99}'


