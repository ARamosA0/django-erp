from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *


def produccion(request):

    busquedaform = ProduccioBusqueda()
    produccion_list = Produccion.objects.all()
    if 'btnestadoinicio' in request.POST:
        prodid = request.POST['prodid']
        prod_item = Produccion.objects.get(id = prodid)
        prod_item.estdo_produccion = Produccion_linea.PROCESO
        prod_item.save() 
    elif 'btnestadoproceso' in request.POST:
        prodid = request.POST['prodid']
        prod_item = Produccion.objects.get(id = prodid)
        prod_item.estdo_produccion = Produccion_linea.TERMINADO
        prod_item.save() 
    elif 'btnestadoterminado' in request.POST:
        prodid = request.POST['prodid']
        prod_item = Produccion.objects.get(id = prodid)
        prod_item.estdo_produccion = Produccion_linea.SALIENDO
        prod_item.save() 
    elif 'btnestadosaliendo' in request.POST:
        prodid = request.POST['prodid']
        prod_item = Produccion.objects.get(id = prodid)
        prod_item.estdo_produccion = Produccion_linea.NINGUNO
        prod_item.save() 
    context = {
        'busquedaform':busquedaform,
        'contador':len(produccion_list),
        'produccion_list':produccion_list
    }
    if 'busquedaproduccion' in request.POST:
        busquedaform = ProduccioBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Produccion.objects.all()
            print(data.filter(fecha_fin=busquedaform.cleaned_data['fecha_fin']))
            data = data.filter(fecha_inicio=busquedaform.cleaned_data['fecha_inicio'])  if busquedaform.cleaned_data['fecha_inicio'] else data
            data = data.filter(fecha_fin=busquedaform.cleaned_data['fecha_fin'])  if busquedaform.cleaned_data['fecha_fin'] else data
            data = data.filter(estdo_produccion=busquedaform.cleaned_data['estado'])  if busquedaform.cleaned_data['estado'] else data
            context['produccion_list']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = ProduccioBusqueda()
    return render(request, 'Produccion/produccion_crud.html', context)

def agr_produccion(request):

    factura_list = Factura_clie.objects.filter(estadoprod = False)
    red = request.POST.get('prod','/erp/produccion/')

    if request.method == 'POST':
        fecha_inicio = request.POST['fechainicio']
        fecha_fin = request.POST['fechafin']
        factura_id = request.POST['facturaid']

        produccion = Produccion()
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
            prod_datos = Produccion_linea()
            prod_datos.produccion = last_prod
            prod_datos.cod_producto = i
            prod_datos.save()

        return HttpResponseRedirect(red)
    
    context={
        'factura_list':factura_list,
        'contador':0
    }

    return render(request, 'Produccion/agregar_produccion.html', context)

def ver_produccion (request, id):
    prod_linea_list = Produccion_linea.objects.filter(produccion_id = id)
    red = request.POST.get('prod','/erp/produccion/ver/'+str(id)+'/')
    if 'btnestadoinicio' in request.POST:
        prodid = request.POST['prodid']
        prod_item = Produccion_linea.objects.get(id = prodid)
        prod_item.estdo_produccion_prod = Produccion_linea.PROCESO
        producto_selec = Producto.objects.get(pk = prod_item.cod_producto.codproducto.id)
        producto_selec_detalle = Producto_detalle.objects.filter(producto = producto_selec)
        for prod_det in producto_selec_detalle:
            articulo_prod = Articulos.objects.get(pk = prod_det.articulo.id)
            articulo_prod.stock = articulo_prod.stock - prod_det.cantidad
            articulo_prod.save()
        producto_selec.cantidad = producto_selec.cantidad + prod_item.cod_producto.cantidad
        producto_selec.save()
        prod_item.save() 
    elif 'btnestadoproceso' in request.POST:
        prodid = request.POST['prodid']
        prod_item = Produccion_linea.objects.get(id = prodid)
        prod_item.estdo_produccion_prod = Produccion_linea.TERMINADO
        prod_item.save() 
    elif 'btnestadoterminado' in request.POST:
        prodid = request.POST['prodid']
        prod_item = Produccion_linea.objects.get(id = prodid)
        prod_item.estdo_produccion_prod = Produccion_linea.SALIENDO
        prod_item.save() 
    elif 'btnestadosaliendo' in request.POST:
        prodid = request.POST['prodid']
        prod_item = Produccion_linea.objects.get(id = prodid)
        prod_item.estdo_produccion_prod = Produccion_linea.NINGUNO
        prod_item.save() 
    context = {
        'prod_linea_list':prod_linea_list,
    }
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