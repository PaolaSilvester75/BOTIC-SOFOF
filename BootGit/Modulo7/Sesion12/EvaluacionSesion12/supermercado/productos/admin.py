from django.contrib import admin
from .models import Fabricante, Producto

#admin.site.register(Fabricante)
#admin.site.register(Producto)


@admin.register(Fabricante)
class FabricanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'pais')  # Campos visibles en el administrador
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'fabricante', 'f_vencimiento')
    search_fields = ('nombre',)
    list_filter = ('fabricante', 'f_vencimiento')


# Register your models here.
