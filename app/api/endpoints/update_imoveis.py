# Description: Endpoint para atualizar um imóvel existente
# app/api/endpoints/update_imovel.py

from flask import Blueprint, request, jsonify
from app.db.database import connect_db  # Importando a função de conexão

update_imovel_bp = Blueprint('update_imovel', __name__)  # Definindo o Blueprint

@update_imovel_bp.route('/update_imovel/<int:id>', methods=['PUT'])
def update_imovel(id):
    conn = connect_db()  # Conectando ao banco de dados

    if conn is None:
        return jsonify({'erro': 'Erro ao conectar ao banco de dados'}), 500

    data = request.json  # Obtém os dados enviados na requisição

    # Verifica se há dados para atualizar
    if not data:
        return jsonify({'erro': 'Nenhum dado fornecido para atualização'}), 400

    cursor = conn.cursor()

    # Criando a query dinamicamente com base nos campos fornecidos
    set_clause = ', '.join(f"{key} = %s" for key in data.keys())
    values = list(data.values()) + [id]

    query = f"UPDATE imoveis SET {set_clause} WHERE ID = %s"

    try:
        cursor.execute(query, values)
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({'erro': 'Nenhum imóvel encontrado com esse ID'}), 404

        return jsonify({'mensagem': 'Imóvel atualizado com sucesso'}), 200

    except Exception as e:
        conn.rollback()
        return jsonify({'erro': f'Erro ao atualizar imóvel: {str(e)}'}), 500

    finally:
        cursor.close()
        conn.close()
