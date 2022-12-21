from django import forms
from .models import *


class NombresForm(forms.Form):

    class Meta:
        model = Nombre
        fields = '__all__'


class ConfirmacionForm(forms.Form):
    class Meta:
        model = Confirmacion
        fields = '__all__'