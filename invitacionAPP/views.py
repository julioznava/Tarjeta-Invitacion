from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login as dj_login
# Create your views here.

def index(request):
    nombr = Nombre.objects.all()

    context = {
        'listar': nombr
    }
    return render(request, 'invitacion.html', context)

def ingresonombre(request):
    context = {
        'form': NombresForm()
    }
    if request.method == 'POST':
        formulario = NombresForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="index")
        context['form'] = formulario

    return render(request, 'ingresonombre.html', context)



