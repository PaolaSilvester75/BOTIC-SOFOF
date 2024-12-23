from django.shortcuts import render

from django.http import HttpResponse

def welcome_view(request):
    return render(request, 'book/index.html')

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
