from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def crud(request):
    proveedores_list = Proveedores.objects.all()
    provincia_lista = Provincias.objects.all()
    print(provincia_lista)
    context = {
        'proveedores_list': proveedores_list,
        'provincia_lista': provincia_lista
    }
    return render(request,"estructura_crud.html", context)


    

def form_busqueda(request):

    # provincia_lista = Provincias.objects.all()

    # context = {
    #     'provincia_lista': provincia_lista
    # }

    return render(request,"formulario_busqueda.html", context)  

def insertar_proveedor(request):
    return render(request,"formulario_insertar_proveedor.html")