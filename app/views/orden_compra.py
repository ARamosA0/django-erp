from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *
from datetime import datetime

def suma_importes(context, id):
    art_fac = Compra_linea_prov.objects.filter(compra_cliente_id = id)
    suma_importes = 0
    for i in art_fac:
        suma_importes += i.importe
    if art_fac:
        factura_last = Factura.objects.get(pk=art_fac[0].compra_cliente.compra.pk)
        total_iva = suma_importes * (factura_last.iva/100)
    else:
        total_iva = 0
    total_fac = suma_importes + total_iva
    context['articulo_factura'] = art_fac
    context['suma_importe'] = suma_importes
    context['total_fac'] = total_fac


def define_context(context={},**kwargs):
    return {**context,**kwargs}

    
def orden_compra(request):

    compra_list = Compra_prov.objects.all()
    busquedaform = OrdenCompraBusqueda()
    context = { 
        'compra_list':compra_list,
        'busquedaform':busquedaform
    }
    if request.method == 'POST':
        busquedaform = OrdenCompraBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Compra_prov.objects.all()
            data = data.filter(codprov__ruc=busquedaform.cleaned_data['rucproveedor'])  if busquedaform.cleaned_data['rucproveedor'] else data
            data = data.filter(factura_id=busquedaform.cleaned_data['numorden'])  if busquedaform.cleaned_data['numorden'] else data
            data = data.filter(factura__fecha=busquedaform.cleaned_data['fechaorden'])  if busquedaform.cleaned_data['fechaorden'] else data
            data = data.filter(estado=busquedaform.cleaned_data['estado'])  if busquedaform.cleaned_data['estado'] else data
            context['compra_list']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = OrdenCompraBusqueda()

    return render(request, "CompraProv/compraprov_crud.html", context)

