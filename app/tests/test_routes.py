# Description: Testes de integração para as rotas da API
# app/tests/test_routes.py

import pytest
from main import app  # Sua instância do Flask
from unittest.mock import patch, MagicMock

@pytest.fixture
def client():
    """Cria um cliente de teste para a API."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@patch("app.db.database.connect_db")  # O caminho correto para a função a ser mockada
def test_route_view_imoveis(mock_connect_db, client):
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
                "id": 1,
                "logradouro": "Nicole Common",
                "tipo_logradouro": "Travessa",
                "bairro": "Lake Danielle",
                "cidade": "Judymouth",
                "cep": "85184",
                "tipo": "casa em condominio",
                "valor": 488423.52,
                "data_aquisicao": "2017-07-29"
            },
            {
                "id": 2,
                "logradouro": "Price Prairie",
                "tipo_logradouro": "Travessa",
                "bairro": "Colonton",
                "cidade": "North Garyville",
                "cep": "93354",
                "tipo": "casa em condominio",
                "valor": 260069.89,
                "data_aquisicao": "2021-11-30"
            },
            {
                "id": 3,
                "logradouro": "Taylor Ranch",
                "tipo_logradouro": "Avenida",
                "bairro": "West Jennashire",
                "cidade": "Katherinefurt",
                "cep": "51116",
                "tipo": "apartamento",
                "valor": 815969.92,
                "data_aquisicao": "2020-04-24"
            }
        ]
    }
    
    # Asserção para comparar o JSON retornado com o esperado
    assert response.get_json() == expected_response

@patch("app.db.database.connect_db")  # O caminho correto para a função a ser mockada
def test_route_view_imoveis_from_id(mock_connect_db, client):
    # Criamos um Mock para a conexão e o cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    # Configuramos o Mock para retornar o cursor quando chamarmos conn.cursor()
    mock_conn.cursor.return_value = mock_cursor

    # Simulamos o retorno do banco de dados para o ID 1
    mock_cursor.fetchall.return_value = [
        (1, "Nicole Common", "Travessa", 'Lake Danielle', 'Judymouth', '85184', 'casa em condominio', 488423.52, '2017-07-29')
    ]

    # Substituímos a função `connect_db` para retornar nosso Mock em vez de uma conexão real
    mock_connect_db.return_value = mock_conn

    # Fazemos a requisição para a API
    response = client.get("/view_imoveis_from_id/1")

    # Verificamos se o código de status da resposta é 200 (OK)
    assert response.status_code == 200

    # Verificamos se os dados retornados estão corretos
    expected_response = {
        "imoveis": [
            {
                "id": 1,
                "logradouro": "Nicole Common",
                "tipo_logradouro": "Travessa",
                "bairro": "Lake Danielle",
                "cidade": "Judymouth",
                "cep": "85184",
                "tipo": "casa em condominio",
                "valor": 488423.52,
                "data_aquisicao": "2017-07-29"
            }
        ]
    }

    # Asserção para comparar o JSON retornado com o esperado
    assert response.get_json() == expected_response

@patch("app.db.database.connect_db")
def test_route_add_imovel(mock_connect_db, client):
    # Criamos um Mock para a conexão e o cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    # Configuramos o Mock para retornar o cursor quando chamarmos conn.cursor()
    mock_conn.cursor.return_value = mock_cursor

    # Substituímos a função `connect_db` para retornar nosso Mock em vez de uma conexão real
    mock_connect_db.return_value = mock_conn

    # Dados para adicionar um imóvel
    new_imovel = {
        "logradouro": "Rua Exemplo",
        "tipo_logradouro": "Avenida",
        "bairro": "Centro",
        "cidade": "São Paulo",
        "cep": "01000-000",
        "tipo": "apartamento",
        "valor": 500000.00,
        "data_aquisicao": "2024-03-01"
    }

    # Fazemos a requisição `POST` para a API
    response = client.post("/add_imovel", json=new_imovel)

    # Verificamos se o código de status da resposta é 201 (Created)
    assert response.status_code == 201

    # Verificamos se os dados retornados estão corretos
    expected_response = {
        "mensagem": "Imóvel adicionado com sucesso."
    }
    assert response.get_json() == expected_response

    # Certificamos que o método `execute` foi chamado com o SQL correto
    mock_cursor.execute.assert_called_once_with(
        """
        INSERT INTO imoveis (logradouro, tipo_logradouro, bairro, cidade, cep, tipo, valor, data_aquisicao)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            "Rua Exemplo",
            "Avenida",
            "Centro",
            "São Paulo",
            "01000-000",
            "apartamento",
            500000.00,
            "2024-03-01",
        ),
    )

    # Certificamos que o método `commit` foi chamado
    mock_conn.commit.assert_called_once()
