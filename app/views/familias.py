from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *


def familias(request):
    familias_list = Familia.objects.all()
    busquedaform = FamiliaBusqueda()
    context ={
        'familias_list': familias_list,
        'contador':len(familias_list),
        'busquedaform': busquedaform
    }
    if request.method == 'POST':
        busquedaform = FamiliaBusqueda(request.POST)
        if busquedaform.is_valid():
            
            data = Familia.objects.all()
            data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
            data = data.filter(nombre=busquedaform.cleaned_data['nombre'])  if busquedaform.cleaned_data['nombre'] else data
            context['familias_list']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = FamiliaBusqueda()
    return render(request, "Familias/estructura_crud_fam.html",context)


def agregar_familia(request):
    enviado = False
    if request.method == 'POST':
        in_familia_per = AgregarFamilia(request.POST)
        if in_familia_per.is_valid():
            in_familia_per.save()
            return HttpResponseRedirect('agregarfam?enviado=True')
    else:
        in_familia_per= AgregarFamilia()
        if 'enviado' in request.GET:
            enviado = True
    context = {
        'in_familia_per':in_familia_per,
        'enviado':enviado, 
    }
    return render(request, "Familias/formulario_insertar_familia.html", context)

def ver_familia(request, id):
    familia_list = Familia.objects.get(id=id)
    context = {
        'fam': familia_list
    }
    return render(request, "Familias/familia.html", context)

def editar_familia(request, id):
    familia_put = Familia.objects.get(id=id)
    in_familia_per = AgregarFamilia(request.POST or None, instance=familia_put)
    if in_familia_per.is_valid():
            in_familia_per.save()       
            return redirect('fam')
    
    context = {
        'in_familia_per':in_familia_per,
    }    
    return render(request, "Familias/formulario_insertar_familia.html", context)

def eliminar_familia(request,id):
    enviado = False
    del_familia = Familia.objects.filter(id=id)
    red = request.POST.get('fam','/erp/fam/')
    if request.method =="POST":
        del_familia.delete()
        return HttpResponseRedirect(red)
    context = {
        'enviado':enviado
    }
    return render(request, "Familias/delete_familia.html", context)