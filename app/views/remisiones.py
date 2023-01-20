from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

def remisiones(request):
    remisiones_list = Remision_clie.objects.all()
    busquedaform = RemisionBusqueda()
    context ={
        'remisiones_list': remisiones_list,
        'busquedaform': busquedaform
    }
    if request.method == 'POST':
        busquedaform = RemisionBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Remision_clie.objects.all()
            data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
            data = data.filter(factura_cliente__factura__id=busquedaform.cleaned_data['factura'])  if busquedaform.cleaned_data['factura'] else data
            data = data.filter(factura_cliente__codcliente__persona__nombre=busquedaform.cleaned_data['cliente'])  if busquedaform.cleaned_data['cliente'] else data
            context['remisiones_list']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = RemisionBusqueda()
    return render(request, "Remisiones/estructura_crud_rem.html",context)

def agregar_remision(request,id):
    enviado = False
    
    if Remision_clie.objects.filter(factura_cliente__factura__id=id).exists():
        productos_list = Factura_linea_clie.objects.filter(factura_cliente__factura__id=id).filter(remision_hecha=False)
    else:
        productos_list = Factura_linea_clie.objects.filter(factura_cliente__factura__id=id)

    if request.method == 'POST':
        rem_clie = Remision_clie()
        rem_clie.factura_cliente=Factura_clie.objects.filter(factura__id=id).last()
        rem_clie.save()
        contador = 0
        lista=request.POST.getlist('productos')
        for producto_seleccionado in lista:
            rem_linea_clie=Remision_linea_clie()
            rem_linea_clie.codremision=Remision_clie.objects.last()
            rem_linea_clie.codproducto=Factura_linea_clie.objects.get(pk=producto_seleccionado)
            
            actualizar=Factura_linea_clie.objects.get(id=producto_seleccionado)
            actualizar.remision_hecha=True
            actualizar.save()

            contador += 1
            rem_linea_clie.save()
        rem_clie2 = Remision_clie.objects.last()
        rem_clie2.contador = contador
        rem_clie2.save()
        return HttpResponseRedirect('?enviado=True')
    else:
        if 'enviado' in request.GET:
            enviado = True
    context = {
        'productos_list':productos_list,
        'enviado':enviado, 
    }
    return render(request, "Remisiones/formulario_insertar_remision.html", context)

def editar_remision(request, id): 
    remisiones_list = Remision_clie.objects.get(id=id)
    articulo_factura = Remision_linea_clie.objects.filter(codremision_id=id)

    context = {
        'rem': remisiones_list,
        'articulo_factura':articulo_factura
    }
    return render(request, "Remisiones/remision_editar.html", context)

def ver_remision(request, id):
    remisiones_list = Remision_clie.objects.get(id=id)
    articulo_factura = Remision_linea_clie.objects.filter(codremision_id=id)

    context = {
        'rem': remisiones_list,
        'articulo_factura':articulo_factura
    }
    return render(request, "Remisiones/remision.html", context)

def eliminar_remision(request, id):
    enviado = False

    del_remision_linea_clie = Remision_linea_clie.objects.filter(codremision_id=id)
    del_remision_clie = Remision_clie.objects.get(id=id)
    
    red = request.POST.get('rem','/erp/rem/')

    if request.method =="POST":
        for i in del_remision_linea_clie:
            i.delete()

        del_remision_clie.delete()
        return HttpResponseRedirect(red)

    context = {
        'enviado':enviado
    }
    return render(request, "Remisiones/delete_remision.html", context)

def eliminar_articulo_remision(request, id):
    enviado = False

    del_remision_linea_clie = Remision_linea_clie.objects.get(id=id)
    
    red = request.POST.get('rem','/erp/rem/')

    if request.method =="POST":
        del_remision_linea_clie.delete()
        return HttpResponseRedirect(red)

    context = {
        'enviado':enviado
    }
    return render(request, "Remisiones/delete_remision.html", context)