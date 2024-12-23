from django.contrib import admin
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'fecha_creacion', 'fecha_modificacion') 
    list_filter = ('fecha_creacion', 'fecha_modificacion')  
    search_fields = ('title', 'author')  



# Register your models here.
