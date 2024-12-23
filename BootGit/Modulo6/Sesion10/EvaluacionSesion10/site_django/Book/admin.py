from django.contrib import admin
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'author', 'rating', 'fecha_modificacion')  
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')  
    list_filter = ('rating', 'fecha_modificacion')  
    search_fields = ('title', 'author')  


# Register your models here.
