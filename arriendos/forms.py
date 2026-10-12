from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Inmueble

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'rut', 'direccion', 'telefono_personal', 'tipo_usuario']

class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        exclude = ['arrendador']