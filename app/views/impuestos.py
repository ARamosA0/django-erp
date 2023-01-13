from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

def impuestos(request):
    impuestos_list = Impuestos.objects.all()
    busquedaform = ImpuestoBusqueda()

    context = {
        'impuestos_list':impuestos_list,
        'busquedaform':busquedaform
    }

    if request.method == 'POST':
        busquedaform = ImpuestoBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Impuestos.objects.all()
            data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
            data = data.filter(nombre=busquedaform.cleaned_data['nombre'])  if busquedaform.cleaned_data['nombre'] else data
            data = data.filter(nombre=busquedaform.cleaned_data['valor'])  if busquedaform.cleaned_data['valor'] else data
            context['impuestos_list']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = FamiliaBusqueda()

    return render(request, "Impuestos/estructura_crud_imp.html", context) 

def agregar_impuesto(request):
    enviado = False
    if request.method == 'POST':
        in_imp_per = AgregarImpuesto(request.POST)
        if in_imp_per.is_valid():
            in_imp_per.save()
            return HttpResponseRedirect('agregarimpuesto?enviado=True')
    else:
        in_imp_per = AgregarImpuesto()
        if 'enviado' in request.GET:
            enviado = True
    context = {
        'in_imp_per':in_imp_per,
        'enviado':enviado, 
    }
    return render(request, "Impuestos/formulario_insertar_impuesto.html", context)

def editar_impuesto(request, id):
    imp_put = Impuestos.objects.get(id=id)
    in_imp_per = AgregarImpuesto(request.POST or None, instance=imp_put)
    if in_imp_per.is_valid():
            in_imp_per.save()       
            return redirect('imp')
    context = {
        'in_imp_per':in_imp_per,
    }    
    return render(request, "Impuestos/formulario_insertar_impuesto.html", context)

def ver_impuesto(request, id):
    imp_list = Impuestos.objects.get(id=id)
    context = {
        'imp_list': imp_list
    }
    return render(request, "Impuestos/impuesto.html", context)

def eliminar_impuesto(request, id):
    enviado = False
    del_imp = Impuestos.objects.filter(id=id)
    red = request.POST.get('imp','/erp/impuestos/')

    if request.method =="POST":
        del_imp.delete()
        return HttpResponseRedirect(red)
    context = {
        'enviado':enviado
    }
    return render(request, "Impuestos/delete_impuesto.html", context)