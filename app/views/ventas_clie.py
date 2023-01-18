from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

from datetime import datetime

def define_context(context={},**kwargs):
    return {**context,**kwargs}

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
    
    context={
        'nueva_factura_form':NuevaFactura({'fecha': datetime.now(),'iva':8}),
        'nombre_factura':'NUEVA VENTA',
        'iva_factura':8
    }

    if request.method == 'POST':
        estado_registro = True if request.POST.get("estado_registro",False) == "True" else False
        cancelado = request.POST.get("cancelado", False)
        dni_cliente = request.POST.get('dni_cliente','')
        nombre_cliente = request.POST.get('nombre_cliente','')
        reg_fac_clie = request.POST.get('reg_fac_clie',None)
        nombre_factura = request.POST.get('nombre_factura','')
        iva_factura = request.POST.get('iva_fac',None)
        mensaje_registro = request.POST.get('mensaje_registro','')
        factura_clie = request.POST.get('factura_clie','')

        context = define_context(context,dni_cliente=dni_cliente,estado_registro=estado_registro,nombre_factura=nombre_factura,
                                         nombre_cliente=nombre_cliente,factura_clie=factura_clie,
                                         iva_factura=iva_factura,mensaje_registro=mensaje_registro)

        if not estado_registro and not cancelado:
            nueva_factura = NuevaFactura(request.POST)
            context['nueva_factura_form'] = nueva_factura
            clie = Clientes.objects.filter(persona_id__dni=dni_cliente)
            if dni_cliente!='':
                nombre_cliente = clie[0] if clie else "DNI INVÁLIDO"
                context = define_context(context,dni_cliente=dni_cliente,
                                    nombre_cliente=nombre_cliente)
            if clie and reg_fac_clie==dni_cliente:
                nueva_factura.save()
                last_factura = Factura.objects.last()
                fac_clie = Factura_clie()
                fac_clie.codcliente = clie[0]
                fac_clie.factura = last_factura
                fac_clie.save()
                factura_clie = Factura_clie.objects.last()
                context = define_context(context,mensaje_registro='succeed',nombre_factura='VENTA N° '+str(last_factura.pk),
                                                estado_registro=True,iva_factura=last_factura.iva,factura_clie=str(factura_clie))

        else:
            validfac_cliente_list_form = request.POST.get("validfac_cliente_list_form", None)
            validfac_finalform = request.POST.get("validfac_finalform", None)
            eliminar_art_venta = request.POST.get("eliminar_art_venta",None)
            
            if nombre_factura != 'NUEVA VENTA' != "VENTA REALIZADA":
                factura = Factura.objects.last()
                fecha = factura.fecha
                iva = factura.iva
                context['nueva_factura_form'] = NuevaFactura({'fecha': fecha,'iva':iva})

            if cancelado and dni_cliente:
                last = Factura.objects.filter(pk=int(nombre_factura[9:]))
                last[0].delete()
                return redirect("venta")
            
            if validfac_cliente_list_form:
                    nomarticulo = request.POST["nomarticulo"]
                    cantidad = request.POST["cantidad_art"]
                    descuento = request.POST["descuento_art"]
                    articulo_data = Articulos.objects.get(referencia=nomarticulo)
                    factura_linea_clie = Factura_linea_clie()
                    factura_linea_clie.factura_cliente = Factura_clie.objects.last()
                    factura_linea_clie.codproducto = articulo_data
                    factura_linea_clie.precio = articulo_data.precio_compra
                    factura_linea_clie.cantidad = cantidad
                    factura_linea_clie.dsctoproducto = descuento
                    factura_linea_clie.importe = (articulo_data.precio_compra * int(cantidad)) - float(descuento)
                    factura_linea_clie.save()    
                    suma_importes(context)
            if eliminar_art_venta:
                del_flc = Factura_linea_clie.objects.filter(pk=eliminar_art_venta)
                del_flc.delete()
                suma_importes(context)
            if validfac_finalform:
                factura  = Factura.objects.filter(pk=int(nombre_factura[9:]))[0]
                factura.totalfactura = request.POST["total_fac"]
                factura.save()
                context={
                    'nueva_factura_form':NuevaFactura({'fecha': datetime.now(),'iva':8}),
                    'nombre_factura':'VENTA REALIZADA',
                    'iva_factura':8
                }
    return render(request, "VentaClientes/registroventa.html", context)