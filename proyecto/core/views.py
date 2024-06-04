from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required # Incorporacion de "decorador"
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login # Metodo para que despues de guardar registro inicia automaticamente la sesion


# login_required = permite la necesidad de poder logear para ingresar a una vista
# debe aplicarse como decorador delate de la funcion de vista 

#@login_required
# Define "home"
def home(request):
	return render(request, 'core/home.html')

@login_required 
# si login required estuviee aqui, al estar despues de la vista NO encuentra TEMPLATED y marca error de template obviamente 
# Define products o el contenido
def products(request):
	return render(request, 'core/products.html')

def exit(request):
	logout(request)
	return redirect('home')

def register(request):
	# Instancia el formulario para registros de sesiones
	data = {
		'form': CustomUserCreationForm() #form aqui es solo variable
	}
	
	# Para generar utildad al formulario se genera la siguiente funcion para cargar datos de este
	if request.method == 'POST': 
		user_creation_form = CustomUserCreationForm(data=request.POST)
		
		if user_creation_form.is_valid(): # Si son validos los datos PUM lo guarda a la base de datos
			user_creation_form.save()
			
			# ojo que es password1 porque es el contenedor donde se escribe la contraseña en registro 
			user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1']) # pasar el user y contraseña
			login(request, user)
			return redirect('home')
		
	# Ojo que ahora el data se tiene que pasar como "render" al return (Solucion a ERROR)
	return render(request, 'registration/register.html', data)