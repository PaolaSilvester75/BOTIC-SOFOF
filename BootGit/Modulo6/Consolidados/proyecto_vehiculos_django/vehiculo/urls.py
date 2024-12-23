from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.vehiculo_add, name='add'),  
    path('listar', views.vehiculo_list, name='listar'),
]
