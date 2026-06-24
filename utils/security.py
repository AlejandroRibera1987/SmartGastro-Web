from flask_bcrypt import Bcrypt
import jwt
from datetime import datetime, timedelta
from flask import current_app

bcrypt = Bcrypt()

def hash_password(password):
    return bcrypt.generate_password_hash(password).decode("utf-8")

def verify_password(password, password_hash):
    return bcrypt.check_password_hash(password_hash, password)

def generar_token(usuario):
    payload = {
        "usuario_id": usuario.id,
        "usuario": usuario.usuario,
        "rol": usuario.rol,
        "exp": datetime.utcnow() + timedelta(hours=2)
    }

    token = jwt.encode(
        payload,
        current_app.config["SECRET_KEY"],
        algorithm="HS256"
    )

    return token

def verificar_token(token):
    try:
        data = jwt.decode(
            token,
            current_app.config["SECRET_KEY"],
            algorithms=["HS256"]
        )
        return data
    except:
        return None