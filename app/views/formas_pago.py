from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

def formas_de_pago(request):
    formas_de_pago_list = Formapago.objects.all()
    busquedaform = FormasPagoBusqueda()
    
    context = {
        'formas_de_pago_list':formas_de_pago_list,
        'busquedaform':busquedaform
    }

    if request.method == 'POST':
        busquedaform = FormasPagoBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Formapago.objects.all()
            data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
            data = data.filter(nombre=busquedaform.cleaned_data['fpago'])  if busquedaform.cleaned_data['fpago'] else data
            context['formas_de_pago_list']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = FamiliaBusqueda()

    return render(request, "FormasPago/estructura_crud_forpag.html", context)

def agregar_fpago(request):
    enviado = False
    if request.method == 'POST':
        in_fpago_per = AgregarFormaPago(request.POST)
        if in_fpago_per.is_valid():
            in_fpago_per.save()
            return HttpResponseRedirect('agregarformapago?enviado=True')

    else:
        in_fpago_per = AgregarFormaPago()
        if 'enviado' in request.GET:
            enviado = True

    context = {
        'in_fpago_per':in_fpago_per,
        'enviado':enviado, 
    }
    return render(request, "FormasPago/formulario_insertar_formapago.html", context)

def ver_fpago(request, id):
    fpago_list = Formapago.objects.get(id=id)
    context = {
        'fpago_list': fpago_list
    }
    return render(request, "FormasPago/formapago.html", context)

def editar_fpago(request, id):
    fpago_put = Formapago.objects.get(id=id)
    in_fpago_per = AgregarFormaPago(request.POST or None, instance=fpago_put)
    if in_fpago_per.is_valid():
            in_fpago_per.save()       
            return redirect('fpago')
    
    context = {
        'in_fpago_per':in_fpago_per,
    }    
    return render(request, "FormasPago/formulario_insertar_formapago.html", context)

def eliminar_fpago(request, id):
    enviado = False
    del_fpago = Formapago.objects.filter(id=id)
    red = request.POST.get('fpago','/erp/formapago/')

    if request.method =="POST":
        del_fpago.delete()
        return HttpResponseRedirect(red)

    context = {
        'enviado':enviado
    }
    return render(request, "FormasPago/delete_formapago.html", context)
