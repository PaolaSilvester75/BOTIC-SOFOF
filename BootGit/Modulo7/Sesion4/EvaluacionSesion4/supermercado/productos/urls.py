from django.urls import path
from . import views

urlpatterns = [
    path('lista', views.productos_view, name='lista'),
    path('agregar', views.agregar_producto, name='agregar'),
]
