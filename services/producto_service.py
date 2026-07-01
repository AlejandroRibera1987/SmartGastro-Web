from database.db import db
from models.producto import Producto

def listar_productos():
    return Producto.query.all()

def crear_producto(data):
    nombre = data.get("nombre")
    descripcion = data.get("descripcion")
    precio = data.get("precio")
    stock = data.get("stock")
    activo = data.get("activo", True)

    if not nombre or precio is None or stock is None:
        return None, "Faltan datos obligatorios"

    try:
        producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=float(precio),
            stock=int(stock),
            activo=activo
        )

        db.session.add(producto)
        db.session.commit()

        return producto, None

    except Exception:
        db.session.rollback()
        return None, "Error al crear el producto"


def obtener_producto_por_id(producto_id):
    return Producto.query.get(producto_id)


def actualizar_producto(producto_id, data):
    producto = obtener_producto_por_id(producto_id)

    if not producto:
        return None, "Producto no encontrado"

    try:
        producto.nombre = data.get("nombre", producto.nombre)
        producto.descripcion = data.get("descripcion", producto.descripcion)
        producto.precio = float(data.get("precio", producto.precio))
        producto.stock = int(data.get("stock", producto.stock))
        producto.activo = data.get("activo", producto.activo)

        db.session.commit()

        return producto, None

    except Exception:
        db.session.rollback()
        return None, "Error al actualizar el producto"


def eliminar_producto(producto_id):
    producto = obtener_producto_por_id(producto_id)

    if not producto:
        return False, "Producto no encontrado"

    try:
        db.session.delete(producto)
        db.session.commit()

        return True, None

    except Exception:
        db.session.rollback()
        return False, "Error al eliminar el producto"

def cambiar_estado_producto(producto_id):
    producto = Producto.query.get(producto_id)

    if not producto:
        return None, "Producto no encontrado"

    try:
        producto.activo = not producto.activo
        db.session.commit()

        return producto, None

    except Exception:
        db.session.rollback()
        return None, "Error al cambiar el estado del producto"