#
# Descr.:
# Exemplo de servidor que possibilita persistencia de dados no browser via Cookie 
# e LocalStorage, ou ficheiro localizado no servidor.
#
# Uso:
# $ python ./server_storage.py
#
# Autor:
# Jose G. Faisca
#

from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)
host = '0.0.0.0'
port = 8000
FILE_PATH = 'message_store.json'

@app.route('/set_cookie', methods=['GET', 'POST'])
def set_cookie():
    msg = request.args.get('message') or request.form.get('message') or 'default-cookie-value'
    resp = jsonify({'status': 'ok', 'message': msg})
    resp.set_cookie('message', msg)
    return resp

@app.route('/read_cookie')
def read_cookie():
    cookie_value = request.cookies.get('message', '(none)')
    return jsonify({'message': cookie_value})

@app.route('/message_local_storage')
def index():
    return render_template('message_local_storage.html')

def load_message():
    if os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {"message": None}
    return {"message": None}

def save_message(msg_dict):
    with open(FILE_PATH, 'w') as f:
        json.dump(msg_dict, f)

@app.route('/message_server_side', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        msg = request.form.get('message')
        if not msg:
            data = request.get_json(silent=True)
            if data:
                msg = data.get('message')
        if msg:
            save_message({"message": msg})
            return jsonify({'status': 'ok', 'message': msg}), 200
        else:
            return jsonify({'error': 'no message provided'}), 400
    else:
        stored = load_message()
        return jsonify({'message': stored.get("message") or "(none)"}), 200

if __name__ == "__main__":
    app.run(host=host, port=port, debug=True)

