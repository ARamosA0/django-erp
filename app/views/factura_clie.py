from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

def factura(request):
    factura_list = Factura_clie.objects.all()
    busquedaform = FacturaBusqueda()
    context ={
        'factura_list': factura_list,
        'busquedaform': busquedaform
    }
    if request.method == 'POST':
        busquedaform = FacturaBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Factura_clie.objects.all()
            data = data.filter(codcliente__persona__dni=busquedaform.cleaned_data['dnicliente'])  if busquedaform.cleaned_data['dnicliente'] else data
            data = data.filter(factura_id=busquedaform.cleaned_data['numfactura'])  if busquedaform.cleaned_data['numfactura'] else data
            data = data.filter(factura__fecha=busquedaform.cleaned_data['fechafac'])  if busquedaform.cleaned_data['fechafac'] else data
            context['factura_list']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = FacturaBusqueda()
    return render(request, "FacturaClie/factura_crud.html",context)

def ver_factura(request, id):
    factura_clie = Factura_clie.objects.get(pk=id)
    articulo_factura = Factura_linea_clie.objects.filter(factura_cliente_id=id)

    context = {
        'fac': factura_clie,
        'articulo_factura':articulo_factura
    }
    return render(request, "FacturaClie/facturaclie.html", context)

def ver_factura_eliminar_articulo(request, id):
    enviado = False

    del_articulo_factura = Factura_linea_clie.objects.get(pk=id)

    red = request.POST.get('facturaclie','/erp/facturaclie/')

    if request.method =="POST":
        del_articulo_factura.delete()
        return HttpResponseRedirect(red)
    
    context = {
        'enviado':enviado
    }

    return render(request, "FacturaClie/delete_factura.html", context)

def editar_factura(request, id):
    factura_clie = Factura_clie.objects.get(pk=id)
    articulo_factura = Factura_linea_clie.objects.filter(factura_cliente_id=id)

    context = {
        'fac': factura_clie,
        'articulo_factura':articulo_factura
    }
    return render(request, "FacturaClie/facturaclie_editar.html", context)

def eliminar_factura(request,id):
    enviado = False

    del_factura_linea_clie = Factura_linea_clie.objects.filter(factura_cliente_id=id)
    del_factura_clie = Factura_clie.objects.get(pk=id)
    del_factura_libro_diario = Libro_diario.objects.get(obtener_factura=id)
    del_factura = Factura.objects.get(id=id)
    
    red = request.POST.get('facturaclie','/erp/facturaclie/')

    if request.method =="POST":
        for i in del_factura_linea_clie:
            i.delete()

        del_factura_clie.delete()
        del_factura_libro_diario.delete()
        del_factura.delete()
        return HttpResponseRedirect(red)

    context = {
        'enviado':enviado
    }
    return render(request, "FacturaClie/delete_factura.html", context)