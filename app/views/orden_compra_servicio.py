from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

#Relacionado a la orden de compra
def orden_compra_servicio(request):
    compra_servicios_list = Orden_compra_servicio.objects.all()
    
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
    orden_compra_list = Orden_compra_servicio.objects.get(id=id)
    orden_compra_servicio_list = Servicio_compra.objects.filter(orden_compra=id)

    context = {
        'orden_compra': orden_compra_list,
        'servicios': orden_compra_servicio_list
    }
    return render(request, "CompraServicios/compraservicio.html", context)

def editar_orden_compra_servicio(request, id):
    orden_compra_list = Orden_compra_servicio.objects.get(id=id)
    orden_compra_servicio_list = Servicio_compra.objects.filter(orden_compra=id)
    
    context = {
        'orden_compra_list': orden_compra_list,
        'servicios': orden_compra_servicio_list
    }
    return render(request, "CompraServicios/editar_compraservicio.html", context)

def editar_datos_generales_orden_compra(request, id):
    orden_compra_put = Orden_compra_servicio.objects.get(id=id)
    in_compra_servicios_per = AgregarOrdenServicio(request.POST or None, instance=orden_compra_put)
    if in_compra_servicios_per.is_valid():
        in_compra_servicios_per.save()       
        return redirect('peserv')
    context = {
        'in_compra_servicios_per':in_compra_servicios_per,
    }    
    return render(request, "CompraServicios/formulario_insertar_compraservicio.html", context)

def eliminar_orden_compra_servicio(request, id):
    enviado = False
    del_orden_compra = Orden_compra_servicio.objects.filter(id=id)
    del_servicio_orden = Servicio_compra.objects.filter(orden_compra=id)

    red = request.POST.get('peserv','/erp/compraservicio/')
    if request.method =="POST":
        for i in del_servicio_orden:
            i.delete()
            
        del_orden_compra.delete()
        return HttpResponseRedirect(red)
    context = {
        'enviado':enviado
    }
    return render(request, "CompraServicios/delete_compraservicio.html", context)

#Relacionado al servicio dentro de la orden de compra
def agregar_servicio_orden_compra(request):
    enviado = False
    if request.method == 'POST':
        in_servicio_orden_compra = AgregarServicioEnOrdenCompra(request.POST)
        if in_servicio_orden_compra.is_valid():
            in_servicio_orden_compra.save()
            return HttpResponseRedirect('agregarservicioenordencompra?enviado=True')
    else:
        in_servicio_orden_compra = AgregarServicioEnOrdenCompra()
        if 'enviado' in request.GET:
            enviado = True
    context = {
        'in_servicio_orden_compra':in_servicio_orden_compra,
        'enviado':enviado, 
    }
    return render(request, "CompraServicios/Servicios/formulario_insertar_servicioenordencompra.html", context)

def editar_servicio_orden_compra(request, id):
    orden_compra_servicio_put = Servicio_compra.objects.get(id=id)
    in_servicio_orden_compra = AgregarServicioEnOrdenCompra(request.POST or None, instance=orden_compra_servicio_put)
    if in_servicio_orden_compra.is_valid():
        in_servicio_orden_compra.save()       
        return redirect('peserv')
    context = {
        'in_servicio_orden_compra':in_servicio_orden_compra,
    }    
    return render(request, "CompraServicios/Servicios/formulario_insertar_servicioenordencompra.html", context)

def eliminar_servicio_orden_compra(request, id):
    del_servicio_orden = Servicio_compra.objects.get(id=id)
    del_servicio_orden.delete()

    return redirect('peserv')
