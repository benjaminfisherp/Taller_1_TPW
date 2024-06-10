from django.contrib import admin
from .models import TablaCliente, TablaProv, TablaVariedad, TablaEspecie

# Register your models here.
admin.site.register(TablaCliente) #PERMISO PARA AÑADIR REGISTROS DE CLIENTE COMO ADMIN
admin.site.register(TablaProv) #PERMISO PARA AÑADIR REGISTROS DE PROVEEDORES COMO ADMIN
admin.site.register(TablaVariedad) #PERMISO PARA AÑADIR REGISTROS DE VARIEDAD COMO ADMIN
admin.site.register(TablaEspecie) #PERMISO PARA AÑADIR REGISTROS DE ESPECIE COMO ADMIN

