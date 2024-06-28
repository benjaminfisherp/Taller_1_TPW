from django.contrib import admin
from django.urls import path, include # se incluye include para solucionar error de rutas de admin
from .views import home, products, exit, register, table_view_cliente, table_view_prov, table_view_ing, table_view_egr
from .views import lista_usuarios, editar_usuarios, eliminar_usuarios, add_cliente, add_prov, eliminar_cliente, add_ingreso, modificar_cliente, modificar_prov
from .views import table_view_especies, table_view_variedades, add_especie, add_variedad
from . import views
#from . import views ESTO NOS SERVIRÁ PARA ELIMINAR LAS LINEAS 3 Y 4 (ESTETICA DEL CODIGO)

urlpatterns = [
	path('', home, name='home'),
    path('products/', products, name='products'),
    path('logout/', exit, name='exit'),
    path('register/', register, name='register'),
    path('get-cliente-data/', table_view_cliente, name='table_view_cliente'),
    path('get-prov-data/', table_view_prov, name='table_view_prov'),
    path('get-ing-data/', table_view_ing, name='table_view_ing'),
    path('get-egr-data/', table_view_egr, name='table_view_egr'),
    path('users/', lista_usuarios, name='lista_usuarios'),
    path('users/edit/<int:user_id>/', editar_usuarios, name='editar_usuarios'),
    path('users/delete/<int:user_id>/', eliminar_usuarios, name='eliminar_usuarios'),
    path('agregar/', add_cliente, name='AddCliente'),
    path('eliminar/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('modificar/<int:cliente_id>/', modificar_cliente, name='modificar_cliente'),
    path('agregar_prov/', add_prov, name='agregar_prov'),
    path('modificar_prov/<int:prov_id>/', views.modificar_prov, name='modificar_prov'),
    path('eliminar_prov/<int:prov_id>/', views.eliminar_prov, name='eliminar_prov'),
    path('get-esp-data/',table_view_especies, name = 'table_view_esp'),
    path('get-var-data/',table_view_variedades, name = 'table_view_var'),
    path('agregar-especie/', add_especie, name='AddEspecie'),
    path('agregar-variedad/', add_variedad, name='AddVariedad'),
    path('ingreso/agregar/', add_ingreso, name='AddIngreso'),

]
