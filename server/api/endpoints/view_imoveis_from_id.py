#  DESC: Endpoint para visualizar um imóvel a partir de um ID
# app/api/endpoints/view_imoveis_from_id.py

from flask import Blueprint, jsonify
from server.db.database import connect_db  # Importando a função de conexão

view_imovel_by_id_bp = Blueprint('view_imovel_by_id', __name__)  # Novo nome para o Blueprint

@view_imovel_by_id_bp.route('/view_imoveis_from_id/<int:id>', methods=['GET'])
def view_imoveis_from_id(id):
    conn = connect_db()  # Conectando ao banco de dados

    if conn is None:
        return jsonify({'erro': 'Erro ao conectar ao banco de dados'}), 500

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM imoveis WHERE ID = %s", (id,))
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
