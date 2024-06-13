from django.contrib import admin
from django.urls import path, include # se incluye include para solucionar error de rutas de admin
from .views import home, products, exit, register, table_view_cliente, table_view_prov
from .views import lista_usuarios, editar_usuarios, eliminar_usuarios
urlpatterns = [
	path('', home, name='home'),
    path('products/', products, name='products'),
    path('logout/', exit, name='exit'),
    path('register/', register, name='register'),
    path('get-cliente-data/', table_view_cliente, name='table_view_cliente'),
    path('get-prov-data/', table_view_prov, name='table_view_prov'),
    path('users/', lista_usuarios, name='lista_usuarios'),
    path('users/edit/<int:user_id>/', editar_usuarios, name='editar_usuarios'),
    path('users/delete/<int:user_id>/', eliminar_usuarios, name='eliminar_usuarios'),
]
