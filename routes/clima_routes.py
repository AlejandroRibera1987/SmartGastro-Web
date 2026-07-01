from flask import Blueprint, jsonify
from middleware.auth_middleware import api_login_required
from services.clima_service import obtener_clima_actual

clima_bp = Blueprint("clima_api", __name__)

@clima_bp.route("/api/clima", methods=["GET"])
@api_login_required
def api_clima():
    clima, error = obtener_clima_actual()

    if error:
        return jsonify({
            "success": False,
            "message": error
        }), 400

    return jsonify({
        "success": True,
        "clima": clima
    })