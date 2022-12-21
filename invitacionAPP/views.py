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
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'])
            dj_login(request, user)
            return redirect(to="panel")

        context['form'] = formulario

    return render(request, 'ingresonombre.html', context)



