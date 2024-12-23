from django.shortcuts import render,redirect
from .models import Producto
from .form import ProductoForm

def productos_view(request):
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})



def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = ProductoForm()
    return render(request, 'agregar.html', {'form': form})


# Create your views here.
