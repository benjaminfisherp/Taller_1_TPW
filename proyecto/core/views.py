from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required # Incorporacion de "decorador"
from django.contrib.auth import logout
from .forms import CustomUserCreationForm, ClienteForm, ProvForm, EspecieForm, VariedadForm
from django.contrib.auth import authenticate, login # Metodo para que despues de guardar registro inicia automaticamente la sesion
from .models import TablaCliente, TablaProv, Ingreso, Egreso, TablaEspecie, TablaVariedad
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomUserChangeForm
from django.template.loader import render_to_string

@login_required
def home(request):
    is_admin = request.user.is_authenticated and (request.user.is_superuser or request.user.groups.filter(name='Administrativos').exists())
    return render(request, 'core/home.html', {'is_admin': is_admin})

@login_required
def products(request):
    is_admin = request.user.is_superuser or request.user.groups.filter(name='Administrativos').exists()
    return render(request, 'core/products.html', {'is_admin': is_admin})

def exit(request):
	logout(request)
	return redirect('home')

def is_admin(user):
    return user.is_superuser or user.groups.filter(name='Administrativos').exists()

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
@user_passes_test(is_admin)
def table_view_cliente(request):
    if request.method == "GET":
        data = list(TablaCliente.objects.values())
        return JsonResponse({'data': data})

def add_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ClienteForm()
    return render(request, 'core/agregar_cliente.html', {'form': form})

def eliminar_persona(request, persona_id):
    if request.method == "POST":
        persona = get_object_or_404(TablaCliente, id=persona_id)
        persona.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

#FUNCION PARA VISUALIZAR LA TABLA DE PROVEEDORES
@user_passes_test(is_admin)
def table_view_prov(request):
    if request.method == "GET":
        data = list(TablaProv.objects.values())
        return JsonResponse({'data': data})

def add_prov(request):
    if request.method == 'POST':
        form = ProvForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProvForm()
    return render(request, 'core/agregar_prov.html', {'form': form})

#FUNCION PARA VISUALIZAR LA TABLA DE INGRESOS
def table_view_ing(request):
    if request.method == "GET":
        data = list(Ingreso.objects.values())
        return JsonResponse({'data': data})
    
#FUNCION PARA VISUALIZAR LA TABLA DE EGRESOS
def table_view_egr(request):
    if request.method == "GET":
        data = list(Egreso.objects.values())
        return JsonResponse({'data': data})

#FUNCION PARA VISUALIZAR LA TABLA DE FRUTAS
@user_passes_test(is_admin)
def table_view_especies(request):
    if request.method == "GET":
        data = list(TablaEspecie.objects.values())
        return JsonResponse({'data': data})

def add_especie(request):
    if request.method == 'POST':
        form = EspecieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = EspecieForm()
    return render(request, 'core/agregar_especie.html', {'form': form})

#FUNCION PARA VISUALIZAR LA TABLA DE VARIEDADES
@user_passes_test(is_admin)
def table_view_variedades(request):
    if request.method == "GET":
        data = list(TablaVariedad.objects.values())
        return JsonResponse({'data': data})

def add_variedad(request):
    if request.method == 'POST':
        form = VariedadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = EspecieForm()
    return render(request, 'core/agregar_variedad.html', {'form': form})

User = get_user_model()

@login_required
@user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='Administrativos').exists())
def lista_usuarios(request):
    users = User.objects.all()
    return render(request, 'core/lista_usuarios.html', {'users': users})

@login_required
@user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='Administrativos').exists())
def editar_usuarios(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            form_html = render_to_string('core/editar_usuarios_form.html', {'form': form, 'user': user})
            return JsonResponse({'success': False, 'form': form_html})
    else:
        form = CustomUserChangeForm(instance=user)
        form_html = render_to_string('core/editar_usuarios_form.html', {'form': form, 'user': user})
        return JsonResponse({'form': form_html, 'url': request.path})


@login_required
@user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='Administrativos').exists())
def eliminar_usuarios(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('lista_usuarios')
    return render(request, 'core/eliminar_usuarios.html', {'user': user})




