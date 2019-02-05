from django.contrib import admin

# Register your models here.

from .models import Edificio, Nivel, Impuestos, Estacionamiento, Contrato, Cliente

class AdminEdificios(admin.ModelAdmin):
  list_display = (
    'id',
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
    'Nombre',
    'Porcentaje'
  )

class AdminEstacionamiento(admin.ModelAdmin):
  list_display = (
    'id',
    'UsoCajon'
  )

class AdminContrato(admin.ModelAdmin):
  list_display = (
    'id',
    'Folio',
    'Metros_contratados',
    'Precio_metro',
    'importe'
  )

class AdminClientes(admin.ModelAdmin):
  list_display = (
    'id',
    'Nombre',
    'email',
    'direccion'
  )


admin.site.register(Edificio, AdminEdificios)
admin.site.register(Nivel, AdminNiveles)
admin.site.register(Impuestos, AdminImpuestos)
admin.site.register(Estacionamiento, AdminEstacionamiento)
admin.site.register(Contrato, AdminContrato)
admin.site.register(Cliente, AdminClientes)