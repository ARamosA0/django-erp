from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

def entidad(request):
    entidades_list = Entidades.objects.all()
    busquedaform = EntidadBusqueda()
    context ={
        'entidades_list': entidades_list,
        'contador':len(entidades_list),
        'busquedaform': busquedaform
    }
    if request.method == 'POST':
        busquedaform = EntidadBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Entidades.objects.all()
            data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
            data = data.filter(nombreentidad=busquedaform.cleaned_data['nombreentidad'])  if busquedaform.cleaned_data['nombreentidad'] else data
            context['entidades_list']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = EntidadBusqueda()
    return render(request, "Entidades/estructura_crud_ent.html",context)

def agregar_entidad(request):
    enviado = False
    if request.method == 'POST':
        in_entidades_per = AgregarEntidad(request.POST)
        if in_entidades_per.is_valid():
            in_entidades_per.save()
            return HttpResponseRedirect('agregarent?enviado=True')
    else:
        in_entidades_per= AgregarEntidad()
        if 'enviado' in request.GET:
            enviado = True
    context = {
        'in_entidades_per':in_entidades_per,
        'enviado':enviado, 
    }
    return render(request, "Entidades/formulario_insertar_entidad.html", context)

def editar_entidad(request, id):
    entidad_put = Entidades.objects.get(id=id)
    in_entidades_per = AgregarEntidad(request.POST or None, instance=entidad_put)
    if in_entidades_per.is_valid():
            in_entidades_per.save()       
            return redirect('ent')
    
    context = {
        'in_entidades_per':in_entidades_per,
    }    
    return render(request, "Entidades/formulario_insertar_entidad.html", context)

def ver_entidad(request,id):
    entidad_list = Entidades.objects.get(id=id)
    context = {
        'ent': entidad_list
    }
    return render(request, "Entidades/entidad.html", context)
    
def eliminar_entidad(request,id):
    enviado = False
    del_entidad = Entidades.objects.filter(id=id)
    red = request.POST.get('ent','/erp/ent/')
    if request.method =="POST":
        del_entidad.delete()
        return HttpResponseRedirect(red)
    context = {
        'enviado':enviado
    }
    return render(request, "Entidades/delete_entidad.html", context)
    