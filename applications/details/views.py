from django.shortcuts import render
from . models import Edificio, Cliente

# Create your views here.
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
)

class ClientsView(ListView):
    template_name = "../templates/sketch.html"
    model = Cliente
    context_object_name = 'clientes'

    print(context_object_name)
