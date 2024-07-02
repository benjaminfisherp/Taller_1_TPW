from django.contrib import admin
from django.urls import path, include # se incluye include para solucionar error de rutas de admin
from .views import home, products, exit, register
from .views import table_view_cliente, table_view_prov, table_view_especies, table_view_variedades
from .views import lista_usuarios, editar_usuarios, eliminar_usuarios, add_cliente, add_prov, eliminar_cliente, modificar_cliente, modificar_prov, add_especie, modificar_especie, eliminar_especie, modificar_variedad, eliminar_variedad
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('logout/', views.exit, name='exit'),
    path('register/', views.register, name='register'),
    # URLS PARA USUARIOS
    path('users/', views.lista_usuarios, name='lista_usuarios'),
    path('users/edit/<int:user_id>/', views.editar_usuarios, name='editar_usuarios'),
    path('users/delete/<int:user_id>/', views.eliminar_usuarios, name='eliminar_usuarios'),
    # URLS PARA CLIENTES
    path('get-cliente-data/', views.table_view_cliente, name='table_view_cliente'),
    path('agregar/', views.add_cliente, name='AddCliente'),
    path('eliminar/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('modificar/<int:cliente_id>/', views.modificar_cliente, name='modificar_cliente'),
    # URLS PARA PROVEEDORES
    path('get-prov-data/', views.table_view_prov, name='table_view_prov'),
    path('agregar_prov/', views.add_prov, name='agregar_prov'),
    path('modificar_prov/<int:prov_id>/', views.modificar_prov, name='modificar_prov'),
    path('eliminar_prov/<int:prov_id>/', views.eliminar_prov, name='eliminar_prov'),
    # URLS PARA ESPECIES
    path('get-esp-data/',views.table_view_especies, name = 'table_view_especies'),
    path('agregar-especie/', views.add_especie, name='agregar_especie'),
    path('modificar_especie/<int:especie_id>/', views.modificar_especie, name='modificar_especie'),
    path('eliminar_especie/<int:especie_id>/', views.eliminar_especie, name='eliminar_especie'),
    # URLS PARA VARIEDADES
    path('get-var-data/',views.table_view_variedades, name = 'table_view_variedades'),
    path('agregar-variedad/', views.add_variedad, name='agregar_variedad'),
    path('modificar_variedad/<int:variedad_id>/', views.modificar_variedad, name='modificar_variedad'),
    path('eliminar_variedad/<int:variedad_id>/', views.eliminar_variedad, name='eliminar_variedad'),

    # URLS PARA STOCK
    path('historial/', views.view_historial, name="view_historial"),

	# list_stock
	path('list_stock/', views.list_stock, name='list_stock'),
	path('get-ingreso-data/', views.add_orden_ingreso, name='add_orden_ingreso'),

]
