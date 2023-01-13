from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

def albaranes(request):
    albaranes_list = Albaran_linea_clie.objects.all()
    busquedaform = AlbaranBusqueda()
    context ={
        'albaranes_list': albaranes_list,
        'busquedaform': busquedaform
    }
    if request.method == 'POST':
        busquedaform = AlbaranBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Albaran_linea_clie.objects.all()
            data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
            data = data.filter(cliente=busquedaform.cleaned_data['cliente'])  if busquedaform.cleaned_data['cliente'] else data
            data = data.filter(descripcionproducto=busquedaform.cleaned_data['descripcionproducto'])  if busquedaform.cleaned_data['descripcionproducto'] else data
            context['albaranes_list']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = AlbaranBusqueda()
    return render(request, "Albaranes/estructura_crud_alb.html",context)

def agregar_albaran(request):
    enviado = False
    if request.method == 'POST':
        in_albaranes_per = AgregarAlbaran(request.POST)
        if in_albaranes_per.is_valid():
            in_albaranes_per.save()
            return HttpResponseRedirect('agregaralb?enviado=True')
    else:
        in_albaranes_per= AgregarAlbaran()
        if 'enviado' in request.GET:
            enviado = True
    context = {
        'in_albaranes_per':in_albaranes_per,
        'enviado':enviado, 
    }
    return render(request, "Albaranes/formulario_insertar_albaran.html", context)

def editar_albaran(request, id): 
    albaranes_put = Albaran_linea_clie.objects.get(id=id)
    in_albaranes_per = AgregarAlbaran(request.POST or None, instance=albaranes_put)
    if in_albaranes_per.is_valid():
            in_albaranes_per.save()       
            return redirect('alb')
    
    context = {
        'in_albaranes_per':in_albaranes_per,
    }    
    return render(request, "Albaranes/formulario_insertar_albaran.html", context)
<<<<<<< HEAD

=======
>>>>>>> 83d7b8e7ad8ebe7af0322045b4f9d9fa9f8cffa3

def ver_albaran(request, id):
    albaran_list = Albaran_linea_clie.objects.get(id=id)
    context = {
        'alb': albaran_list
    }
    return render(request, "Albaranes/albaran.html", context)

def eliminar_albaran(request, id):
    enviado = False
    del_albaranes = Albaran_linea_clie.objects.filter(id=id)
    red = request.POST.get('alb','/erp/alb/')
    if request.method =="POST":
        del_albaranes.delete()
        return HttpResponseRedirect(red)
    context = {
        'enviado':enviado
    }
    return render(request, "Albaranes/delete_albaran.html", context)

# FACTURA ALBANARES
def fac_albanar(request):
    return 