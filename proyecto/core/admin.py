from django.contrib import admin
from .models import TablaCliente, TablaProv, TablaFruta

# Register your models here.
admin.site.register(TablaCliente) #PERMISO PARA AÑADIR REGISTROS DE CLIENTE COMO ADMIN
admin.site.register(TablaProv) #PERMISO PARA AÑADIR REGISTROS DE PROVEEDORES COMO ADMIN
admin.site.register(TablaFruta) #PERMISO PARA AÑADIR REGISTROS DE FRUTA COMO ADMIN
