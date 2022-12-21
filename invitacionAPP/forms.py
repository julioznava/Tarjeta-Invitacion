from django import forms
from .models import Nombre, Confirmacion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NombresForm(forms.ModelForm):

    class Meta:
        model = Nombre
        fields = ['nombre']


class ConfirmacionForm(forms.ModelForm):
    class Meta:
        model = Confirmacion
        fields = '__all__'

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
        exclude = ['password1', 'password2', 'password']

