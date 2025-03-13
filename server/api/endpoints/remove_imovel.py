# Description: Remove um imóvel do banco de dados pelo ID.
# server/api/endpoints/remove_imovel.py

from flask import Blueprint, request, jsonify, url_for
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


        #Gerando o HATEOAS
        links = {
            "list_all": url_for("app.view_imoveis.view_imoveis", _external=True),
            "add": url_for("app.add_imovel.add_imovel", _external=True),
            "filter_by_city": url_for("app.view_imoveis_by_cidade.view_imoveis_by_cidade", cidade=imovel[4], _external=True),
            "filter_by_type": url_for("app.view_imoveis_by_tipo.view_imoveis_by_tipo", tipo=imovel[6], _external=True),
        }

        return jsonify({"mensagem": "Imóvel removido com sucesso", 'links': links}), 200

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

    finally:
        cursor.close()
        conn.close()