def agregar_orden_compra(request):

    if 'n_factura' in request.GET:
        fac_id = request.GET.get('n_factura',None)
        if  fac_id:
            compra_prov = Compra_prov.objects.get(pk=fac_id)
            articulo_factura = Compra_linea_prov.objects.filter(compra_cliente_id = compra_prov.pk)

            context=define_context(estado_registro=True,nueva_factura_form=NuevaFactura({'fecha':compra_prov.compra.fecha,'iva':compra_prov.compra.iva}),
                                   nombre_prov=compra_prov.codprov,mensaje_registro='succeed',
                                   ruc_prov=compra_prov.codprov.ruc,compra_prov=str(compra_prov),
                                   articulo_factura=articulo_factura,iva_factura=compra_prov.compra.iva,
                                   nombre_factura='COMPRA N° '+str(compra_prov.compra.pk))
            suma_importes(context,compra_prov.compra.pk)

    else:
        context={
            'nueva_factura_form':NuevaFactura({'fecha': datetime.now(),'iva':18}),
            'nombre_factura':'Nueva orden de compra',
            'iva_factura':8
        }

    if request.method == 'POST':
        nueva_factura = NuevaFactura(request.POST)
        estado_registro = True if request.POST.get("estado_registro",False) == "True" else False
        cancelado = request.POST.get("cancelado", False)
        ruc_prov = request.POST.get('ruc_prov',None)
        reg_com_clie = request.POST.get('reg_com_clie',None)
        nombre_factura = request.POST.get('nombre_factura','')
        iva_factura = request.POST.get('iva_fac',None)
        mensaje_registro = request.POST.get('mensaje_registro','')
        valid_prov_form = request.POST.get("valid_prov_form",None)
        validfac_finalform = request.POST.get("validfac_finalform", None)

        eliminar_art_compra = request.POST.get("eliminar_art_compra",None)
        prov = Proveedores.objects.filter(ruc=ruc_prov)


        if not estado_registro and not cancelado:
            prov = Proveedores.objects.filter(ruc=ruc_prov)
            if ruc_prov!='':
                nombre_prov = prov[0] if prov else "RUC INVÁLIDO"
                context = define_context(context,ruc_prov=ruc_prov,
                                        nombre_prov=nombre_prov,nueva_factura_form=nueva_factura)
            
            if prov and reg_com_clie==ruc_prov:
                print(prov, 'prov1')
                print('estado de registro', estado_registro)
                nueva_factura.save()
                last_factura = Factura.objects.last()
                fac_prov = Compra_prov()
                fac_prov.codprov = prov[0]
                fac_prov.compra = last_factura
                fac_prov.save()
                compra_prov = Compra_prov.objects.last()
                context = define_context(context,
                                        mensaje_registro='succeed',
                                        nombre_factura='COMPRA N° '+str(last_factura.pk),
                                        estado_registro=True,
                                        iva_factura=last_factura.iva,
                                        compra_prov=str(compra_prov))

        else:
            if nombre_factura != 'Nueva orden de compra':
                    factura  = Factura.objects.get(pk=int(nombre_factura[9:]))
                    context['nueva_factura_form']=NuevaFactura({'fecha':factura.fecha,'iva':factura.iva})
            
            if cancelado and ruc_prov:
                if 'n_factura' not in request.GET:
                    last = Factura.objects.filter(pk=factura.pk)
                    last[0].delete()
                    return redirect("agcompra")
                else:
                    return redirect('edorden',id=request.GET['n_factura'])
            

            if eliminar_art_compra:
                del_flc = Compra_linea_prov.objects.filter(pk=request.POST['eliminar_art_compra'])
                del_flc.delete()
                suma_importes(context,Compra_prov.objects.get(pk=factura.pk))
    

            if valid_prov_form:
                nomarticulo = request.POST["nomarticulo"] 
                articulo_data = Articulos.objects.get(nombre=nomarticulo)
                last_factura = Factura.objects.get(pk=factura.pk)

                compra_prov = Compra_prov.objects.get(pk=factura.pk)

                compra_linea_prov = Compra_linea_prov()
                compra_linea_prov.compra_cliente = compra_prov
                compra_linea_prov.codproducto = Articulos.objects.get(nombre=nomarticulo)
                compra_linea_prov.precio = articulo_data.precio_compra
                cantidad = request.POST["cantidad_art"]
                compra_linea_prov.cantidad = cantidad
                compra_linea_prov.importe = (articulo_data.precio_compra * int(cantidad))
                compra_linea_prov.save()    
                suma_importes(context, compra_prov.pk)
                context = define_context(context,
                                        mensaje_registro='succeed',
                                        nombre_factura='COMPRA N° '+str(last_factura.pk),
                                        estado_registro=True,
                                        iva_factura=last_factura.iva,
                                        compra_prov=compra_prov)
                print("======== PROV2")
                print(prov)

            #Modifica Factura
            if validfac_finalform:
                compra_put = factura
                compra_put.totalfactura = request.POST["total_fac"]
                compra_put.save()
                com_clie_last = Compra_prov.objects.get(pk=factura.pk)
                art_com = Compra_linea_prov.objects.filter(compra_cliente_id = com_clie_last.compra.id)
                context['articulo_factura'] = art_com
                context = define_context(context,
                                        mensaje_registro='succeed',
                                        nombre_factura='COMPRA N° '+str(compra_put.pk),
                                        estado_registro=True,
                                        iva_factura=compra_put.iva,
                                        compra_prov=com_clie_last)
                return redirect('edorden',id=com_clie_last.compra.pk)

    return render(request, "CompraProv/agregar_fac_prov.html", context)

def ver_orden(request):
    return 

def editar_orden(request, id):
    orden_compra = Compra_prov.objects.get(compra_id = id)
    art_com = Compra_linea_prov.objects.filter(compra_cliente_id = id)  
    editarCompra = EditarCompra()
    
    editarCompra = EditarCompra(request.POST or None, instance=orden_compra)
    if editarCompra.is_valid():
        editarCompra.save()
        
    context={
        'ord':orden_compra,
        'articulo_factura':art_com,
        'editarform':editarCompra,
    }


    return render(request, "CompraProv/compra_editar.html", context)

def eliminar_orden(request, id):
    enviado = False

    del_orden_liena = Compra_linea_prov.objects.filter(compra_cliente_id=id)
    del_orden_compra = Compra_prov.objects.get(pk=id)
    del_factura = Factura.objects.get(id=id)
    
    red = request.POST.get('compraprov','/erp/compraprov/')

    if request.method =="POST":
        for i in del_orden_liena:
            i.delete()

        del_orden_compra.delete()
        del_factura.delete()
        return HttpResponseRedirect(red)

    context = {
        'enviado':enviado
    }
    return render(request, "CompraProv/del_compra.html", context)
