from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required # Incorporacion de "decorador"
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login # Metodo para que despues de guardar registro inicia automaticamente la sesion
from .models import TablaCliente, TablaProv, TablaFruta
from django.http import JsonResponse
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

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Aquí puedes manejar el envío del correo o guardar la información en la base de datos
        send_mail(
            f'Mensaje de {name}',
            message,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return HttpResponse('Gracias por tu mensaje. Nos pondremos en contacto contigo pronto.')
    
    return render(request, 'core/contact.html')

def exit(request):
	logout(request)
	return redirect('home')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)

#FUNCION PARA VISUALIZAR LA TABLA DE CLIENTE
def table_view_cliente(request):
    if request.method == "GET":
        data = list(TablaCliente.objects.values())
        return JsonResponse({'data': data})

#FUNCION PARA VISUALIZAR LA TABLA DE PROVEEDORES
def table_view_prov(request):
    if request.method == "GET":
        data = list(TablaProv.objects.values())
        return JsonResponse({'data': data})
	
#FUNCION PARA VISUALIZAR LA TABLA DE FRUTAS
def table_view_fruta(request):
    if request.method == "GET":
        data = list(TablaFruta.objects.values())
        return JsonResponse({'data': data})
