from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home_view, name='home'),               # Ruta para la página principal
    path('inicio/', views.welcome_view, name='inicio'), 
    path('listbook/', views.list_books, name='list_books'),  # Ruta para la sección "Inicio"
    path('inputbook/', views.input_book, name='inputbook'),
    
    
]
