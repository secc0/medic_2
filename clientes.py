import json
from flask import Blueprint, jsonify

clientes_api = Blueprint('clientes_api', __name__)

# Carregar dados dos clientes do arquivo JSON
with open('clientes.json', 'r') as f:
    clientes = json.load(f)

# Rota para consultar informações do cliente pelo CPF
@clientes_api.route('/cliente/<cpf>', methods=['GET'])
def consultar_cliente(cpf):
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            return jsonify(cliente), 200
    return jsonify({'error': 'Cliente não encontrado'}), 404
