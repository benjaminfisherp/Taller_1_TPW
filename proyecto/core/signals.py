# ejecuta la operacion de apenas le llegue una solicitud de creacioin de cuenta lo envie a la asignacion de algun grupo autimaticamente
#se importan los grupos (modelos)
from django.contrib.auth.models import Group

#se importa el modelo account
from .models import Account

# se importa un receive o señal o solicitudes mediante un decorador
from django.dispatch import receiver
from django.db.models.signals import post_save

# se instancia el decorador
@receiver(post_save, sender=Account)
def add_user_to_user_group(sender, instance, created, **kwargs): #se define la funcion de agregar usuaruio a grupo detemrinado
	if created:
		try:
			users_account = Group.objects.get(name='Usuarios')
		except Group.DoesNotExist:
			users_account = Group.objects.create(name='Usuarios')
			users_account = Group.objects.create(name='Administrativos')
			
		instance.user.groups.add(users_account)