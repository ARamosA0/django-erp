from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

def remision_proveedores(request):
    albaranes_prov_list = Remision_linea_prov.objects.all()
    busquedaform = RemisionProvBusqueda()
    context ={
        'albaranes_prov_list': albaranes_prov_list,
        'busquedaform': busquedaform
    }

    if request.method == 'POST':
        busquedaform = RemisionProvBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Remision_linea_prov.objects.all()
            data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
            data = data.filter(codremision__factura_proveedor__factura__id=busquedaform.cleaned_data['factura'])  if busquedaform.cleaned_data['factura'] else data
            data = data.filter(codproducto__factura_proveedor__factura__fecha=busquedaform.cleaned_data['fecha'])  if busquedaform.cleaned_data['fecha'] else data
            context['albaranes_prov_list']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = RemisionProvBusqueda()

    return render(request, "AlbaranesProv/estructura_crud_albprov.html",context)

def agregar_remision_proveedores(request):
    enviado = False
    if request.method == 'POST':
        in_albaranes_prov = AgregarRemisionProv(request.POST)
        if in_albaranes_prov.is_valid():
            in_albaranes_prov.save()
            return HttpResponseRedirect('agregarremision?enviado=True')
    else:
        in_albaranes_prov = AgregarRemisionProv()
        if 'enviado' in request.GET:
            enviado = True
    context = {
        'in_albaranes_prov':in_albaranes_prov,
        'enviado':enviado, 
    }
    return render(request, "AlbaranesProv/formulario_insertar_albaranprov.html", context)

def ver_remision_proveedores(request, id):
    albaran_prov_list = Remision_linea_prov.objects.get(codremision__factura_proveedor__factura__id=id)
    art_fac_prov = Factura_linea_prov.objects.filter(id = id)
    context = {
        'art_fac_prov':art_fac_prov,
        'alb_prov': albaran_prov_list
    }
    return render(request, "AlbaranesProv/albaranprov.html", context)

def editar_remision_proveedores(request, id):
    albaranes_put = Remision_linea_prov.objects.get(id=id)
    in_albaranes_prov = AgregarRemisionProv(request.POST or None, instance=albaranes_put)
    if in_albaranes_prov.is_valid():
        in_albaranes_prov.save()       
        return redirect('provrem')
    
    context = {
        'in_albaranes_prov':in_albaranes_prov,
    }    
    return render(request, "AlbaranesProv/formulario_insertar_albaranprov.html", context)

def eliminar_remision_proveedores(request, id):
    enviado = False
    del_albaranes_prov = Remision_linea_prov.objects.filter(id=id)
    red = request.POST.get('provrem','/erp/provremision/')
    if request.method =="POST":
        del_albaranes_prov.delete()
        return HttpResponseRedirect(red)
    context = {
        'enviado':enviado
    }
    return render(request, "AlbaranesProv/delete_albaranprov.html", context)