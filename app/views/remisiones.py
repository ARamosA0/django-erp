from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

def remisiones(request):
    albaranes_list = Remision_linea_clie.objects.all()
    busquedaform = RemisionBusqueda()
    context ={
        'albaranes_list': albaranes_list,
        'busquedaform': busquedaform
    }
    if request.method == 'POST':
        busquedaform = RemisionBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Remision_linea_clie.objects.all()
            data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
            data = data.filter(cliente__factura_cliente__factura__id=busquedaform.cleaned_data['factura'])  if busquedaform.cleaned_data['factura'] else data
            #data = data.filter(cliente__factura_cliente__codcliente__persona__dni=busquedaform.cleaned_data['dni'])  if busquedaform.cleaned_data['dni'] else data
            data = data.filter(cliente__factura_cliente__codcliente__persona__nombre=busquedaform.cleaned_data['cliente'])  if busquedaform.cleaned_data['cliente'] else data
            context['albaranes_list']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = RemisionBusqueda()
    return render(request, "Remisiones/estructura_crud_rem.html",context)

def agregar_remision(request):
    return

def editar_remision(request, id): 
    return

def ver_remision(request, id):
    return

def eliminar_remision(request, id):
    return