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
    Nombre = models.CharField('Nombre del impuesto', max_length = 80, default = "%")
    Porcentaje = models.DecimalField('Valor', max_digits = 5, decimal_places = 2, default = 0, null = True, blank=True)
    
    def __str__(self):  
        return str(self.Nombre)

    '''def get_impuestos(self):
        return "\n".join([i.Impuestos for i in self.Impuestos.all()])'''

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
    Cajon = models.CharField('Cajón Número', max_length=1, blank = True, default=None)

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
    Precio_Metro = models.DecimalField(verbose_name=u'Precio por metro cuadrado', max_digits = 5, decimal_places = 2, default= None, validators = [MinValueValidator(0.0)])
    #cliente
    Cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE, default = None)
    #cajones
    #Cajones = models.ForeignKey(Estacionamiento, on_delete = models.CASCADE, default = None)
    Cajon = models.ManyToManyField('Estacionamiento', max_length = 80, blank=True)
    #impuestos
    Nombre = models.ManyToManyField('Impuestos', max_length = 80, blank=True)
    #nivel
    Nivel = models.ForeignKey(Edificio, on_delete = models.CASCADE, default = None)

    def __str__(self):
        return (self.Folio)



#Many to many fields: https://www.revsys.com/tidbits/tips-using-djangos-manytomanyfield/        