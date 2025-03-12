# Description: Arquivo de inicialização do pacote de endpoints da API
# server/api/endpoints/__init__.py

from flask import Blueprint
from server.api.endpoints.view_imoveis import view_imoveis_bp
from server.api.endpoints.view_imoveis_from_id import view_imovel_by_id_bp
from server.api.endpoints.add_imovel import add_imovel_bp
from server.api.endpoints.update_imovel import update_imovel_bp
from server.api.endpoints.remove_imovel import remove_imovel_bp
from server.api.endpoints.view_imoveis_by_tipo import view_imoveis_by_tipo_bp
from server.api.endpoints.view_imoveis_by_cidade import view_imoveis_by_cidade_bp

api_bp = Blueprint('app', __name__)

# Registra todas as rotas disponíveis
api_bp.register_blueprint(view_imoveis_bp, url_prefix='')
api_bp.register_blueprint(view_imovel_by_id_bp, url_prefix='')
api_bp.register_blueprint(add_imovel_bp, url_prefix='')
api_bp.register_blueprint(update_imovel_bp, url_prefix='')
api_bp.register_blueprint(remove_imovel_bp, url_prefix='')
api_bp.register_blueprint(view_imoveis_by_tipo_bp, url_prefix='')
api_bp.register_blueprint(view_imoveis_by_cidade_bp, url_prefix='')