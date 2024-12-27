from django.shortcuts import render


from productos.models import Fabricante, Producto

def listar_fabricas_productos(request):
    fabricas_query = "SELECT id, nombre FROM productos_fabricante"
    fabricas = Fabricante.objects.raw(fabricas_query)
    productos_query = """
        SELECT p.id, p.nombre, f.nombre AS fabricante_nombre
        FROM productos_producto p
        INNER JOIN productos_fabricante f ON p.fabricante_id = f.id
    """
    productos = Producto.objects.raw(productos_query)

    return render(request, 'listar_fabricas_productos.html', {
        'fabricas': fabricas,
        'productos': productos,
    })


def buscar_producto(request):

    producto_query = """
        SELECT p.id, p.nombre, f.nombre AS fabricante_nombre
        FROM productos_producto p
        INNER JOIN productos_fabricante f ON p.fabricante_id = f.id
        WHERE p.nombre = %s
    """
    producto = Producto.objects.raw(producto_query, ['Protex Aloe'])

    return render(request, 'buscar_producto.html', {'producto': producto[0] if producto else None})


# Create your views here.
