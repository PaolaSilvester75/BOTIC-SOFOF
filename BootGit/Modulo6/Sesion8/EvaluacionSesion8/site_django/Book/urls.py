from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home_view, name='home'),               # Ruta para la página principal
    path('inicio/', views.welcome_view, name='inicio'), 
    path('listbook/', views.list_books, name='list_books'),  # Ruta para la sección "Inicio"
    path('inputbook/', views.input_book, name='inputbook'),
    path('registro/', views.registro, name='registro'),
    path('libros/', views.libros, name='libros'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
