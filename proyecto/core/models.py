from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

#TABLA DE CLIENTES
class TablaCliente(models.Model):
    name = models.CharField(max_length=100, null=False)
    rut = models.CharField(max_length=100, primary_key=True)
    correo = models.EmailField(null=False, blank=False)
    telefono = models.IntegerField(unique=True) 
    razon_social = models.CharField(max_length=100,default=' - ')

    def __str__(self):
        return self.rut

#TABLA DE PROVEEDORES
class TablaProv(models.Model):
    name_prov = models.CharField(max_length=100)
    rut_prov = models.CharField(max_length=100, primary_key=True)
    correo_prov = models.EmailField(null=False, blank=False)
    telefono_prov = models.IntegerField(unique=True) 
    razon_social_prov = models.CharField(max_length=100, default=" - ")
    direccion_prov = models.CharField(max_length=100, null=False)
    region_prov = models.CharField(max_length=100, null=False)
    comuna_prov =  models.CharField(max_length=100, null=False)
    ncontacto_prov = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.rut_prov

#TABLA ESPECIE
class TablaEspecie(models.Model):
    especie = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.especie

#TABLA VARIEDAD
class TablaVariedad(models.Model):
    variedad = models.CharField(max_length=100, primary_key=True)
    especie = models.ForeignKey(TablaEspecie, on_delete=models.CASCADE, to_field='especie')

    def __str__(self):
        return self.variedad

#MODELOS AÚN NO IMPLEMENTADOS-----------------------------------------------------------------------------------------------------

#ORDEN DE EGRESO DE FRUTA
class Egreso(models.Model):

    #egr <- egreso
    rut_prov_egr = models.ForeignKey(TablaCliente, on_delete=models.CASCADE, to_field='rut')
    codigo_fruta_egr = models.CharField(max_length=100)
    order_date_egr = models.DateTimeField()
    total_amount_egr = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return self.id
    
#ORDEN DE INGRESO DE FRUTA
class Ingreso(models.Model):
    
    #ing <- ingreso
    rut_prov_ing = models.ForeignKey(TablaProv, on_delete=models.CASCADE, to_field='rut_prov')
    codigo_fruta_ing = models.CharField(max_length=100)
    order_date_ing = models.DateTimeField()
    total_amount_ing = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return self.id
    

# MODELOS ORIENTADOS A LOS ROLES------------------------------------------

# cuenta de usuario
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account', verbose_name='Usuario')
    telephone = models.CharField(max_length=50, null=True, blank=True, verbose_name='Telefono')
    class Meta:
        verbose_name='usuario'
        verbose_name_plural='usuarios'
        ordering = ['-id']
    def __str__(self):
        return self.user.username
    
def create_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)
        
def save_user_account(sender, instance, **kwargs):
    instance.account.save()
    
post_save.connect(create_user_account, sender=User)
post_save.connect(save_user_account, sender=User)
