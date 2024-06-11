from django.contrib import admin
from .models import TablaCliente, TablaProv, TablaVariedad, TablaEspecie, Account
#from .models import Account


# Register your models here.
admin.site.register(TablaCliente) #PERMISO PARA AÑADIR REGISTROS DE CLIENTE COMO ADMIN
admin.site.register(TablaProv) #PERMISO PARA AÑADIR REGISTROS DE PROVEEDORES COMO ADMIN
admin.site.register(TablaVariedad) #PERMISO PARA AÑADIR REGISTROS DE VARIEDAD COMO ADMIN
admin.site.register(TablaEspecie) #PERMISO PARA AÑADIR REGISTROS DE ESPECIE COMO ADMIN

# Cuenta detallada
class AccountAdmin(admin.ModelAdmin):
	list_display=('user', 'telephone', 'user_group')
	list_filter = ('user__groups',)
	def user_group(self, obj):
		return " - ".join([t.name for t in obj.user.groups.all().order_by('name')])
	
	user_group.short_description = "Grupo"
	
# Ver las cuenas en la parte administrativa, requiere de .models improt Account
admin.site.register(Account, AccountAdmin)

