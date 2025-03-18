#  Description: Endpoint para adicionar um imóvel ao banco de dados
#  server/api/endpoints/add_imovel.py

from flask import Blueprint, request, jsonify, url_for
from server.db.database import connect_db  # Importando a função de conexão

add_imovel_bp = Blueprint('add_imovel', __name__)

@add_imovel_bp.route('/imoveis', methods=['POST'])
def add_imovel():
    data = request.get_json()

    campos_obrigatorios = ["logradouro", "tipo_logradouro", "bairro", "cidade", "cep", "tipo", "valor", "data_aquisicao"]
    if not all(campo in data for campo in campos_obrigatorios):
        return jsonify({"erro": "Todos os campos são obrigatórios"}), 400

    conn = connect_db()
    if conn is None:
        return jsonify({"erro": "Erro ao conectar ao banco de dados"}), 500

    cursor = conn.cursor()
    query = """
        INSERT INTO imoveis (logradouro, tipo_logradouro, bairro, cidade, cep, tipo, valor, data_aquisicao)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (data["logradouro"], data["tipo_logradouro"], data["bairro"], data["cidade"], 
               data["cep"], data["tipo"], data["valor"], data["data_aquisicao"])

    cursor.execute(query, valores)
    imovel_id = cursor.lastrowid  #Pegando o ID da query recém-criada
    conn.commit()

    conn.close()


    #Gerando o HATEOAS
    links = {'self': url_for('app.view_imovel_by_id.view_imoveis_from_id', id= imovel_id, _external=True),
        'list_all': url_for('app.view_imoveis.view_imoveis',  _external=True),
        'update': url_for('app.update_imovel.update_imovel', id= imovel_id, _external=True),
        'delete': url_for('app.remove_imovel.remove_imovel', imovel_id=imovel_id, _external=True),}
    
    return jsonify({"mensagem": "Imóvel adicionado com sucesso.", "links": links}), 201
