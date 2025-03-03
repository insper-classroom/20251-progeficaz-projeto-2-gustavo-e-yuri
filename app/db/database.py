# Description: Módulo de conexão com o banco de dados MySQL.
# app/db/database.py

import mysql.connector
from mysql.connector import Error
from app.api.core.config import Config  # Importa a configuração corretamente

# Conexão com o banco de dados
def connect_db():
    """Estabelece a conexão com o banco de dados usando as configurações fornecidas."""
    try:
        # Passa os parâmetros de conexão diretamente a partir da configuração
        conn = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME,
            port=Config.DB_PORT
        )
        if conn.is_connected():
            return conn
    except Error as err:
        # Em caso de erro, imprime a mensagem de erro
        print(f"Erro: {err}")
        return None
