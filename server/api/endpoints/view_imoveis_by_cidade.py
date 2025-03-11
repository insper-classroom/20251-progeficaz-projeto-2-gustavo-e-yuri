# Description: Endpoint para visualização de imóveis por cidade.
# app/api/endpoints/view_imoveis_by_city.py

from flask import Blueprint, jsonify
from server.db.database import connect_db

view_imoveis_by_cidade_bp = Blueprint("view_imoveis_by_cidade", __name__)

@view_imoveis_by_cidade_bp.route("/view_imoveis_by_cidade/<string:cidade>", methods=["GET"])
def view_imoveis_by_cidade(cidade):
    """
    Retorna a lista de imóveis filtrados por cidade.
    """
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Busca os imóveis com a cidade especificada
        cursor.execute("SELECT * FROM imoveis WHERE cidade = %s", (cidade,))
        imoveis = cursor.fetchall()

        if not imoveis:
            return jsonify({"erro": "Nenhum imóvel encontrado para essa cidade"}), 404

        # Estruturamos os imóveis em uma lista de dicionários
        imoveis_list = [
            {
                "id": row[0],
                "logradouro": row[1],
                "tipo_logradouro": row[2],
                "bairro": row[3],
                "cidade": row[4],
                "cep": row[5],
                "tipo": row[6],
                "valor": row[7],
                "data_aquisicao": row[8],
            }
            for row in imoveis
        ]

        return jsonify({"imoveis": imoveis_list}), 200

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

    finally:
        cursor.close()
        conn.close()
