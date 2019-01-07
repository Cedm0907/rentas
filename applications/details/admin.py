from django.contrib import admin

# Register your models here.

from .models import Edificio, Nivel, Impuestos, Estacionamiento, Contrato

class AdminEdificios(admin.ModelAdmin):
  list_display = (
    'id',
    'Nivel',
    'Metros'
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


admin.site.register(Edificio, AdminEdificios)
admin.site.register(Nivel, AdminNiveles)
admin.site.register(Impuestos, AdminImpuestos)
admin.site.register(Estacionamiento, AdminEstacionamiento)
admin.site.register(Contrato, AdminContrato)