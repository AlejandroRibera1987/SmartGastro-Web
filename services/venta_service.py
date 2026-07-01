from database.db import db
from models.venta import Venta
from models.producto import Producto

def registrar_venta(data):
    producto_id = data.get("producto_id")
    cantidad = data.get("cantidad")

    if not producto_id or not cantidad:
        return None, "Faltan datos obligatorios"

    producto = Producto.query.get(producto_id)

    if not producto:
        return None, "Producto no encontrado"

    if not producto.activo:
        return None, "El producto está inactivo"

    cantidad = int(cantidad)

    if cantidad <= 0:
        return None, "La cantidad debe ser mayor a cero"

    if producto.stock < cantidad:
        return None, "Stock insuficiente"

    try:
        precio_unitario = producto.precio
        total = precio_unitario * cantidad

        venta = Venta(
            producto_id=producto.id,
            cantidad=cantidad,
            precio_unitario=precio_unitario,
            total=total
        )

        producto.stock -= cantidad

        db.session.add(venta)
        db.session.commit()

        return venta, None

    except Exception:
        db.session.rollback()
        return None, "Error al registrar la venta"


def listar_ventas():
    return Venta.query.order_by(Venta.fecha.desc()).all()