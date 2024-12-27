from django.shortcuts import render, redirect, get_object_or_404
from .models import Laboratorio
from .forms import LaboratorioForm

def listar_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'listar.html', {'laboratorios': laboratorios})

def insertar_laboratorio(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_laboratorios')
    else:
        form = LaboratorioForm()
    return render(request, 'insertar.html', {'form': form})

def editar_laboratorio(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('listar_laboratorios')
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'editar.html', {'form': form})

def eliminar_laboratorio(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('listar_laboratorios')
    return render(request, 'eliminar.html', {'laboratorio': laboratorio})
