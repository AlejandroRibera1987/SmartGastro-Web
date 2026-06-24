from flask import Blueprint, request, jsonify

from middleware.auth_middleware import api_login_required
from services.producto_service import (
    listar_productos,
    crear_producto,
    actualizar_producto,
    eliminar_producto,
    cambiar_estado_producto
)

producto_bp = Blueprint("productos_api", __name__)


@producto_bp.route("/api/productos", methods=["GET"])
@api_login_required
def api_listar_productos():
    productos = listar_productos()

    data = []

    for p in productos:
        data.append({
            "id": p.id,
            "nombre": p.nombre,
            "descripcion": p.descripcion,
            "precio": p.precio,
            "stock": p.stock,
            "activo": p.activo
        })

    return jsonify({
        "success": True,
        "productos": data
    })


@producto_bp.route("/api/productos", methods=["POST"])
@api_login_required
def api_crear_producto():
    data = request.get_json()

    producto, error = crear_producto(data)

    if error:
        return jsonify({
            "success": False,
            "message": error
        }), 400

    return jsonify({
        "success": True,
        "message": "Producto creado correctamente",
        "producto": {
            "id": producto.id,
            "nombre": producto.nombre,
            "descripcion": producto.descripcion,
            "precio": producto.precio,
            "stock": producto.stock,
            "activo": producto.activo
        }
    }), 201


@producto_bp.route("/api/productos/<int:producto_id>", methods=["PUT"])
@api_login_required
def api_actualizar_producto(producto_id):
    data = request.get_json()

    producto, error = actualizar_producto(producto_id, data)

    if error:
        return jsonify({
            "success": False,
            "message": error
        }), 404

    return jsonify({
        "success": True,
        "message": "Producto actualizado correctamente",
        "producto": {
            "id": producto.id,
            "nombre": producto.nombre,
            "descripcion": producto.descripcion,
            "precio": producto.precio,
            "stock": producto.stock,
            "activo": producto.activo
        }
    })



@producto_bp.route("/api/productos/<int:producto_id>", methods=["DELETE"])
@api_login_required
def api_eliminar_producto(producto_id):
    eliminado, error = eliminar_producto(producto_id)

    if error:
        return jsonify({
            "success": False,
            "message": error
        }), 404

    return jsonify({
        "success": True,
        "message": "Producto eliminado correctamente"
    })

