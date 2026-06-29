from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'produtos.json')


# Carrega os dados do json
def carregar_dados():
    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)


# Rota 1, retorna o status da aplicação
@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({
        "nome": "API de Estoque Gerber",
        "versao": "1.0.0",
        "status": "online"
    }), 200


# Rota 2, lista todos os produtos cadatrados
@app.route('/produtos', methods=['GET'])
def get_produtos():
    try:
        dados = carregar_dados()
        return jsonify(dados), 200
    except Exception:
        return jsonify({"erro": "ocorreu um erro inesperado no servidor"}), 500


# Rota 3, busca um produto específico pelo ID
@app.route('/produtos/<int:produto_id>', methods=['GET'])
def get_produto_por_id(produto_id):
    dados = carregar_dados()
    produto = next(
        (p for p in dados if p["id"] == produto_id),
        None
    )

    if produto is None:
        return jsonify({"erro": "Produto não encontrado"}), 404

    return jsonify(produto), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
