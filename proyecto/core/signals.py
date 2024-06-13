# ejecuta la operacion de apenas le llegue una solicitud de creacioin de cuenta lo envie a la asignacion de algun grupo autimaticamente
#se importan los grupos (modelos)
from django.contrib.auth.models import Group

#se importa el modelo account
from .models import CustomUser

# se importa un receive o señal o solicitudes mediante un decorador
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=CustomUser)
def add_user_to_user_group(sender, instance, created, **kwargs):
    if created:
        try:
            users_account = Group.objects.get(name='Usuarios')
        except Group.DoesNotExist:
            users_account = Group.objects.create(name='Usuarios')
        
        try:
            admin_account = Group.objects.get(name='Administrativos')
        except Group.DoesNotExist:
            admin_account = Group.objects.create(name='Administrativos')
        
        instance.groups.add(users_account)

