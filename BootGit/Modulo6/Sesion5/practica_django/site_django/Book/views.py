from django.shortcuts import render

from django.shortcuts import render

def home_view(request):
    return render(request, 'book/home.html')  # Renderiza la página home

def welcome_view(request):
    return render(request, 'book/index.html')  # Renderiza la página de bienvenida

def list_books(request):
    books = [
        {"titulo": "Django 3 Web Development Cookbook", "autor": "Aidas Bendoraitis", "valoracion": 3250},
        {"titulo": "Two Scoops of Django 3.x", "autor": "Daniel Feldroy", "valoracion": 1570},
        {"titulo": "El libro de Django", "autor": "Adrian Holovaty", "valoracion": 1200},
        {"titulo": "Python Web Development with Django", "autor": "Jeff Forcier", "valoracion": 1400},
        {"titulo": "Django for Professionals", "autor": "William S. Vincent", "valoracion": 2100},
        {"titulo": "Django for APIs", "autor": "William S. Vincent", "valoracion": 2540},
    ]

    high_rated_books = [book for book in books if book["valoracion"] > 1500]

    context = {
        "books": books,
        "high_rated_books": high_rated_books,
    }

    return render(request, 'book/list_books.html', context)

# views.py
from django.http import HttpResponse

def check_palindrome(request, phrase):
    # Eliminar espacios y poner en minúsculas
    cleaned_phrase = ''.join(phrase.split()).lower()
    # Verificar si es un palíndromo
    if cleaned_phrase == cleaned_phrase[::-1]:
        result = f"{phrase} ES PALINDROMO"
    else:
        result = f"{phrase} NO ES PALINDROMO"
    return HttpResponse(result)

