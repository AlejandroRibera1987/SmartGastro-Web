from flask import Blueprint, render_template, session, redirect, url_for

view_bp = Blueprint("views", __name__)

@view_bp.route("/dashboard")
def dashboard():
    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    return render_template("dashboard.html")