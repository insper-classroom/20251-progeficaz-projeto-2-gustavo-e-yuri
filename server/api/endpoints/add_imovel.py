#  Description: Endpoint para adicionar um imóvel ao banco de dados
#  app/api/endpoints/add_imovel.py

from flask import Blueprint, request, jsonify
from server.db.database import connect_db  # Importando a função de conexão

add_imovel_bp = Blueprint('add_imovel', __name__)

@add_imovel_bp.route('/add_imovel', methods=['POST'])
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
    conn.commit()
    
    return jsonify({"mensagem": "Imóvel adicionado com sucesso."}), 201
