from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contenido
from .forms import ContenidoForm
# Create your views here.

def principal(request):
    return render(request, 'paginas/inicio.html')
def inicio(request):
    return render(request, 'paginas/inicio.html')
def empleados(request):
    contenidos = Contenido.objects.all()
    return render(request, 'empleados/index.html', {'contenidos': contenidos})
def crear(request):
    formulario = ContenidoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('empleados')
    return render(request, 'empleados/crear.html', {'formulario': formulario})
def editar(request, id):
    empleado = Contenido.objects.get(id=id)
    formulario = ContenidoForm(request.POST or None, request.FILES or None, instance=empleado)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('empleados')
    return render(request, 'empleados/editar.html', {'formulario':formulario})
def eliminar(request, id):
    contenido = Contenido.objects.get(id=id)
    contenido.delete()
    return redirect('empleados')