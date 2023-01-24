from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

def provincia(request):
    provincias_list = Provincias.objects.all()
    busquedaform = ProvinciaBusqueda()
    context ={
        'provincias_list': provincias_list,
        'contador':len(provincias_list),
        'busquedaform': busquedaform
    }
    if request.method == 'POST':
        busquedaform = ProvinciaBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Provincias.objects.all()
            data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
            data = data.filter(nombreprovincia=busquedaform.cleaned_data['nombre'])  if busquedaform.cleaned_data['nombre'] else data
            context['provincias_list']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = ProvinciaBusqueda()
    return render(request, "Provincia/estructura_crud_provi.html",context)

def agregar_provincia(request):
    enviado = False
    if request.method == 'POST':
        in_provincia_per = AgregarProvincia(request.POST)
        if in_provincia_per.is_valid():
            in_provincia_per.save()
            return HttpResponseRedirect('agregarprovi?enviado=True')
    else:
        in_provincia_per= AgregarProvincia()
        if 'enviado' in request.GET:
            enviado = True
    context = {
        'in_provincia_per':in_provincia_per,
        'enviado':enviado, 
    }
    return render(request, "Provincia/formulario_insertar_provincia.html", context)

def ver_provincia(request,id):
    provincias_list = Provincias.objects.get(id=id)
    context = {
        'provi': provincias_list
    }
    return render(request, "Provincia/provincia.html", context)

def editar_provincia(request, id):
    provincia_put = Provincias.objects.get(id=id)
    in_provincia_per = AgregarProvincia(request.POST or None, instance=provincia_put)
    if in_provincia_per.is_valid():
            in_provincia_per.save()       
            return redirect('provi')
    context = {
        'in_provincia_per':in_provincia_per,
    }    
    return render(request, "Provincia/formulario_insertar_provincia.html", context)

def eliminar_provincia(request,id):
    enviado = False
    del_provincia = Provincias.objects.filter(id=id)
    red = request.POST.get('provi','/erp/provi/')
    if request.method =="POST":
        del_provincia.delete()
        return HttpResponseRedirect(red)
    context = {
        'enviado':enviado
    }
    return render(request, "Provincia/delete_provincia.html", context)