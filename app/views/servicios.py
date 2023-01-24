from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

def servicios(request):
    servicios_list = Servicios.objects.all()
    
    context = {
        'servicios_list':servicios_list,
    }

    return render(request, 'Servicios/estructura_crud_servicios.html', context)

def agregar_servicios(request):
    enviado = False
    if request.method == 'POST':
        in_servicios_per = AgregarServicio(request.POST)
        if in_servicios_per.is_valid():
            in_servicios_per.save()
            return HttpResponseRedirect('agregarservicio?enviado=True')
    else:
        in_servicios_per = AgregarServicio()
        if 'enviado' in request.GET:
            enviado = True
    context = {
        'in_servicios_per':in_servicios_per,
        'enviado':enviado, 
    }
    return render(request, "Servicios/formulario_insertar_servicio.html", context)

def ver_servicio(request, id):
    servicio_list = Servicios.objects.get(id=id)
    context = {
        'serv': servicio_list
    }
    return render(request, "Servicios/servicio.html", context)

def editar_servicio(request, id):
    servicio_put = Servicios.objects.get(id=id)
    in_servicios_per = AgregarServicio(request.POST or None, instance=servicio_put)
    if in_servicios_per.is_valid():
        in_servicios_per.save()       
        return redirect('serv')
    context = {
        'in_servicios_per':in_servicios_per,
    }    
    return render(request, "Servicios/formulario_insertar_servicio.html", context)

def eliminar_servicio(request, id):
    enviado = False
    del_servicio = Servicios.objects.filter(id=id)
    red = request.POST.get('serv','/erp/servicios/')
    if request.method =="POST":
        del_servicio.delete()
        return HttpResponseRedirect(red)
    context = {
        'enviado':enviado
    }
    return render(request, "Servicios/delete_servicio.html", context)
