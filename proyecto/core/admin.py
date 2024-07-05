from django.contrib import admin
from .models import TablaCliente, TablaProv, TablaVariedad, TablaEspecie, Account, OrdenIngreso, OrdenIngresoDetalle, OrdenEgresoDetalle, OrdenEgreso, TablaCalidad

# Register your models here.
admin.site.register(TablaEspecie)  # PERMISO PARA AÑADIR REGISTROS DE ESPECIE COMO ADMIN
admin.site.register(TablaCalidad)

@admin.register(TablaProv)
class TablaProvAdmin(admin.ModelAdmin):
    list_display = ('name_prov', 'rut_prov', 'correo_prov', 'telefono_prov', 'razon_social_prov', 'direccion_prov', 'region_prov', 'comuna_prov', 'ncontacto_prov')
    search_fields = ('name_prov', 'rut_prov', 'correo_prov')
    list_filter = ('region_prov', 'comuna_prov')

@admin.register(TablaCliente)
class TablaClienteAdmin(admin.ModelAdmin):
	list_display = ('name', 'rut', 'correo', 'telefono', 'razon_social')
	search_fields = ('name', 'rut', 'correo')

@admin.register(TablaVariedad)
class TablaVariedadAdmin(admin.ModelAdmin):
	list_display = ('variedad', 'especie')
	search_fields = ('variedad', 'especie')
      
@admin.register(OrdenIngreso)
class OrdenIngresoAdmin(admin.ModelAdmin):
    list_display = ('id', 'proveedor', 'fecha_ingreso')
    list_filter = ('proveedor', 'fecha_ingreso')

@admin.register(OrdenIngresoDetalle)
class OrdenIngresoDetalleAdmin(admin.ModelAdmin):
    list_display = ('id_orden_ingreso', 'especie','variedad','calidad','cantidad')
    list_filter = ('id_orden_ingreso__proveedor', 'especie','variedad')
    
@admin.register(OrdenEgreso)
class OrdenEgresoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha_egreso')
    list_filter = ('cliente', 'fecha_egreso')

@admin.register(OrdenEgresoDetalle)
class OrdenEgresoDetalleAdmin(admin.ModelAdmin):
    list_display = ('id_orden_egreso', 'especie','variedad','calidad' ,'cantidad')
    list_filter = ('id_orden_egreso__cliente', 'especie','variedad')
    
# Cuenta detallada
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'telephone', 'user_group')
    list_filter = ('user__groups',)

    def user_group(self, obj):
        return " - ".join([t.name for t in obj.user.groups.all().order_by('name')])
    
    user_group.short_description = "Grupo"
    
# Ver las cuentas en la parte administrativa, requiere de .models import Account
admin.site.register(Account, AccountAdmin)
