# Description: Arquivo de inicialização do pacote de endpoints da API
# app/api/endpoints/__init__.py

from flask import Blueprint
from app.api.endpoints.view_imoveis import view_imoveis_bp
from app.api.endpoints.view_imoveis_from_id import view_imovel_by_id_bp

api_bp = Blueprint('api', __name__)

# Registra todas as rotas disponíveis
api_bp.register_blueprint(view_imoveis_bp, url_prefix='/imoveis')
api_bp.register_blueprint(view_imovel_by_id_bp, url_prefix='/imoveis')
