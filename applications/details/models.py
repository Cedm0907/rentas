from django.db import models

# Create your models here.

class Edificio(models.Model):
    Nombre = models.CharField('Nombre', max_length = 80, blank = True) 
    Nivel = models.CharField('Nivel', max_length = 80, blank = True)
    Metros = models.FloatField('Metros', max_length = 80, blank = True)

    def __str__(self):  
       return str(self.Nivel)

class Nivel(models.Model):
    Nivel = models.ForeignKey(Edificio, on_delete = models.CASCADE, default = None)
    #Metros = models.ForeignKey(Metros, on_delete = models.CASCADE, default = None)
    Metros = models.DecimalField('Metros', max_length = 80, blank = True, max_digits = 6, decimal_places = 2)
    Sanitarios = models.IntegerField('Número de Baños', blank = True)
    #Plano = models.FileField(upload_to = None)

class Impuestos(models.Model):
    Nombre = models.CharField('Nombre del impuesto', max_length = 80, default = None)
    Porcentaje = models.IntegerField('Cuota (%)', blank = True)
        
    def __str__(self):  
       return str(self.Nombre)

class Estacionamiento(models.Model):
    Contrato = 'PC'
    Pension = 'PS'
    Hora = 'HR'
    Uso_Cajon_Choices = (
        (Contrato, 'Contrato'),
        (Pension, 'Pensión'),
        (Hora, 'Renta por Hora'),
    )
    UsoCajon = models.CharField('Uso de cajón', choices = Uso_Cajon_Choices, default = Contrato, max_length = 80)

    def __str__(self):
        return (self.UsoCajon)

class Contrato(models.Model):
    Folio = models.CharField('Número de contrato', default = None, max_length = 80)
    Metros_contratados = models.IntegerField('Metros arrendados', blank = True)
    Precio_metro = models.DecimalField('Precio por metro cuadrado', max_length = 80, blank = True, max_digits = 6, decimal_places = 2)
    
    def __get_importe__(self):
        return self.Metros_contratados*self.Precio_metro
    importe = property (__get_importe__)
