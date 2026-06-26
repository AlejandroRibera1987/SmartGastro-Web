from functools import wraps
from flask import session, jsonify, request
from utils.security import verificar_token

def api_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        token = None

        auth_header = request.headers.get("Authorization")

        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]

        if not token:
            token = session.get("api_token")

        if not token:
            return jsonify({
                "success": False,
                "message": "Token no enviado"
            }), 401

        data = verificar_token(token)

        if not data:
            return jsonify({
                "success": False,
                "message": "Token inválido o vencido"
            }), 401

        return f(*args, **kwargs)

    return decorated_function