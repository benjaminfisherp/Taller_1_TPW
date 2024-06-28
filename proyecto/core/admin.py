from django.contrib import admin
from .models import TablaCliente, TablaProv, TablaVariedad, TablaEspecie, Account, Ingreso, Egreso

# Register your models here.
admin.site.register(TablaVariedad)  # PERMISO PARA AÑADIR REGISTROS DE VARIEDAD COMO ADMIN
admin.site.register(TablaEspecie)  # PERMISO PARA AÑADIR REGISTROS DE ESPECIE COMO ADMIN
admin.site.register(Ingreso)  # PERMISO PARA AÑADIR REGISTROS DE INGRESO COMO ADMIN
admin.site.register(Egreso)  # PERMISO PARA AÑADIR REGISTROS DE EGRESO COMO ADMIN

@admin.register(TablaProv)
class TablaProvAdmin(admin.ModelAdmin):
    list_display = ('name_prov', 'rut_prov', 'correo_prov', 'telefono_prov', 'razon_social_prov', 'direccion_prov', 'region_prov', 'comuna_prov', 'ncontacto_prov')
    search_fields = ('name_prov', 'rut_prov', 'correo_prov')
    list_filter = ('region_prov', 'comuna_prov')

@admin.register(TablaCliente)
class TablaClienteAdmin(admin.ModelAdmin):
	list_display = ('name', 'rut', 'correo', 'telefono', 'razon_social')
	search_fields = ('name', 'rut', 'correo')


# Cuenta detallada
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'telephone', 'user_group')
    list_filter = ('user__groups',)

    def user_group(self, obj):
        return " - ".join([t.name for t in obj.user.groups.all().order_by('name')])
    
    user_group.short_description = "Grupo"
    
# Ver las cuentas en la parte administrativa, requiere de .models import Account
admin.site.register(Account, AccountAdmin)
