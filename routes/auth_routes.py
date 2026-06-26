from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from models.usuario import Usuario
from utils.security import verify_password, generar_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        password = request.form.get("password")

        user = Usuario.query.filter_by(usuario=usuario).first()

        if user and verify_password(password, user.password_hash):
            from utils.security import generar_token

            token = generar_token(user)

            session["usuario_id"] = user.id
            session["usuario"] = user.usuario
            session["rol"] = user.rol
            session["api_token"] = token

            return redirect(url_for("views.dashboard"))

        flash("Usuario o contraseña incorrectos")
        return render_template("login.html")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))

@auth_bp.route("/token", methods=["POST"])
def api_login_token():

    data = request.get_json()

    usuario = data.get("usuario")
    password = data.get("password")

    user = Usuario.query.filter_by(
        usuario=usuario
    ).first()

    if not user:
        return jsonify({
            "success": False,
            "message": "Usuario incorrecto"
        }), 401

    if not verify_password(
        password,
        user.password_hash
    ):
        return jsonify({
            "success": False,
            "message": "Contraseña incorrecta"
        }), 401

    token = generar_token(user)

    return jsonify({
        "success": True,
        "token": token
    })