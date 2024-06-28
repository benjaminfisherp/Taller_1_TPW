from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required # Incorporacion de "decorador"
from django.contrib.auth import logout
from .forms import CustomUserCreationForm, ClienteForm, ProvForm, EspecieForm, VariedadForm, IngresoForm
from django.contrib.auth import authenticate, login # Metodo para que despues de guardar registro inicia automaticamente la sesion
from .models import TablaCliente, TablaProv, Ingreso, Egreso, TablaEspecie, TablaVariedad
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomUserChangeForm
from django.template.loader import render_to_string
from django import forms

@login_required
def home(request):
    is_admin = request.user.is_authenticated and (request.user.is_superuser or request.user.groups.filter(name='Administrativos').exists())
    return render(request, 'core/home.html', {'is_admin': is_admin})


def products(request):
    cliente = TablaCliente.objects.all()
    proveedores = TablaProv.objects.all()
    is_admin = request.user.is_superuser or request.user.groups.filter(name='Administrativos').exists()
    return render(request, 'core/products.html', {'proveedores': proveedores, 'is_admin': is_admin})

#FUNCION PARA SALIR
def exit(request):
	logout(request)
	return redirect('home')

#FUNCION FILTRO
def is_admin(user):
    return user.is_superuser or user.groups.filter(name='Administrativos').exists()

#FUNCION PARA REGISTRAR USUARIOS
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

#FUNCION PARA AÑADIR EN LA TABLA DE CLIENTE
@user_passes_test(is_admin)
def add_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ClienteForm()
    return render(request, 'core/agregar_cliente.html', {'form': form})

#FUNCION PARA ELIMINAR EN LA TABLA DE CLIENTE
@user_passes_test(is_admin)
def eliminar_cliente(request, cliente_id):
    if request.method == "POST":
        cliente = get_object_or_404(TablaCliente, id=cliente_id)
        cliente.delete()
        return HttpResponse('Cliente eliminado correctamente', status=200)
    else:
        return HttpResponse('Método no permitido', status=405)

#FUNCION PARA MODIFICAR EN LA TABLA DE CLIENTE
@user_passes_test(is_admin)
def modificar_cliente(request, cliente_id):
    cliente = get_object_or_404(TablaCliente, id=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente modificado correctamente')
            return redirect('products')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'core/modificar_cliente.html', {'form': form, 'cliente': cliente})
    

#FUNCION PARA VISUALIZAR LA TABLA DE PROVEEDORES
def table_view_prov(request):
    if request.method == "GET":
        proveedores = list(TablaProv.objects.values())
        return JsonResponse({'data': proveedores})

#FUNCION PARA AÑADIR EN LA TABLA DE PROVEEDORES
@user_passes_test(is_admin)
def add_prov(request):
    if request.method == 'POST':
        form = ProvForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProvForm()
    return render(request, 'core/agregar_prov.html', {'form': form})

#FUNCION PARA ELIMINAR PROVEEDORES
@user_passes_test(is_admin)
def eliminar_prov(request, prov_id):
    if request.method == 'POST':
        prov = get_object_or_404(TablaProv, id=prov_id)
        prov.delete()
        return HttpResponse('Proveedor eliminado correctamente', status=200)
    else:
        return HttpResponse('Método no permitido', status=405)

#FUNCION PARA MODIFICAR PROVEEDORES
@user_passes_test(is_admin)
def modificar_prov(request, prov_id):
    proveedor = get_object_or_404(TablaProv, id=prov_id)
    if request.method == 'POST':
        form = ProvForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor modificado correctamente')
            return redirect('products')
    else:
        form = ProvForm(instance=proveedor)

    return render(request, 'core/modificar_prov.html', {'form': form, 'proveedor': proveedor})


#FUNCION PARA VISUALIZAR LA TABLA DE INGRESOS
def table_view_ing(request):
    if request.method == "GET":
        data = list(Ingreso.objects.values())
        return JsonResponse({'data': data})

def add_ingreso(request):
    if request.method == 'POST':
        form = IngresoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = IngresoForm()
    return render(request, 'core/agregar_ingreso.html', {'form': form})

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

#FUNCION PARA VISUALIZAR LOS USUARIOS DE LA PLATAFORMA
@login_required
def lista_usuarios(request):
    users = User.objects.all()
    return render(request, 'core/lista_usuarios.html', {'users': users})

#FORMULARIO DE DJANGO PARA EDITAR USUARIOS
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

#FUNCION PARA EDITAR USUARIOS
@login_required
def editar_usuarios(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UserEditForm(instance=user)
    return render(request, 'core/editar_usuarios.html', {'form': form})

#FUNCION PARA ELIMINAR USUARIOS
@login_required
@user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='Administrativos').exists())
def eliminar_usuarios(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('lista_usuarios')
    return render(request, 'core/eliminar_usuarios.html', {'user': user})

#FUNCION PARA VISUALIZAR INGRESOS
def view_ingresos(request):
    ingresos = models.IngresoOrden.objects.all()
    return render(request, 'core/lista_ingresos.html', {"ingresos": ingresos})

