from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

def remisiones(request):
    remisiones_list = Remision_clie.objects.all()
    busquedaform = RemisionBusqueda()
    context ={
        'remisiones_list': remisiones_list,
        'busquedaform': busquedaform
    }
    if request.method == 'POST':
        busquedaform = RemisionBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Remision_clie.objects.all()
            data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
            data = data.filter(factura_cliente__factura__id=busquedaform.cleaned_data['factura'])  if busquedaform.cleaned_data['factura'] else data
            data = data.filter(factura_cliente__codcliente__persona__nombre=busquedaform.cleaned_data['cliente'])  if busquedaform.cleaned_data['cliente'] else data
            context['remisiones_list']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = RemisionBusqueda()
    return render(request, "Remisiones/estructura_crud_rem.html",context)

def agregar_remision(request,id):
    enviado = False
    productos_list = Factura_linea_clie.objects.filter(factura_cliente__factura__id=id)
    if request.method == 'POST':
        in_remision_per = NuevaRemision(request.POST)
        if in_remision_per.is_valid():
            in_remision_per.save()
            return HttpResponseRedirect('agregarrem?enviado=True')
    else:
        in_remision_per= NuevaRemision()
        if 'enviado' in request.GET:
            enviado = True
    context = {
        'productos_list':productos_list,
        'in_remision_per':in_remision_per,
        'enviado':enviado, 
    }
    return render(request, "Remisiones/formulario_insertar_remision.html", context)

def editar_remision(request, id): 
    return

def ver_remision(request, id):
    return

def eliminar_remision(request, id):
    return