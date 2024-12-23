from django import forms
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'valoracion']

    title = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Título del libro'})
    )
    author = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Autor'})
    )
    valoracion = forms.DecimalField(
        min_value=0,
        max_value=10000,
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Valoración'})
    )



class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
