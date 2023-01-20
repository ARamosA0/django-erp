from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

def orden_compra_servicio(request):
    compra_servicios_list = Servicio_compra.objects.all()
    
    context = {
        'compra_servicios_list':compra_servicios_list,
    }

    return render(request, 'CompraServicios/estructura_crud_compraservicios.html', context)

def agregar_orden_compra_servicio(request):
    enviado = False
    if request.method == 'POST':
        in_compra_servicios_per = AgregarOrdenServicio(request.POST)
        if in_compra_servicios_per.is_valid():
            in_compra_servicios_per.save()
            return HttpResponseRedirect('agregarservicio?enviado=True')
    else:
        in_compra_servicios_per = AgregarOrdenServicio()
        if 'enviado' in request.GET:
            enviado = True
    context = {
        'in_compra_servicios_per':in_compra_servicios_per,
        'enviado':enviado, 
    }
    return render(request, "CompraServicios/formulario_insertar_compraservicio.html", context)

def ver_orden_compra_servicio(request, id):
    servicio_list = Servicio_compra.objects.get(id=id)
    context = {
        'serv': servicio_list
    }
    return render(request, "CompraServicios/compraservicio.html", context)

def editar_orden_compra_servicio(request, id):
    pass

def eliminar_orden_compra_servicio(request, id):
    pass