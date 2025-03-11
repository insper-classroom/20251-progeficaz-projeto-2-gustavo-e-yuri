# Description: Remove um imóvel do banco de dados pelo ID.
# app/api/endpoints/remove_imovel.py

from flask import Blueprint, request, jsonify
from server.db.database import connect_db

remove_imovel_bp = Blueprint("remove_imovel", __name__)

@remove_imovel_bp.route("/remove_imovel/<int:imovel_id>", methods=["DELETE"])
def remove_imovel(imovel_id):
    """
    Remove um imóvel do banco de dados pelo ID.
    """
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Verifica se o imóvel existe antes de deletar
        cursor.execute("SELECT * FROM imoveis WHERE id = %s", (imovel_id,))
        imovel = cursor.fetchone()

        if not imovel:
            return jsonify({"erro": "Imóvel não encontrado"}), 404

        # Executa a remoção
        cursor.execute("DELETE FROM imoveis WHERE id = %s", (imovel_id,))
        conn.commit()

        return jsonify({"mensagem": "Imóvel removido com sucesso"}), 200

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

    finally:
        cursor.close()
        conn.close()
