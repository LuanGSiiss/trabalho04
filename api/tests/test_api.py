import pytest
from api.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Teste 1, retorno HTTP 200 para a rota GET /produtos
def test_get_produtos_status_200(client):
    resposta = client.get('/produtos')
    assert resposta.status_code == 200

# Teste 2, valida a estrutura do JSON retornado
def test_get_produtos_estrutura_json(client):
    resposta = client.get('/produtos')
    dados = resposta.get_json()
    assert isinstance(dados, list)
    assert len(dados) >= 10
    # verifica se os atributos obrigatórios estão presentes
    assert "id" in dados[0]
    assert "nome" in dados[0]
    assert "preco" in dados[0]

# Teste 3, testa quando informado um identificador inexistente
def test_get_produto_inexistente_404(client):
    resposta = client.get('/produtos/9999')
    assert resposta.status_code == 404

# Teste 4, testa a rota de "/status"
def test_get_status_aplicacao(client):
    resposta = client.get('/status')
    dados = resposta.get_json()
    assert resposta.status_code == 200
    assert dados["status"] == "online"
    assert "versao" in dados