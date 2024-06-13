from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User # Importa la base de datos de usuarios para tener mayor cantidad de data para el registro (mail y demas)
from django.contrib.auth import get_user_model
from core.models import TablaCliente, TablaProv

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
