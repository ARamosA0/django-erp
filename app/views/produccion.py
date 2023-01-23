from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *


def produccion(request):

    busquedaform = ProduccioBusqueda()
    produccion_list = Produccion.objects.all()

    context = {
        'busquedaform':busquedaform,
        'produccion_list':produccion_list
    }
    return render(request, 'Produccion/produccion_crud.html', context)

def agr_produccion(request):

    factura_list = Factura_clie.objects.filter(estadoprod = False)
    red = request.POST.get('prod','/erp/produccion/')

    if request.method == 'POST':
        fecha_inicio = request.POST['fechainicio']
        fecha_fin = request.POST['fechafin']
        factura_id = request.POST['facturaid']

        produccion = Produccion()
        prod_datos = Produccion_linea()
        facturasave = Factura_clie.objects.get(pk = factura_id)
        
        produccion.factura_clie = facturasave
        produccion.fecha_inicio = fecha_inicio
        produccion.fecha_fin = fecha_fin
        produccion.save()
        
        facturasave.estadoprod = True
        facturasave.save()

        last_prod = Produccion.objects.last()
        fac_linea_clie = Factura_linea_clie.objects.filter(factura_cliente_id = facturasave.factura.id)
        for i in fac_linea_clie:
            prod_datos.produccion = last_prod
            prod_datos.cod_producto = i.codproducto
            prod_datos.save()

        return HttpResponseRedirect(red)

    context={
        'factura_list':factura_list,
        'contador':0
    }

    return render(request, 'Produccion/agregar_produccion.html', context)

def ver_produccion (request, id):
    context = {}
    return render(request, 'Produccion/produccion.html', context)

def del_produccion(request, id):
    enviado = False
    del_produ = Produccion.objects.get(pk = id)
    fac = Factura_clie.objects.get(pk = del_produ.factura_clie.factura.id)
    print(fac.estadoprod)
    red = request.POST.get('prod','/erp/produccion/')
    if request.method =="POST":
        del_produ.delete()
        fac.estadoprod= False
        fac.save()
        return HttpResponseRedirect(red)
    context={
        'enviado':enviado
    }

    return render(request, 'Produccion/del_produccion.html', context)