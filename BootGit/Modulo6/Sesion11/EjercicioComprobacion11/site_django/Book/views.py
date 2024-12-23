from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect
from .formsRL import RegistroUsuarioForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User



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



# Book/views.py
from django.shortcuts import render
from .forms import BookForm

def input_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'book/success.html') 
    else:
        form = BookForm()
    return render(request, 'book/inputbook.html', {'form': form})




#registro 

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            content_type = ContentType.objects.get(app_label='Book', model='book')
            permiso = Permission.objects.get(content_type=content_type, codename='development')
            usuario.user_permissions.add(permiso)

            return redirect('inicio')
    else:
        form = UserCreationForm()

    return render(request, 'book/registro.html', {'form': form})


#login :D
#user : test
#pass : 12345 
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inputbook')
    else:
        form = AuthenticationForm()
    return render(request, 'book/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')  
