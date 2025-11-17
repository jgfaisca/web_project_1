Exemplo de persistencia de dados em ambiente Web
---------------------------------------------------

Este exemplo fornece rotas para leitura e gravação de mensagens persistentes utilizando cookies, localStorage (no browser) e server-side por intermédio de um ficheiro JSON.

Descrição

  - Uso da Pasta Templates:
    O ficheiro da página HTML (`message_local_storage.html`) é colocado na pasta `templates` e renderizado usando a função `render_template` do Flask.
  - Definição de Cookie:
    A rota `/set_cookie` aceita requisições GET ou POST para definir um cookie designado `message`. O cookie pode ser lido utilizando a rota `/read_cookie`.
  - Persistência Server-Side:
    A rota `/message_server_side` permite requisições GET e POST para armazenar e recuperar uma mensagem guardada num ficheiro JSON (`message_store.json`), garantindo que os dados continuarão disponíveis após reinicio do servidor.
  - Funcionalidade LocalStorage:
    A rota `/message_local_storage` serve uma página HTML que permite ao utilizador armazenar e ler uma mensagem no localStorage do browser via JavaScript.

Utilização

1. Iniciar o servidor:

	$ python server_storage.py

2. Armazenar/consultar uma mensagem via cookie no browser

	Utilizar o URL 'http://localhost:8000/set_cookie?message=test'
	Utilizar o URL 'http://localhost:8000/read_cookie'

2.2 Armazenar/consultar uma mensagem via cookie utilizando o comando curl

    $ curl -v -c cookies.txt "http://localhost:8000/set_cookie?message=test"
    $ curl -v -b cookies.txt "http://localhost:8000/read_cookie"

3. Armazenar/Recuperar mensagem via ficheiro no servidor.

	POST:
	$ curl -X POST -d "message=teste" http://localhost:8000/message_server_side

	GET:
	$ curl http://localhost:8000/message_server_side

4. Utilizar o LocalStorage no browser.
    - Aceder ao URL `http://localhost:8000/message_local_storage` no browser e digitar a mensagem. 
    - Clique em "Save" para gravar no LocalStorage.
