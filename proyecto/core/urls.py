from django.contrib import admin
from django.urls import path 
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

    #URLS PARA CALIDAD
    path('get-calidad-data/', views.table_view_calidad, name='table_view_calidad'),
    path('agregar-calidad/', views.add_calidad, name="agregar_calidad"),
    path('modificar_calidad/<int:calidad_id>/', views.modificar_calidad, name='modificar_calidad'),
    path('eliminar_calidad/<int:calidad_id>/', views.eliminar_calidad, name='eliminar_calidad'),

    # URLS PARA HISTORIAL (INGRESO, EGRESO Y STOCK)
    path('historial/', views.view_historial, name="view_historial"),

    #INGRESO
    path('view_ingresos/', views.view_ingresos, name="view_ingresos"),
    path('view_detalle_ingreso<int:id>', views.view_detalle_ingreso, name="view_detalle_ingreso"),
    path('add_ingreso/', views.add_ingreso,name="add_ingreso"),
    path('add_detalle_ingreso/<int:id>/',views.add_detalle_ingreso,name="add_detalle_ingreso"),
    path('eliminar_ingreso/<int:ingreso_id>/', views.eliminar_ingreso, name='eliminar_ingreso'),

    #EGRESO
    path('view_egresos/', views.view_egresos, name="view_egresos"),
    path('view_detalle_egreso<int:id>', views.view_detalle_egreso, name="view_detalle_egreso"),
    path('add_egreso/', views.add_egreso,name="add_egreso"),
    path('add_detalle_egreso/<int:id>/',views.add_detalle_egreso,name="add_detalle_egreso"),
    path('eliminar_egreso/<int:egreso_id>/', views.eliminar_egreso, name='eliminar_egreso'),

    #PRUEBA STOCK
    path('view_stock', views.view_stock, name="view_stock"),
]
