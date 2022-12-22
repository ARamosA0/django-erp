from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView, FormView
from .models import *

# Create your views here.



def proveedores(request):
    
    # proveedores_labels_serch = ['Nombre del proveedor', 'DNI del Proveedor']
    proveedores_list = Proveedores.objects.all()
    provincia_list = Provincias.objects.all()


    context ={
        'proveedores_list': proveedores_list,
        'provincia_list': provincia_list
    }
    return render(request, "Pag/proveedores.html", context)
  

def insertar_proveedor(request):
    return render(request,"formulario_insertar_proveedor.html")
