from flask import Blueprint, request, jsonify

from middleware.auth_middleware import api_login_required
from services.venta_service import registrar_venta, listar_ventas

venta_bp = Blueprint("ventas_api", __name__)


@venta_bp.route("/api/ventas", methods=["GET"])
@api_login_required
def api_listar_ventas():
    ventas = listar_ventas()

    data = []

    for v in ventas:
        data.append({
            "id": v.id,
            "producto_id": v.producto_id,
            "producto": v.producto.nombre,
            "cantidad": v.cantidad,
            "precio_unitario": v.precio_unitario,
            "total": v.total,
            "fecha": v.fecha.strftime("%d/%m/%Y %H:%M")
        })

    return jsonify({
        "success": True,
        "ventas": data
    })


@venta_bp.route("/api/ventas", methods=["POST"])
@api_login_required
def api_registrar_venta():
    data = request.get_json()

    venta, error = registrar_venta(data)

    if error:
        return jsonify({
            "success": False,
            "message": error
        }), 400

    return jsonify({
        "success": True,
        "message": "Venta registrada correctamente",
        "venta": {
            "id": venta.id,
            "producto_id": venta.producto_id,
            "producto": venta.producto.nombre,
            "cantidad": venta.cantidad,
            "precio_unitario": venta.precio_unitario,
            "total": venta.total,
            "fecha": venta.fecha.strftime("%d/%m/%Y %H:%M")
        }
    }), 201