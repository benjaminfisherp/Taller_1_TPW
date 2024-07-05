from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required # Incorporacion de "decorador"
from django.contrib.auth import logout
from .forms import CustomUserCreationForm, ClienteForm, ProvForm, EspecieForm, OrdenIngresoForm, OrdenIngresoDetalleForm, CalidadForm, OrdenEgresoForm
from .models import OrdenIngresoDetalle, OrdenEgresoDetalle
from django.contrib.auth import authenticate, login # Metodo para que despues de guardar registro inicia automaticamente la sesion
from .models import TablaCliente, TablaProv, TablaEspecie, TablaVariedad, TablaCalidad, OrdenEgreso
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect,HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomUserChangeForm, VariedadForm
from django.template.loader import render_to_string
from django import forms
from . import models
from django.db.models import Sum

@login_required
def home(request):
    is_admin = request.user.is_authenticated and (request.user.is_superuser or request.user.groups.filter(name='Administrativos').exists())
    return render(request, 'core/home.html', {'is_admin': is_admin})

def products(request):
    proveedores = TablaProv.objects.all() #?
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

#FUNCION PARA VISUALIZAR LA TABLA DE ESPECIES
def table_view_especies(request):
    if request.method == "GET":
        data = list(TablaEspecie.objects.values())
        return JsonResponse({'data': data})

@user_passes_test(is_admin)
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

#FUNCION PARA VISUALIZAR LA TABLA DE VARIEDADES
def table_view_variedades(request):
    if request.method == "GET":
        data = list(TablaVariedad.objects.values('id', 'especie__especie', 'variedad'))
        return JsonResponse({'data': data})

@user_passes_test(is_admin)
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

#FUNCIONES PARA VISUALIZAR TABLA DE CALIDADES
def table_view_calidad(request):
    if request.method == "GET":
        data = list(TablaCalidad.objects.values())
        return JsonResponse({'data': data})

@user_passes_test(is_admin)
def add_calidad(request):
    if request.method == 'POST':
        form = CalidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = CalidadForm()
    return render(request, 'core/agregar_calidad.html', {'form': form})

@user_passes_test(is_admin)
def modificar_calidad(request, calidad_id):
    calidad = get_object_or_404(TablaCalidad, id=calidad_id)
    if request.method == 'POST':
        form = CalidadForm(request.POST, instance=calidad)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = CalidadForm(instance=calidad)
    return render(request, 'core/modificar_calidad.html', {'form': form})

def eliminar_calidad(request, calidad_id):
    calidad = get_object_or_404(TablaCalidad, id=calidad_id)
    if request.method == 'POST':
        calidad = get_object_or_404(TablaCalidad, id=calidad_id)
        calidad.delete()
        return HttpResponse('Variedad eliminada correctamente', status=200)
    else:
        return HttpResponse('Método no permitido', status=405)
# FUNCIONES ORIENTADOS A LOS ROLES

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

#INGRESOS
def view_ingresos(request):
    ingresos = models.OrdenIngreso.objects.all()
    return render(request, 'core/lista_ingresos.html', {'ingresos': ingresos})

def view_detalle_ingreso(request, id):
    detalles = models.OrdenIngresoDetalle.objects.filter(id_orden_ingreso=id)
    return render(request, 'core/lista_detalle_ingreso.html', {'detalles': detalles})

def add_ingreso(request):
    if request.method=='POST':
        form = OrdenIngresoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/lista_ingresos.html', {'form': form})
    else:
        form = OrdenIngresoForm()
    return render(request,'core/agregar_ingreso.html', {'form': form})

def add_detalle_ingreso(request,id):
    if request.method=="POST":
        form = OrdenIngresoDetalleForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/lista_ingresos.html', {'form': form})
    else:
        form = OrdenIngresoDetalleForm()
    return render(request, 'core/agregar_detalle_ingreso.html', {'form': form})

def eliminar_ingreso(request, ingreso_id):
    if request.method == "POST":
        ingreso = get_object_or_404(models.OrdenIngreso, id=ingreso_id)
        ingreso.delete()
        return redirect('view_ingresos')
        #return HttpResponse('Orden de ingreso eliminado correctamente', status=200)
    else:
        return HttpResponse('Método no permitido', status=405)

#EGRESOS
def view_egresos(request):
    egresos = models.OrdenEgreso.objects.all()
    return render(request, 'core/lista_egresos.html', {'egresos': egresos})

