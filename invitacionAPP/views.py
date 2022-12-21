from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
# Create your views here.

def index(request):
    nombr = Nombre.objects.all()

    context = {
        'listar': nombr
    }
    return render(request, 'invitacion.html', context)

def ingresonombre(request):
    nombr = Nombre.objects.all()

    context = {
        'form': NombresForm(),
        'nombr': nombr,
    }
    if request.method == 'POST':
        formulario = NombresForm(data=request.POST)
        if formulario.is_valid():
           formulario.save()
           context['mensaje'] = "Se han ingresado los datos correctamente."
           return redirect(to='index')
        else:
            context['form'] = formulario

    return render(request, 'ingresonombre.html', context)

def listarnombre(request):
    listar = Nombre.objects.all()

    context = {
        'listar': listar
    }
    return render(request, 'listar.html', context)

def confirmar(request):
    data = {
        'form': ConfirmacionForm()
    }
    if request.method == 'POST':
        formulario = ConfirmacionForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Se han ingresado los datos correctamente."
        else:
            data['form'] = formulario

    return render(request, 'confirmacion.html', data)

