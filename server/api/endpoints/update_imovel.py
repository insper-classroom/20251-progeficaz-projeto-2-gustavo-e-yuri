# Description: Endpoint para atualizar um imóvel existente
# server/api/endpoints/update_imovel.py

from flask import Blueprint, request, jsonify, url_for
from server.db.database import connect_db  # Importando a função de conexão

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
    
        # Recupera o imóvel atualizado para gerar os links HATEOAS
        cursor.execute("SELECT * FROM imoveis WHERE id = %s", (id,))
        imovel = cursor.fetchone()

        if not imovel:
            return jsonify({'erro': 'Erro ao recuperar imóvel atualizado'}), 500
        
                # Converte o resultado para um dicionário
        columns = ["id", "logradouro", "tipo_logradouro", "bairro", "cidade", "cep", "tipo", "valor", "data_aquisicao"]
        imovel_dict = dict(zip(columns, imovel))
        
        #Gerando o HATEOAS
        links = {
            "self": url_for("app.update_imovel.update_imovel", id=id, _external=True),
            "list_all": url_for("app.view_imoveis.view_imoveis", _external=True),
            "view_by_id": url_for("app.view_imovel_by_id.view_imoveis_from_id", id=id, _external=True),
            "delete": url_for("app.remove_imovel.remove_imovel", imovel_id=id, _external=True),
            "filter_by_city": url_for("app.view_imoveis_by_cidade.view_imoveis_by_cidade", cidade=imovel[4], _external=True),
            "filter_by_type": url_for("app.view_imoveis_by_tipo.view_imoveis_by_tipo", tipo=imovel[6], _external=True),
        }

        return jsonify({'mensagem': 'Imóvel atualizado com sucesso', 'links': links, 'imovel_atualizado': imovel_dict}), 200

    except Exception as e:
        conn.rollback()
        return jsonify({'erro': f'Erro ao atualizar imóvel: {str(e)}'}), 500

    finally:
        cursor.close()
        conn.close()
