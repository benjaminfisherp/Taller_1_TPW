from django.db import models

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
    especie = models.CharField(max_length=100, null=False, unique=True)

#TABLA VARIEDAD
class TablaVariedad(models.Model):
    variedad = models.CharField(max_length=100, null=False, unique=True)

#TABLA FRUTAS
class TablaFruta(models.Model): #Cambiar
    codigo = models.CharField(max_length=100, primary_key=True)
    especie = models.ForeignKey(TablaEspecie, on_delete=models.CASCADE, to_field='especie')
    variedad = models.ForeignKey(TablaVariedad, on_delete=models.CASCADE, to_field='variedad')
    calidad = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.especie
    
#MODELOS AÚN NO IMPLEMENTADOS-----------------------------------------------------------------------------------------------------

#ORDEN DE EGRESO DE FRUTA
class Egreso(models.Model):

    #egr <- egreso
    rut_prov_egr = models.ForeignKey(TablaCliente, on_delete=models.CASCADE, to_field='rut')
    codigo_fruta_egr = models.ForeignKey(TablaFruta, on_delete=models.CASCADE, to_field='codigo')
    order_date_egr = models.DateTimeField()
    total_amount_egr = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return f'Order {self.id} from {self.rut_prov_ing.name}'
    
#ORDEN DE INGRESO DE FRUTA
class Ingreso(models.Model):
    
    #ing <- ingreso
    rut_prov_ing = models.ForeignKey(TablaProv, on_delete=models.CASCADE, to_field='rut_prov')
    codigo_fruta_ing = models.ForeignKey(TablaFruta, on_delete=models.CASCADE, to_field='codigo')
    order_date_ing = models.DateTimeField()
    total_amount_ing = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return f'Order {self.id} from {self.rut_prov_ord.name_prov}'