from django.shortcuts import redirect, render
from vehiculo.forms import VehiculoForm
from .models import Vehiculo

def index(request):
    return render(request, 'index.html')


def vehiculo_add(request):
    if request.method == "POST":
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VehiculoForm()
    return render(request, 'form.html', {'form': form})

def vehiculo_list(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'listar.html', {'vehiculos': vehiculos})



# Create your views here.
