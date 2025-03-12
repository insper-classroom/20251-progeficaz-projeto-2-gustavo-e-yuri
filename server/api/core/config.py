# Description: Arquivo de configuração da aplicação.
# app/api/core/config.py

import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv('.cred')

class Config:
    """Configurações globais da aplicação."""

    # Carrega as configurações globais
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    SECRET_KEY = os.getenv('SECRET_KEY', 'minha_chave_secreta')

    # Configurações do banco de dados
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_USER = os.getenv('DB_USER')  # Exige que o DB_USER seja definido
    DB_PASSWORD = os.getenv('DB_PASSWORD')  # Exige que o DB_PASSWORD seja definido
    DB_NAME = os.getenv('DB_NAME')  # Exige que o DB_NAME seja definido
    DB_PORT = int(os.getenv('DB_PORT', 19216))  # Usa o valor padrão de 3306 se DB_PORT não for encontrado

    # Validação das variáveis obrigatórias
    if not DB_USER or not DB_PASSWORD or not DB_NAME:
        raise ValueError("As variáveis de ambiente DB_USER, DB_PASSWORD e DB_NAME são obrigatórias.")

config = Config()
