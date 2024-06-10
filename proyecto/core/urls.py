from django.contrib import admin
from django.urls import path
from .views import home, products, exit, register, table_view_cliente, table_view_prov, contact

urlpatterns = [
	path('', home, name='home'),
    path('admin/', admin.site.urls),
	path('products/', products, name='products'),
    path('contact/', contact, name='contact'),
	path('logout/', exit, name='exit'),
	path('register/', register, name='register'),
    path('get-cliente-data/', table_view_cliente, name='table_view_cliente'), #VISUALIZACION TABLA CLIENTE
    path('get-prov-data/', table_view_prov, name='table_view_prov'), #VISUALIZACION TABLA PROVEEDORES
]
