from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def crud(request):
    proveedores_list = Proveedores.objects.all()
    context = {
        'proveedores_list': proveedores_list
    }
    return render(request,"estructura_crud.html", context)

def busqueda(request, response):
    if(request.GET["prd"]):
        return render(request, 'estructura_crud.html') 
    return HttpResponse('<h1>fallo</h1>')   

def insertar_proveedor(request):
    return render(request,"formulario_insertar_proveedor.html")