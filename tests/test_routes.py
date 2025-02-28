import pytest
from servidor import app, connect_db #minha instância do flask
from unittest.mock import patch, MagicMock

@pytest.fixture
def client():
    """Cria um cliente de teste para a API."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
    
@patch("servidor.connect_db") # Substituímos a função que conecta ao banco por um Mock
def test_route_index(mock_connect_db, client):

    # Criamos um Mock para a conexão e o cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    # Configuramos o Mock para retornar o cursor quando chamarmos conn.cursor()
    mock_conn.cursor.return_value = mock_cursor

    # Simulamos o retorno do banco de dados
    mock_cursor.fetchall.return_value = [
        (1, "Nicole Common", "Travessa", 'Lake Danielle', 'Judymouth', '85184', 'casa em condominio', 488423.52, '2017-07-29'),
        (2, 'Price Prairie', 'Travessa', 'Colonton', 'North Garyville', '93354', 'casa em condominio', 260069.89, '2021-11-30'),
        (3, 'Taylor Ranch', 'Avenida', 'West Jennashire', 'Katherinefurt', '51116', 'apartamento', 815969.92, '2020-04-24')
    ]

    # Substituímos a função `connect_db` para retornar nosso Mock em vez de uma conexão real
    mock_connect_db.return_value = mock_conn

    # Fazemos a requisição para a API
    response = client.get("/view_imoveis")

    # Verificamos se o código de status da resposta é 200 (OK)
    assert response.status_code == 200

    # Verificamos se os dados retornados estão corretos
    expected_response = {
  "imoveis": [
    {
      "bairro": "Lake Danielle",
      "cep": "85184",
      "cidade": "Judymouth",
      "data_aquisicao": "2017-07-29",
      "id": 1,
      "logradouro": "Nicole Common",
      "tipo": "casa em condominio",
      "tipo_logradouro": "Travessa",
      "valor": 488423.52
    },
    {
      "bairro": "Colonton",
      "cep": "93354",
      "cidade": "North Garyville",
      "data_aquisicao": "2021-11-30",
      "id": 2,
      "logradouro": "Price Prairie",
      "tipo": "casa em condominio",
      "tipo_logradouro": "Travessa",
      "valor": 260069.89
    },
    {
      "bairro": "West Jennashire",
      "cep": "51116",
      "cidade": "Katherinefurt",
      "data_aquisicao": "2020-04-24",
      "id": 3,
      "logradouro": "Taylor Ranch",
      "tipo": "apartamento",
      "tipo_logradouro": "Avenida",
      "valor": 815969.92
    },]
    }
    assert response.get_json() == expected_response