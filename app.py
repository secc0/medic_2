import json
from flask import Flask, jsonify

app = Flask(__name__)

# Caminho para o arquivo JSON local
JSON_FILE = 'data.json'

def load_data():
    """Função para carregar os dados do arquivo JSON."""
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

# Endpoint para retornar todo o banco de dados
@app.route('/')
def get_all():
    data = load_data()
    if data is None:
        return jsonify({"error": "Não foi possível obter os dados"}), 500
    return jsonify(data)

# Endpoint para retornar dados de um CPF específico
@app.route('/cpf/<cpf>')
def get_by_cpf(cpf):
    data = load_data()
    if data is None:
        return jsonify({"error": "Não foi possível obter os dados"}), 500

    # Convertendo os CPFs armazenados em strings para comparação
    cliente = next((record for record in data if str(record.get('cpf')) == cpf), None)
    if cliente:
        return jsonify(cliente)
    else:
        return jsonify({"error": "CPF não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
