# Description: Arquivo responsável por criar as rotas da API para a entidade Imóveis.
# app/api/endpoints/view_imoveis.py

from flask import Blueprint, jsonify
from app.db.database import connect_db  # Importando a função de conexão

view_imoveis_bp = Blueprint('view_imoveis', __name__)  # Novo nome para o Blueprint

@view_imoveis_bp.route('/view_imoveis', methods=['GET'])
def view_imoveis():
    conn = connect_db()  # Conectando ao banco de dados

    if conn is None:
        return jsonify({'erro': 'Erro ao conectar ao banco de dados'}), 500

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM imoveis")
    results = cursor.fetchall()

    if not results:
        return jsonify({'erro': 'Nenhum imóvel encontrado.'}), 404

    imoveis = []
    for imovel in results:
        imoveis.append({
            'id': imovel[0],
            'logradouro': imovel[1],
            'tipo_logradouro': imovel[2],
            'bairro': imovel[3],
            'cidade': imovel[4],
            'cep': imovel[5],
            'tipo': imovel[6],
            'valor': imovel[7],
            'data_aquisicao': imovel[8],
        })

    return jsonify({'imoveis': imoveis}), 200
