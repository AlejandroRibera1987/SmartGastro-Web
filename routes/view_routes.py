from flask import Blueprint, render_template, session, redirect, url_for

view_bp = Blueprint("views", __name__)

@view_bp.route("/dashboard")
def dashboard():
    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    return render_template("dashboard.html")


@view_bp.route("/productos")
def productos():
    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    return render_template("productos.html")

@view_bp.route("/productos/editar/<int:producto_id>")
def editar_producto(producto_id):

    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    return render_template(
        "editar_producto.html",
        producto_id=producto_id
    )