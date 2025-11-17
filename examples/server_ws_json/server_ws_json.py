#
# Descr.:
# O servidor fornece uma API RESTful simples para gerir uma lista de itens, 
# utilizando JSON como formato de entrada e saida.
#
# Uso:
# $ python ./server_ws_json.py
#
# Autor:
# Jose G. Faisca
#

from flask import Flask, jsonify, request

app = Flask(__name__)

host = '0.0.0.0'
port = 8000

items = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    items.append(data)
    return jsonify(data), 201

@app.route('/items/<int:index>', methods=['PUT'])
def update_item(index):
    data = request.get_json()
    items[index] = data
    return jsonify(data)

@app.route('/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    item = items.pop(index)
    return jsonify(item)

if __name__ == "__main__":
    app.run(host=host, port=port, debug=True)
 
