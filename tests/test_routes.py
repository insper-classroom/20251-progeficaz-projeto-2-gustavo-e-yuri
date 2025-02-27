import pytest

from servidor import app #minha instância do flask

@pytest.fixture
def client():
    with app.test_client() as client:  # cria o cliente de teste
        yield client 
    
def test_index(client):
    """ Teste a rota 'index' """
    response = client.get('/')  # faz uma requisição para '/'
    assert response.status_code == 200  # verifica se deu tudo certo
    assert response.json['message'] == "Index"  # verifica o json que eu mandei 