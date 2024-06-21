import json
from flask import Flask, jsonify

app = Flask(__name__)

JSON_FILE = 'data.json'

def load_data():
    try:
        with open(JSON_FILE, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Arquivo {JSON_FILE} não encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo {JSON_FILE}. Formato inválido.")
        return None

@app.route('/')
def get_all():
    data = load_data()
    if data is None:
        return jsonify({"error": "Não foi possível obter os dados"}), 500
    return jsonify(data)

@app.route('/cpf/<cpf>')
def get_by_cpf(cpf):
    data = load_data()
    if data is None:
        return jsonify({"error": "Não foi possível obter os dados"}), 500

    # Garantir que o CPF é tratado como string
    cpf = str(cpf).zfill(11)
    cliente = next((record for record in data if str(record.get('cpf')).zfill(11) == cpf), None)
    if cliente:
        return jsonify(cliente)
    else:
        return jsonify({"error": "CPF não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
