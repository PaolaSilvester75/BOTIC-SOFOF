from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_laboratorios, name='listar_laboratorios'),
    path('insertar/', views.insertar_laboratorio, name='insertar_laboratorio'),
    path('editar/<int:id>/', views.editar_laboratorio, name='editar_laboratorio'),
    path('eliminar/<int:id>/', views.eliminar_laboratorio, name='eliminar_laboratorio'),
]
