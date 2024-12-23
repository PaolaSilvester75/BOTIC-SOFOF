from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'valora']
        widgets = {
            'title': forms.TextInput(attrs={'maxlength': 150}),
            'author': forms.TextInput(attrs={'maxlength': 150}),
            'valora': forms.NumberInput(attrs={'min': 0, 'max': 10000}),
        }
