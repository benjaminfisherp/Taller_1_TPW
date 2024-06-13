# Fichero creado para ser el formulario de creacion de usuario
# No se crea database ni formulario, solo se instancia aqui usando liberias django
# De hecho, tambien se genera de antemano la estetica del formulario 

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User # Importa la base de datos de usuarios para tener mayor cantidad de data para el registro (mail y demas)

# Fomrulario personalizado que usa plantilla creator form 
# class CustomUserCreationForm(UserCreationForm):
	
# 	class Meta:
# 		model = User
# 		# Customizacion de data para registro
# 		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


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