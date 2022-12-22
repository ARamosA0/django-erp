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

def find_test(request):
    
    data = data = Proveedores.objects.values('pk','persona_id','persona_id__nombre',
                                             'persona_id__dni','persona_id__localidad',
                                             'persona_id__direccion','persona_id__codpostal',
                                             'persona_id__cuentabancaria','persona_id__telefono',
                                             'persona_id__movil','persona_id__web',
                                             'persona_id__codprovincia_id').filter(borrado='0')
    
    data = data.filter(pk=request.POST['codigo'])  if request.POST['codigo'] else data
    data = data.filter(persona_id__dni=request.POST['dni'])  if request.POST['dni'] else data
    data = data.filter(persona_id__nombre=request.POST['nombre'])  if request.POST['nombre'] else data
    data = data.filter(persona_id__telefono=request.POST['telefono'])  if request.POST['telefono'] else data
    data = data.filter(persona_id__codprovincia_id=request.POST['provincia'])  if request.POST['provincia']!='0' else data
    data = data.filter(persona_id__localidad=request.POST['localidad'])  if request.POST['localidad'] else data
    data = data.filter(persona_id__web=request.POST['web'])  if request.POST['web'] else data
    
    context = {'proveedores': data}
    #print(data)
    return  render(request,"find_test.html",context)
