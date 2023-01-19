from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

def libro_diario(request):
    factura_general = Libro_diario.objects.all()
    
    context = {
        'factura_general':factura_general,
    }

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