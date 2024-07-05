from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User # Importa la base de datos de usuarios para tener mayor cantidad de data para el registro (mail y demas)
from django.contrib.auth import get_user_model
from core.models import TablaCliente, TablaProv, TablaVariedad, TablaEspecie, OrdenIngreso, OrdenIngresoDetalle, TablaCalidad
from . import models

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 5:
            raise forms.ValidationError("El nombre de usuario debe tener al menos 5 caracteres.")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        if len(password1) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        return password2

User = get_user_model()

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_active', 'is_staff')

class ClienteForm(forms.ModelForm):
    class Meta:
        model = TablaCliente
        fields = ('name','rut','correo','telefono','razon_social')

class ProvForm(forms.ModelForm):
    class Meta:
        model = TablaProv
        fields = {'name_prov','rut_prov','correo_prov','telefono_prov','razon_social_prov',
                  'direccion_prov','region_prov','comuna_prov','ncontacto_prov'}

class EspecieForm(forms.ModelForm):
    class Meta:
        model = TablaEspecie
        fields = {'especie'}

class VariedadForm(forms.ModelForm):
    class Meta:
        model = TablaVariedad
        fields = ['especie', 'variedad']
        
class CalidadForm(forms.ModelForm):
    class Meta:
        model = TablaCalidad
        fields = ['calidad']
        
# FORMULARIO DE LA ORDENES DE INGRESO
class OrdenIngresoForm(forms.ModelForm):
    class Meta:
        model = OrdenIngreso
        fields = ['proveedor', 'fecha_ingreso']

        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date'}),
        }

class OrdenIngresoDetalleForm(forms.ModelForm):
    class Meta:
        model = OrdenIngresoDetalle
        fields = ['id_orden_ingreso', 'especie', 'variedad', 'calidad', 'cantidad']

# FORUMULARIO DE LAS ORDENES DE EGRESO
class OrdenEgresoForm(forms.ModelForm):
    class Meta:
        model = models.OrdenEgreso
        fields = ['cliente', 'fecha_egreso']

        widgets = {
            'fecha_egreso': forms.DateInput(attrs={'type': 'date'}),
        }

class OrdenEgresoDetalleForm(forms.ModelForm):
    class Meta:
        model = models.OrdenEgresoDetalle
        fields = ['id_orden_egreso','especie','variedad','calidad','cantidad']