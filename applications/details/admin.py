from django.contrib import admin

# Register your models here.

from . models import Edificio, Nivel, Impuestos, Estacionamiento, Contrato, Cliente

class AdminEdificios(admin.ModelAdmin):
  list_display = (
    'id',
    'Nombre',
    'Nivel',
    'Metros'
    )
  list_filter = (
    'id',
    'Nivel'
  )

class AdminNiveles(admin.ModelAdmin):
  list_display = (
    'id',
    'Nivel',
    'Sanitarios',
    'Metros'
    #'Plano'
  )

class AdminImpuestos(admin.ModelAdmin):
  list_display = (
    'id',
    'Nombre'
    )

class AdminEstacionamiento(admin.ModelAdmin):
  list_display = (
    'id',
    'UsoCajon'
  )

class AdminClientes(admin.ModelAdmin):
  list_display = (
    'id',
    'Nombre',
    'email',
    'direccion'
  )

class AdminContrato(admin.ModelAdmin):
  list_display = (
    'id',
    'Folio',
    'Metros_contratados',
    'Precio_Metro',
    'Cliente',
    'Fecha_i',
    'Fecha_f',
    #'Cajones',
    #'Nombre',
    'Nivel'
  )

admin.site.register(Edificio, AdminEdificios)
admin.site.register(Nivel, AdminNiveles)
admin.site.register(Impuestos, AdminImpuestos)
admin.site.register(Estacionamiento, AdminEstacionamiento)
admin.site.register(Contrato, AdminContrato)
admin.site.register(Cliente, AdminClientes)


