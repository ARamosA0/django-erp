from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *


def suma_importes(context):
    art_fac = Factura_linea_clie.objects.filter(factura_cliente_id = Factura_clie.objects.last().pk)
    suma_importes = 0
    for i in art_fac:
        suma_importes += i.importe
    factura_last = Factura.objects.last()
    total_iva = suma_importes * (factura_last.iva/100) 
    total_fac = suma_importes + total_iva
    context['articulo_factura'] = art_fac
    context['suma_importe'] = suma_importes
    context['total_fac'] = total_fac


#VENTAS CLIENTES
def reg_venta(request):
    nueva_factura_form = NuevaFactura()
    iva_factura = 8
    context = {
        'nueva_factura_form': nueva_factura_form,
        'iva_factura':iva_factura,
        'suma_importe':0,
        'total_fac':0
    }
    #Buequeda de persona
    if 'dni_cliente' in request.GET:
        cod = request.GET['dni_cliente']
        if  cod != '':
            cliente = Clientes.objects.filter(persona_id__dni=cod)
            context['dni_cliente'] = cod
            context['nombre_cliente'] = cliente[0] if cliente else "cliente inexistente"
    #Registro en tabla factura clie
    if 'registro_cli_fac' in request.GET:
        fac_clie = Factura_clie()
        fac_clie.factura = Factura.objects.last()
        fac_clie.codcliente = Clientes.objects.filter(persona_id__dni=cod)[0]
        fac_clie.save()
    #eliminacion factura linea cliente
    if 'factura_cliente_id' in request.GET:
        del_flc = Factura_linea_clie.objects.filter(pk=request.GET['factura_cliente_id'])
        print('==========================',del_flc)
        if del_flc != []:
            del_flc.delete()
            suma_importes(context)
        # context['articulo_factura'] = Factura_linea_clie.objects.filter(factura_cliente_id = Factura_clie.objects.last().pk)
        

    if request.method == 'POST':
        nueva_factura = NuevaFactura(request.POST)
        validfac_cliente_list_form = request.POST.get("validfac_cliente_list_form", None)
        validfac_finalform = request.POST.get("validfac_finalform", None)

        # Crea Factura
        if nueva_factura.is_valid():
            nueva_factura.save()
            print('CREO FACTURA')
            context['nueva_factura_form'] = nueva_factura
            context['iva_factura'] = nueva_factura.cleaned_data['iva']
            return render(request, "VentaClientes/registroventa.html", context)
        
        # fac_cliente_list_form
        if validfac_cliente_list_form:
            nomarticulo = request.POST["nomarticulo"] 
            articulo_data = Articulos.objects.get(referencia=nomarticulo)
            fac_clie_last = Factura_clie.objects.last()
            fac_clie_last_id = fac_clie_last.factura.id
            factura_linea_clie = Factura_linea_clie()
            factura_linea_clie.factura_cliente = Factura_clie.objects.last()
            factura_linea_clie.codproducto = Articulos.objects.get(referencia=nomarticulo)
            factura_linea_clie.precio = articulo_data.precio_compra
            cantidad = request.POST["cantidad_art"]
            factura_linea_clie.cantidad = cantidad
            descuento = request.POST["descuento_art"]
            factura_linea_clie.dsctoproducto = descuento
            factura_linea_clie.importe = (articulo_data.precio_compra * int(cantidad)) - float(descuento)
            factura_linea_clie.save()    
            suma_importes(context)

        #Modifica Factura
        if validfac_finalform:
            factura_put = Factura.objects.last()
            factura_put.totalfactura = request.POST["total_fac"]
            factura_put.save()
            fac_clie_last = Factura_clie.objects.last()
            fac_clie_last_id = fac_clie_last.factura.id
            art_fac = Factura_linea_clie.objects.filter(factura_cliente_id = fac_clie_last_id)
            context['articulo_factura'] = art_fac
        
    return render(request, "VentaClientes/registroventa.html", context)
