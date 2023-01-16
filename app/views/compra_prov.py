from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

def define_context(context={},**kwargs):
    return {**context,**kwargs}
def compra_prov(request):

    context = {

    }

    return render(request, "CompraProv/compraprov_crud.html", context)

def agregar_compra_prov(request):


    context={'nueva_factura_form':NuevaFactura()}

    if request.method == 'POST':
        nueva_factura = NuevaFactura(request.POST)
        ruc_prov = request.POST.get('ruc_prov',None)
        prov = Proveedores.objects.filter(ruc=ruc_prov)
        if ruc_prov!='' and nueva_factura.is_valid():
            nombre_prov = prov[0] if prov else "RUC INVÁLIDO"
            context = define_context(context,ruc_prov=ruc_prov,
                                    nombre_prov=nombre_prov,nueva_factura_form=nueva_factura)



    if request == 'POST':
        valid_prov_form = request.POST.get("valid_prov_form",None)
        validfac_finalform = request.POST.get("validfac_finalform", None)


        # if eliminar_art_venta:
        #     del_flc = Factura_linea_clie.objects.filter(pk=request.POST['eliminar_art_venta'])
        #     del_flc.delete()
        #     suma_importes(context)
 
        
        if valid_prov_form:
            nomarticulo = request.POST["nomarticulo"] 
            articulo_data = Articulos.objects.get(referencia=nomarticulo)
            compra_prov_last = Compra_prov.objects.last()
            compra_prov_last_id = compra_prov_last.factura.id
            compra_linea_prov = Compra_linea_prov()
            compra_linea_prov.factura_cliente = Factura_clie.objects.last()
            compra_linea_prov.codproducto = Articulos.objects.get(referencia=nomarticulo)
            compra_linea_prov.precio = articulo_data.precio_compra
            cantidad = request.POST["cantidad_art"]
            compra_linea_prov.cantidad = cantidad
            descuento = request.POST["descuento_art"]
            compra_linea_prov.dsctoproducto = descuento
            compra_linea_prov.importe = (articulo_data.precio_compra * int(cantidad)) - float(descuento)
            compra_linea_prov.save()    
            # suma_importes(context)

        #Modifica Factura
        if validfac_finalform:
            factura_put = Factura.objects.last()
            factura_put.totalfactura = request.POST["total_fac"]
            factura_put.save()
            fac_clie_last = Factura_clie.objects.last()
            fac_clie_last_id = fac_clie_last.factura.id
            art_fac = Factura_linea_clie.objects.filter(factura_cliente_id = fac_clie_last_id)
            context['articulo_factura'] = art_fac

    return render(request, "CompraProv/agregar_fac_prov.html", context)