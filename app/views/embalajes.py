from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

def embalajes(request):
    embalajes_list = Embalajes.objects.all()
    busquedaform = EmbalajeBusqueda()
    context ={
        'embalajes_list': embalajes_list,
        'contador':len(embalajes_list),
        'busquedaform': busquedaform
    }
    if request.method == 'POST':
        busquedaform = EmbalajeBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Embalajes.objects.all()
            data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
            data = data.filter(nombre=busquedaform.cleaned_data['nombre'])  if busquedaform.cleaned_data['nombre'] else data
            context['embalajes_list']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = EmbalajeBusqueda()
    return render(request, "Embalajes/estructura_crud_emb.html",context)

def agregar_embalaje(request):
    enviado = False
    if request.method == 'POST':
        in_embalaje_per = AgregarEmbalaje(request.POST)
        if in_embalaje_per.is_valid():
            in_embalaje_per.save()
            return HttpResponseRedirect('agregaremb?enviado=True')
    else:
        in_embalaje_per= AgregarEmbalaje()
        if 'enviado' in request.GET:
            enviado = True
    context = {
        'in_embalaje_per':in_embalaje_per,
        'enviado':enviado, 
    }
    return render(request, "Embalajes/formulario_insertar_embalaje.html", context)

def ver_embalaje(request,id):
    embalaje_list = Embalajes.objects.get(id=id)
    context = {
        'emb': embalaje_list
    }
    return render(request, "Embalajes/embalaje.html", context)

def editar_embalaje(request, id):  
    embalaje_put = Embalajes.objects.get(id=id)
    in_embalaje_per = AgregarEmbalaje(request.POST or None, instance=embalaje_put)
    if in_embalaje_per.is_valid():
            in_embalaje_per.save()       
            return redirect('emb')
    
    context = {
        'in_embalaje_per':in_embalaje_per,
    }    
    return render(request, "Embalajes/formulario_insertar_embalaje.html", context)

def eliminar_embalaje(request,id):
    enviado = False
    del_embalaje = Embalajes.objects.filter(id=id)
    red = request.POST.get('emb','/erp/emb/')
    if request.method =="POST":
        del_embalaje.delete()
        return HttpResponseRedirect(red)
    context = {
        'enviado':enviado
    }
    return render(request, "Embalajes/delete_embalaje.html", context)
