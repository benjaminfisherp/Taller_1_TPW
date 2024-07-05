from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser, Group, Permission

#TABLA DE CLIENTES
class TablaCliente(models.Model):
    name = models.CharField(max_length=100, null=False)
    rut = models.CharField(max_length=100, unique=True)
    correo = models.EmailField(null=False, blank=False)
    telefono = models.IntegerField(unique=False) 
    razon_social = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.rut

#TABLA DE PROVEEDORES
class TablaProv(models.Model):
    name_prov = models.CharField(max_length=100)
    rut_prov = models.CharField(max_length=100, unique=True)
    correo_prov = models.EmailField(null=False, blank=False)
    telefono_prov = models.IntegerField(unique=False) 
    razon_social_prov = models.CharField(max_length=100)
    direccion_prov = models.CharField(max_length=100, null=False)
    region_prov = models.CharField(max_length=100, null=False)
    comuna_prov =  models.CharField(max_length=100, null=False)
    ncontacto_prov = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.rut_prov

#TABLA ESPECIE
class TablaEspecie(models.Model):
    especie = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.especie
    
# TABLA CALIDAD
class TablaCalidad(models.Model):
    calidad = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return f"{self.id} - {self.calidad}"
    
#TABLA VARIEDAD
class TablaVariedad(models.Model):
    variedad = models.CharField(max_length=100, unique=True)
    especie = models.ForeignKey(TablaEspecie, on_delete=models.CASCADE, to_field='especie')

    def __str__(self):
        return self.variedad

# ORDEN DE INGRESO DE FRUTA
class OrdenIngreso(models.Model):
    proveedor = models.ForeignKey(TablaProv, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return f"{self.id} - {self.proveedor.rut_prov} - {self.proveedor.name_prov}"
    
class OrdenIngresoDetalle(models.Model):
    id_orden_ingreso = models.ForeignKey(OrdenIngreso, on_delete=models.CASCADE)
    especie = models.ForeignKey(TablaEspecie, on_delete=models.CASCADE)
    variedad = models.ForeignKey(TablaVariedad, on_delete=models.CASCADE)
    calidad = models.ForeignKey(TablaCalidad, on_delete=models.CASCADE)
    cantidad = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{self.id_orden_ingreso.proveedor} - {self.id_orden_ingreso.proveedor.name_prov}" 
    
# ORDEN DE EGRESO DE FRUTA
class OrdenEgreso(models.Model):
    cliente = models.ForeignKey(TablaCliente, on_delete=models.CASCADE)
    fecha_egreso = models.DateField()

    def __str__(self):
        return f"{self.id} - {self.cliente.rut} - {self.cliente.name}"

class OrdenEgresoDetalle(models.Model):
    id_orden_egreso = models.ForeignKey(OrdenEgreso, on_delete=models.CASCADE)
    especie = models.ForeignKey(TablaEspecie, on_delete=models.CASCADE)
    variedad = models.ForeignKey(TablaVariedad, on_delete=models.CASCADE)
    calidad = models.ForeignKey(TablaCalidad, on_delete=models.CASCADE)
    cantidad = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{self.id_orden_egreso.cliente} - {self.id_orden_egreso.cliente.name}"
    
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

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',  # Cambia a un related_name único
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        verbose_name=('groups'),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',  # Cambia a un related_name único
        blank=True,
        help_text=('Specific permissions for this user.'),
        verbose_name=('user permissions'),
    )

    @property
    def is_administrativos(self):
        return self.groups.filter(name='Administrativos').exists()