# Fichero creado para ser el formulario de creacion de usuario
# No se crea database ni formulario, solo se instancia aqui usando liberias django
# De hecho, tambien se genera de antemano la estetica del formulario 

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User # Importa la base de datos de usuarios para tener mayor cantidad de data para el registro (mail y demas)

# Fomrulario personalizado que usa plantilla creator form 
class CustomUserCreationForm(UserCreationForm):
	
	class Meta:
		model = User
		# Customizacion de data para registro
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
