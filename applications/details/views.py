from django.shortcuts import render
from . models import Edificio, Cliente

# Create your views here.
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
)

class IndexView(ListView):
    template_name = "../templates/sketch.html"
    model = Cliente 
    context_object_name = 'clientes'

""" class ClientsView(ListView):
    template_name = "../templates/sketch.html"
    #model = Cliente #Este se borra :u
    context_object_name = 'clientes'

    def get_queryset(self):
        #Identificar el cliente
        id = self.kwargs['pk']
        #add /<pk>/ al url 
        #Filtrar los datos
        #print('**************************************', id)
        lista = Cliente.objects.filter(
            Nombre=id
        )
        #Devolver el resultado
        return lista """