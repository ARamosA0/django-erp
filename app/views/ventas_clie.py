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
        'total_fac':0,
        'mensaje_registro':''
    }

    if request.method == 'POST':
        nueva_factura = NuevaFactura(request.POST)
        validfac_cliente_list_form = request.POST.get("validfac_cliente_list_form", None)
        validfac_finalform = request.POST.get("validfac_finalform", None)

        cod = request.POST.get("dni_cliente",None)
        reg_fac_clie = request.POST.get("reg_fac_clie",None)
        eliminar_art_venta = request.POST.get("eliminar_art_venta",None)


        # Crea Factura
        if nueva_factura.is_valid():
            nueva_factura.save()
            context['nueva_factura_form'] = nueva_factura
            context['iva_factura'] = nueva_factura.cleaned_data['iva']
            return render(request, "VentaClientes/registroventa.html", context)

        if cod and cod!='' and reg_fac_clie!=cod:
            cliente = Clientes.objects.filter(persona_id__dni=cod)  
            context['dni_cliente'] = cod
            context['nombre_cliente'] = cliente[0] if cliente else "cliente inexistente"

        if reg_fac_clie and reg_fac_clie==cod:
            fac_clie = Factura_clie()
            cliente = Clientes.objects.filter(persona_id__dni=reg_fac_clie)[0]
            #last_factura = Factura.objects.last().pk
            #last_fac_clie =Factura_clie.objects.last().pk
            #if last_factura != last_fac_clie:
            #    context['mensaje_registro'] = 'succeed'
            #else:
            #    context['mensaje_registro'] = 'failed'
            fac_clie.codcliente = cliente
            fac_clie.factura = Factura.objects.last()
            fac_clie.save()
            context['dni_cliente'] = reg_fac_clie
            context['nombre_cliente'] = cliente

        if eliminar_art_venta:
            del_flc = Factura_linea_clie.objects.filter(pk=request.POST['eliminar_art_venta'])
            del_flc.delete()
            suma_importes(context)
 
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
