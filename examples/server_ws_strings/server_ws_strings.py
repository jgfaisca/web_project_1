#
# Descr.:
# O servidor fornece uma API simples para gerir uma lista de itens do tipo string utilizando 
# apenas parâmetros de consulta na URL e respostas em texto simples.
#
# Uso:
# $ python ./server_ws_strings.py
#
# Autor:
# Jose G. Faisca
#

from flask import Flask, request

app = Flask(__name__)

host = '0.0.0.0'
port = 8000

items = []

@app.route('/items', methods=['GET'])
def get_items():
    return "<br>".join(items) or "No items found."

@app.route('/items/add', methods=['GET'])
def add_item():
    item = request.args.get('item')
    if item:
        items.append(item)
        return f"Item '{item}' added successfully."
    else:
        return "Please provide an 'item' parameter in the URL.", 400

@app.route('/items/update', methods=['GET'])
def update_item():
    index = request.args.get('index', type=int)
    new_item = request.args.get('item')
    if index is None or new_item is None or index < 0 or index >= len(items):
        return "Invalid index or missing new item.", 400
    items[index] = new_item
    return f"Item at index {index} updated to '{new_item}'."

@app.route('/items/delete', methods=['GET'])
def delete_item():
    index = request.args.get('index', type=int)
    if index is None or index < 0 or index >= len(items):
        return "Invalid index.", 400
    removed = items.pop(index)
    return f"Item '{removed}' at index {index} deleted."

if __name__ == "__main__":
    app.run(host=host, port=port, debug=True)
