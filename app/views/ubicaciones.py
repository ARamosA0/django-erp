from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

def ubicaciones(request):
    ubicaciones_list = Ubicaciones.objects.all()
    busquedaform = UbicacionesBusqueda()
    context ={
        'ubicaciones_list': ubicaciones_list,
        'busquedaform': busquedaform
    }
    if request.method == 'POST':
        busquedaform = UbicacionesBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Ubicaciones.objects.all()
            data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
            data = data.filter(nombre=busquedaform.cleaned_data['nombre'])  if busquedaform.cleaned_data['nombre'] else data
            context['ubicaciones_list']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = UbicacionesBusqueda()
    return render(request, "Ubicaciones/estructura_crud_ubi.html",context)

def agregar_ubicacion(request):
    enviado = False
    if request.method == 'POST':
        in_ubicaciones_per = AgregarUbicaciones(request.POST)
        if in_ubicaciones_per.is_valid():
            in_ubicaciones_per.save()
            return HttpResponseRedirect('agregarubi?enviado=True')
    else:
        in_ubicaciones_per= AgregarUbicaciones()
        if 'enviado' in request.GET:
            enviado = True
    context = {
        'in_ubicaciones_per':in_ubicaciones_per,
        'enviado':enviado, 
    }
    return render(request, "Ubicaciones/formulario_insertar_ubicacion.html", context)

def ver_ubicacion(request,id):
    ubicacion_list = Ubicaciones.objects.get(id=id)
    context = {
        'ubi': ubicacion_list
    }
    return render(request, "Ubicaciones/ubicacion.html", context)

def editar_ubicacion(request, id):
    ubicacion_put = Ubicaciones.objects.get(id=id)
    in_ubicaciones_per = AgregarUbicaciones(request.POST or None, instance=ubicacion_put)
    if in_ubicaciones_per.is_valid():
            in_ubicaciones_per.save()       
            return redirect('ubi')
    context = {
        'in_ubicaciones_per':in_ubicaciones_per,
    }    
    return render(request, "Ubicaciones/formulario_insertar_ubicacion.html", context)

def eliminar_ubicacion(request,id):
    enviado = False
    del_ubicacion = Ubicaciones.objects.filter(id=id)
    red = request.POST.get('ubi','/erp/ubi/')
    if request.method =="POST":
        del_ubicacion.delete()
        return HttpResponseRedirect(red)
    context = {
        'enviado':enviado
    }
    return render(request, "Ubicaciones/delete_ubicacion.html", context)
