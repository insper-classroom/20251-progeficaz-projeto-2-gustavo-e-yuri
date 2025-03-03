# Description: Arquivo de inicialização do pacote de endpoints da API
# app/api/endpoints/__init__.py

from flask import Blueprint
from app.api.endpoints.view_imoveis import view_imoveis_bp

api_bp = Blueprint('api', __name__)

# Registra todas as rotas disponíveis
api_bp.register_blueprint(view_imoveis_bp, url_prefix='/imoveis')
