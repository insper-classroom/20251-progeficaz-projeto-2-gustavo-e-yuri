# Description: Arquivo principal da aplicação, onde é criado o app e as rotas são registradas.
# app/main.py

from flask import Flask
from server.api.endpoints import api_bp  # Importa os Blueprints
from server.api.core.config import Config  # Importa a configuração global
import logging

def create_app():
    # Cria a aplicação Flask
    app = Flask(__name__)
    
    # Configura as configurações globais (ex: chave secreta, debug, etc.)
    app.config.from_object(Config)
    
    # Registra o blueprint com prefixo '/api'
    app.register_blueprint(api_bp, url_prefix='/api')

    # Configurações de logging
    logging.basicConfig(level=logging.DEBUG)  # Registra todos os logs com nível DEBUG ou superior

    return app

app = create_app()

if __name__ == '__main__':
    # Executa a aplicação no modo de desenvolvimento
    app.run(debug=True)