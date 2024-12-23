from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view, name='index'),  
    path('palindromo/<str:phrase>/', views.check_palindrome, name='check_palindrome'),
]
