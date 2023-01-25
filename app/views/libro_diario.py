from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

def libro_diario(request):
    factura_general = Libro_diario.objects.all().order_by('-obtener_factura__fecha')
    busquedaform = LibroDiarioBusqueda()
    
    context = {
        'factura_general':factura_general,
        'contador':len(factura_general),
        'busquedaform': busquedaform
    }

    if request.method == 'POST':
        busquedaform = LibroDiarioBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Libro_diario.objects.all()
            data = data.filter(obtener_factura__fecha=busquedaform.cleaned_data['fecha'])  if busquedaform.cleaned_data['fecha'] else data
            data = data.filter(tipo=busquedaform.cleaned_data['tipo'])  if busquedaform.cleaned_data['tipo'] else data
            context['factura_general']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = LibroDiarioBusqueda()

    return render(request, 'LibroDiario/estructura_librodiario.html', context)

def ver_libro_diario(request, id):
    dato_libro_diario = Libro_diario.objects.get(id=id)

    tipo = dato_libro_diario.obtener_factura_id

    cliente = Factura_clie.objects.all()
    proveedor = Compra_prov.objects.all()


    if dato_libro_diario.tipo == "Compra":
        #Obtener datos necesarios de Compra
        obtener_dato_proveedor = Compra_prov.objects.get(compra_id=tipo)
        proveedor = obtener_dato_proveedor
        
    elif dato_libro_diario.tipo == "Venta":
        #Obtener datos necesarios de Venta
        obtener_dato_cliente = Factura_clie.objects.get(factura_id=tipo)
        cliente = obtener_dato_cliente
    
    context = {
        'librodiario':dato_libro_diario,
        'cliente':cliente,
        'proveedor':proveedor
    }

    return render(request, 'LibroDiario/librodiario.html', context)