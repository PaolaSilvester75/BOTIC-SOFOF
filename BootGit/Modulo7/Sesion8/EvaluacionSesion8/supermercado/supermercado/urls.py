"""
URL configuration for supermercado project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from productos.views import listar_fabricas_productos,buscar_producto
from productos.views import obtener_productos,obtener_productos_precio,modificar_fabrica

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('listar-fabricas-productos/', listar_fabricas_productos, name='listar_fabricas_productos'),
    #path('buscar-producto/', buscar_producto, name='buscar_producto'),
    #path('productos/', obtener_productos, name='productos'),
    path('productos_precio/', obtener_productos_precio, name='productos_precio'),
    path('modificar_fabrica/', modificar_fabrica, name='modificar_fabrica'),
]

