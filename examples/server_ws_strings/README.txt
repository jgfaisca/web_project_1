API baseada em strings
-------------------------------------------------------------

Descrição:  
O servidor fornece uma API simples para gerir uma lista de itens do tipo string utilizando apenas parâmetros de consulta na URL e respostas em texto simples.

Rotas (Endpoints) da API:

1. GET /items  
   - Retorna: Lista de itens em texto simples, cada item numa nova linha.

2. GET /items/add?item=NOME_DO_ITEM  
   - Adiciona NOME_DO_ITEM à lista de itens.  
   - Exemplo: http://localhost:8000/items/add?item=banana  
   - Retorna: Mensagem de confirmação "Item 'banana' adicionado com sucesso."  
   - Se o parâmetro 'item' estiver em falta, retorna HTTP 400 e mensagem de erro.

3. GET /items/update?index=ÍNDICE&item=NOVONOME  
   - Atualiza o item no índice zero-based ÍNDICE para NOVONOME.  
   - Exemplo: http://localhost:8000/items/update?index=0&item=abacate  
   - Validações:  
       * O ÍNDICE deve ser um número inteiro  
       * O ÍNDICE deve estar dentro do intervalo da lista actual  
       * O parâmetro 'item' deve estar presente  
   - Retorna confirmação ou erro com HTTP 400 para entradas inválidas.

4. GET /items/delete?index=ÍNDICE  
   - Elimina o item no índice ÍNDICE.  
   - Exemplo: http://localhost:8000/items/delete?index=0  
   - Retorna confirmação do item eliminado ou erro se o índice for inválido.

Notas:  
- Use a barra de endereço do browser ou clientes REST para aceder aos URLs e gerir os itens.  
- Exemplo para adicionar um item no browser:  
  http://localhost:8000/items/add?item=laranja  
- Para actualizar ou eliminar, forneça 'index' e 'item' (quando aplicável) como parâmetros de query.  
- As respostas são em texto simples para simplificar.  
- Não é necessário configurar cabeçalhos Content-Type para estas respostas em string.

Limitações:  
- Os dados são armazenados em memória e perdem-se ao reiniciar a aplicação.  
- Não suporta JSON nem métodos POST/PUT.  
- Adequado para casos simples ou para aprender a gestão básica de rotas.

Ferramentas de Teste:  
- Pode testar facilmente escrevendo os URLs directamente no browser.  
- Clientes REST (como RESTED ou Postman) podem ser usados com pedidos GET e parâmetros URL.]

