from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required # Incorporacion de "decorador"
from django.contrib.auth import logout
from .forms import CustomUserCreationForm, ClienteForm, ProvForm, EspecieForm, OrdenIngresoForm, OrdenIngresoDetalleForm
from django.contrib.auth import authenticate, login # Metodo para que despues de guardar registro inicia automaticamente la sesion
from .models import TablaCliente, TablaProv, TablaEspecie, TablaVariedad, OrdenIngresoDetalle, OrdenIngreso
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect,HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomUserChangeForm, VariedadForm
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

#FUNCION PARA CERRAR SESION
def exit(request):
	logout(request)
	return redirect('home')

#FUNCION FILTRO PARA GRUPO ADMINISTRADORES
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

# - - - - - - - - - - - - - - - FUNCIONES DE CLIENTES - - - - - - - - - - -

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
    

# - - - - - - - - - - - FUNCIONES DE PROVEEDORES - - - - - - - - - - - - - - - -

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

#FUNCION PARA VISUALIZAR LA TABLA DE ESPECIES
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

@user_passes_test(is_admin)
def modificar_especie(request, especie_id):
    especie = get_object_or_404(TablaEspecie, id=especie_id)
    if request.method == 'POST':
        form = EspecieForm(request.POST, instance=especie)
        if form.is_valid():
            form.save()
            messages.success(request, 'Especie modificada correctamente')
            return redirect('products')
    else:
        form = EspecieForm(instance=especie)

    return render(request, 'core/modificar_especie.html', {'form': form, 'especie': especie})

@user_passes_test(is_admin)
def eliminar_especie(request, especie_id):
    if request.method == 'POST':
        especie = get_object_or_404(TablaEspecie, id=especie_id)
        especie.delete()
        return HttpResponse('Especie eliminada correctamente', status=200)
    else:
        return HttpResponse('Método no permitido', status=405)

# - - - - - - - - - - - FUNCIONES PARA VARIEDADES - - - - - - - - - - - - - - 

#FUNCION PARA VISUALIZAR LA TABLA DE VARIEDADES
@user_passes_test(is_admin)
def table_view_variedades(request):
    if request.method == "GET":
        data = list(TablaVariedad.objects.values('id', 'especie__especie', 'variedad'))
        return JsonResponse({'data': data})

def add_variedad(request):
    if request.method == 'POST':
        form = VariedadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = VariedadForm()
    return render(request, 'core/agregar_variedad.html', {'form': form})

@user_passes_test(is_admin)
def modificar_variedad(request, variedad_id):
    variedad = get_object_or_404(TablaVariedad, id=variedad_id)
    if request.method == 'POST':
        form = VariedadForm(request.POST, instance=variedad)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = VariedadForm(instance=variedad)
    return render(request, 'core/modificar_variedad.html', {'form': form})

def eliminar_variedad(request, variedad_id):
    variedad = get_object_or_404(TablaVariedad, id=variedad_id)
    if request.method == 'POST':
        variedad = get_object_or_404(TablaVariedad, id=variedad_id)
        variedad.delete()
        return HttpResponse('Variedad eliminada correctamente', status=200)
    else:
        return HttpResponse('Método no permitido', status=405)

#otrasfunciones

#FUNCION PARA VISUALIZAR TABLA STOCK
def list_stock(request):
    productos = TablaVariedad.objects.all() 
    return render(request, 'core/lista_stock.html', {'productos': productos})

# FUNCION PARA AGREGAR STOCK
@user_passes_test(is_admin)
def add_orden_ingreso(request):
    if request.method == 'POST':
        form_ingreso = OrdenIngresoForm(request.POST)
        form_detalle = OrdenIngresoDetalleForm(request.POST)
        if form_ingreso.is_valid() and form_detalle.is_valid():
            orden_ingreso = form_ingreso.save()  
            detalle = form_detalle.save(commit=False)
            detalle.id_orden_ingreso = orden_ingreso
            detalle.save()  
            return redirect('list_stock')  
    else:
        form_ingreso = OrdenIngresoForm()
        form_detalle = OrdenIngresoDetalleForm()
    
    context = {
        'form_ingreso': form_ingreso,
        'form_detalle': form_detalle,
    }
    return render(request, 'core/lista_stock.html', context)

# FUNCIONES ORIENTADOS A LOS ROLES------------------------------------------

# INSTANCIACION DE USUARIOS
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

#HISTORIAL (INGRESO Y EGRESO)
def view_historial(request):
    is_admin = request.user.is_authenticated and (request.user.is_superuser or request.user.groups.filter(name='Administrativos').exists())
    return render(request, 'core/historial.html', {'is_admin': is_admin})