def view_detalle_egreso(request, id):
    detalles_e = models.OrdenEgresoDetalle.objects.filter(id_orden_egreso=id)
    return render(request, 'core/lista_detalle_egreso.html', {'detalles_e': detalles_e})

def add_egreso(request):
    if request.method=='POST':
        form = OrdenEgresoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/lista_egresos.html', {'form': form})
    else:
        form = OrdenEgresoForm()
    return render(request,'core/agregar_egreso.html', {'form': form})

def add_detalle_egreso(request, id):
    if request.method == 'POST':
        especie_nombre = request.POST['especie']
        variedad_nombre = request.POST['variedad']
        calidad_nombre = request.POST['calidad']
        cantidad = int(request.POST['cantidad'])
        
        try:
            especie_obj = get_object_or_404(TablaEspecie, especie=especie_nombre)
            variedad_obj = get_object_or_404(TablaVariedad, especie=especie_obj, variedad=variedad_nombre)
            calidad_obj = get_object_or_404(TablaCalidad, calidad=calidad_nombre)
            
            ingresos = OrdenIngresoDetalle.objects.filter(variedad=variedad_obj, calidad=calidad_obj).aggregate(total_ingresos=Sum('cantidad'))
            egresos = OrdenEgresoDetalle.objects.filter(variedad=variedad_obj, calidad=calidad_obj).aggregate(total_egresos=Sum('cantidad'))
            
            total_ingresos = ingresos['total_ingresos'] if ingresos['total_ingresos'] else 0
            total_egresos = egresos['total_egresos'] if egresos['total_egresos'] else 0
            
            stock_disponible = total_ingresos - total_egresos
            
            if stock_disponible >= cantidad:

                orden_egreso = get_object_or_404(OrdenEgreso, id=id)

                OrdenEgresoDetalle.objects.create(
                    id_orden_egreso=orden_egreso,
                    especie=especie_obj,
                    variedad=variedad_obj,
                    calidad=calidad_obj,
                    cantidad=cantidad,
                )
                messages.success(request, 'Egreso creado exitosamente.')
            else:
                messages.error(request, 'Stock insuficiente para crear este egreso.')
        except TablaEspecie.DoesNotExist:
            messages.error(request, 'La especie especificada no existe.')
        except TablaVariedad.DoesNotExist:
            messages.error(request, 'La variedad especificada no existe.')
        except TablaCalidad.DoesNotExist:
            messages.error(request, 'La calidad especificada no existe.')
        
        return redirect('view_historial')
    
    especies = TablaEspecie.objects.values_list('especie', flat=True).distinct()
    variedades = TablaVariedad.objects.values_list('variedad', flat=True).distinct()
    calidades = TablaCalidad.objects.values_list('calidad', flat=True).distinct()
    
    return render(request, 'core/agregar_detalle_egreso.html', {
        'especies': especies,
        'variedades': variedades,
        'calidades': calidades
    })

def eliminar_egreso(request, egreso_id):
    if request.method == "POST":
        egreso = get_object_or_404(models.OrdenEgreso, id=egreso_id)
        egreso.delete()
        return redirect('view_egresos')
    else:
        return HttpResponse('Método no permitido', status=405)
    
#PRUEBA STOCK

from django.db.models import Sum

def view_stock(request):
    stock = []
    ingreso_detalles = OrdenIngresoDetalle.objects.values('variedad', 'calidad').distinct()
    
    for detalle in ingreso_detalles:
        variedad_id = detalle['variedad']
        calidad_id = detalle['calidad']
        
        variedad_obj = TablaVariedad.objects.get(id=variedad_id)
        calidad_obj = TablaCalidad.objects.get(id=calidad_id)
        calidad_nombre = calidad_obj.calidad 
        
        ingresos = OrdenIngresoDetalle.objects.filter(variedad=variedad_id, calidad=calidad_id).aggregate(total_ingresos=Sum('cantidad'))
        egresos = OrdenEgresoDetalle.objects.filter(variedad=variedad_id, calidad=calidad_id).aggregate(total_egresos=Sum('cantidad'))
        
        total_ingresos = ingresos['total_ingresos'] if ingresos['total_ingresos'] else 0
        total_egresos = egresos['total_egresos'] if egresos['total_egresos'] else 0
        
        stock_disponible = total_ingresos - total_egresos
        
        stock.append({
            'especie': variedad_obj.especie,
            'variedad': variedad_obj.variedad,
            'calidad': calidad_nombre,
            'stock_disponible': stock_disponible
        })
    
    return render(request, 'core/view_stock.html', {'stock': stock})
    