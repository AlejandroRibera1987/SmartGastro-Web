from flask import Flask
from config import Config
from database.db import db
from utils.security import bcrypt, hash_password
from flask import redirect, url_for, session
from models.usuario import Usuario
from models.producto import Producto
from models.venta import Venta

from routes.auth_routes import auth_bp
from routes.view_routes import view_bp
from routes.producto_routes import producto_bp
from routes.venta_routes import venta_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
bcrypt.init_app(app)

app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(view_bp)
app.register_blueprint(producto_bp)
app.register_blueprint(venta_bp)

with app.app_context():
    db.create_all()

    admin = Usuario.query.filter_by(usuario="admin").first()

    if not admin:
        admin = Usuario(
            usuario="admin",
            password_hash=hash_password("123456"),
            rol="admin"
        )

        db.session.add(admin)
        db.session.commit()
        print("Usuario admin creado")

@app.route("/")
def home():
    if "usuario_id" in session:
        return redirect(url_for("views.dashboard"))

    return redirect(url_for("auth.login"))


with app.app_context():
    db.create_all()

    admin = Usuario.query.filter_by(usuario="admin").first()

    if not admin:
        admin = Usuario(
            usuario="admin",
            password_hash=hash_password("123456"),
            rol="admin"
        )

        db.session.add(admin)
        db.session.commit()
        print("Usuario admin creado")


if __name__ == "__main__":
    app.run(debug=True)
