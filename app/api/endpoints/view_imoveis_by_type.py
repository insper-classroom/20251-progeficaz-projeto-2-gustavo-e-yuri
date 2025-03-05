# Desc: Endpoint para visualização de imóveis por tipo (ex: casa, apartamento, terreno).
# app/api/endpoints/view_imoveis_by_type.py

from flask import Blueprint, request, jsonify
from app.db.database import connect_db

imoveis_bp = Blueprint("imoveis", __name__)

@imoveis_bp.route("/view_imoveis_by_type/<string:tipo>", methods=["GET"])
def view_imoveis_by_type(tipo):
    """
    Retorna a lista de imóveis filtrados por tipo (ex: casa, apartamento, terreno).
    """
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Busca os imóveis com o tipo especificado
        cursor.execute("SELECT * FROM imoveis WHERE tipo = %s", (tipo,))
        imoveis = cursor.fetchall()

        if not imoveis:
            return jsonify({"erro": "Nenhum imóvel encontrado para esse tipo"}), 404

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
