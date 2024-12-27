from django.shortcuts import render
#from productos.models import Fabricante, Producto
from django.db import connection
from productos.models import Producto


#def listar_fabricas_productos(request):
#    fabricas_query = "SELECT id, nombre FROM productos_fabricante"
#   fabricas = Fabricante.objects.raw(fabricas_query)
#    productos_query = """
#        SELECT p.id, p.nombre, f.nombre AS fabricante_nombre
 #       FROM productos_producto p
 #       INNER JOIN productos_fabricante f ON p.fabricante_id = f.id
  #  """
  #  productos = Producto.objects.raw(productos_query)

  #  return render(request, 'listar_fabricas_productos.html', {
   #     'fabricas': fabricas,
   #     'productos': productos,
   # })


#def buscar_producto(request):

    #producto_query = """
      #  SELECT p.id, p.nombre, f.nombre AS fabricante_nombre
      #  FROM productos_producto p
      #  INNER JOIN productos_fabricante f ON p.fabricante_id = f.id
       # WHERE p.nombre = %s
    #"""
   # producto = Producto.objects.raw(producto_query, ['Protex Aloe'])

   # return render(request, 'buscar_producto.html', {'producto': producto[0] if producto else None})




def obtener_productos(request):
    query = """
        SELECT id, nombre, precio, f_vencimiento
        FROM productos_producto
    """
    productos = Producto.objects.raw(query)

    return render(request, 'productos.html', {
        'productos': productos
    })


def obtener_productos_precio(request):
    query = """
        SELECT id, nombre, precio
        FROM productos_producto
        WHERE precio <= 2500
    """
    productos = Producto.objects.raw(query)

    return render(request, 'productos_precio.html', {
        'productos': productos
    })


def modificar_fabrica(request):
    query = """
        UPDATE productos_fabrica
        SET pais = 'Canadá'
        WHERE nombre = 'P&G' AND (pais = 'EEUU' OR pais = 'Canadá')
    """
    with connection.cursor() as cursor:
        cursor.execute(query)

    return render(request, 'modificacion.html', {
        'mensaje': "Se ha modificado la fábrica P&G correctamente."
    })
