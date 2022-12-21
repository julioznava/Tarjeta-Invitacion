from django import forms
from .models import Nombre, Confirmacion



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
        model = Nombre
        fields = ['nombre']


