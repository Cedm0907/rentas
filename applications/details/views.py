from django.shortcuts import render
from . models import Edificio, Cliente

# Create your views here.
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
)

class Clientsview(TemplateView):
    #print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Prueba')
    template_name = "../templates/sketch.html"
    model = Edificio
    context_object_name = 'clientes'
