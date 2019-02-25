from django.db import models
from django.core.validators import MinValueValidator

class Edificio(models.Model):
    Nombre = models.CharField('Nombre', max_length = 80, blank = True) 
    Nivel = models.PositiveIntegerField('Nivel', blank = True)
    Metros = models.DecimalField(verbose_name=u'Metros', max_digits = 5, decimal_places = 2, validators = [MinValueValidator(0.0)])

    def __str__(self):  
       return str(self.Nivel)

class Nivel(models.Model):
    Nivel = models.ForeignKey(Edificio, on_delete = models.CASCADE, default = None)
    #Metros = models.ForeignKey(Metros, on_delete = models.CASCADE, default = None)
    Metros = models.DecimalField( verbose_name=u'Metros', max_digits = 5, decimal_places = 2, validators = [MinValueValidator(0.0)])
    Sanitarios = models.PositiveIntegerField('Número de Baños', blank = True)
    #Plano = models.FileField(upload_to = None)

class Impuestos(models.Model):
    Nombre = models.CharField('Nombre del impuesto', max_length = 80, default = None)
    Porcentaje = models.PositiveIntegerField('Cuota (%)', blank = True)
        
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
    Cajon = models.PositiveIntegerField('Cajón Número', blank = True, default=None)

    def __str__(self):
        return (self.Cajon)

class Cliente(models.Model):
    Nombre = models.CharField('Razón Social | Nombre', default = None, max_length = 80)
    email = models.EmailField('Correo electrónico', max_length = 100)
    direccion = models.CharField('Domicilio', default = None, max_length = 300)
    #id_contrato

    def __str__(self):
        return (self.Nombre)

class Contrato(models.Model):
    Folio = models.CharField('Folio de contrato', default = None, max_length = 80)
    Metros_contratados = models.PositiveIntegerField('Metros arrendados', blank = True)
    Precio_Metro = models.DecimalField(verbose_name=u'Precio por metro cuadrado', max_digits = 5, decimal_places = 2, validators = [MinValueValidator(0.0)])
    #cliente
    Cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE, default = None)
    #cajones
    Cajones = models.ForeignKey(Estacionamiento, on_delete = models.CASCADE, default = None)
    #impuestos
    Impuesto = models.ForeignKey(Impuestos, on_delete = models.CASCADE, default = None)
    #nivel
    Nivel = models.ForeignKey(Edificio, on_delete = models.CASCADE, default = None)

    def __str__(self):
        return (self.Folio)