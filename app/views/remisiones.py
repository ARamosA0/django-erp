from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

def remisiones(request):
    remisiones_list = Remision_clie.objects.all()
    busquedaform = RemisionBusqueda()
    context ={
        'remisiones_list': remisiones_list,
        'busquedaform': busquedaform
    }
    if request.method == 'POST':
        busquedaform = RemisionBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Remision_clie.objects.all()
            data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
            data = data.filter(factura_cliente__factura__id=busquedaform.cleaned_data['factura'])  if busquedaform.cleaned_data['factura'] else data
            data = data.filter(factura_cliente__codcliente__persona__nombre=busquedaform.cleaned_data['cliente'])  if busquedaform.cleaned_data['cliente'] else data
            context['remisiones_list']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = RemisionBusqueda()
    if 'btnestadono' in request.POST:
        remid = request.POST['remid']
        rem_item = Remision_clie.objects.get(id = remid)
        rem_item.estado = Remision_clie.ENVIADO
        rem_item_list = Remision_linea_clie.objects.filter(codremision = rem_item.id)
        for rem in rem_item_list:
            rem_producto = Producto.objects.get(id = rem.codproducto.codproducto.id)
            rem_producto.cantidad = rem_producto.cantidad - rem.codproducto.cantidad
            rem_producto.save()
        rem_item.save() 
    return render(request, "Remisiones/estructura_crud_rem.html",context)

def agregar_remision(request,id):
    enviado = False
    
    if Remision_clie.objects.filter(factura_cliente__factura__id=id).exists():
        productos_list = Factura_linea_clie.objects.filter(factura_cliente__factura__id=id).filter(remision_hecha=False)
    else:
        productos_list = Factura_linea_clie.objects.filter(factura_cliente__factura__id=id)

    if request.method == 'POST':
        rem_clie = Remision_clie()
        rem_clie.factura_cliente=Factura_clie.objects.filter(factura__id=id).last()
        rem_clie.save()
        contador = 0
        lista=request.POST.getlist('productos')
        for producto_seleccionado in lista:
            rem_linea_clie=Remision_linea_clie()
            rem_linea_clie.codremision=Remision_clie.objects.last()
            rem_linea_clie.codproducto=Factura_linea_clie.objects.get(pk=producto_seleccionado)
            
            actualizar=Factura_linea_clie.objects.get(id=producto_seleccionado)
            actualizar.remision_hecha=True
            actualizar.save()

            contador += 1
            rem_linea_clie.save()
        rem_clie2 = Remision_clie.objects.last()
        rem_clie2.contador = contador
        rem_clie2.save()
        return HttpResponseRedirect('?enviado=True')
    else:
        if 'enviado' in request.GET:
            enviado = True
    context = {
        'productos_list':productos_list,
        'enviado':enviado, 
    }
    return render(request, "Remisiones/formulario_insertar_remision.html", context)

def editar_remision(request, id): 
    remisiones_list = Remision_clie.objects.get(id=id)
    articulo_factura = Remision_linea_clie.objects.filter(codremision_id=id)

    context = {
        'rem': remisiones_list,
        'articulo_factura':articulo_factura
    }
    if request.method == 'POST':
        id_rem_art = request.POST['id_rem_art']
        id_ven_art = request.POST['id_ven_art']
        id_ven_art = Factura_linea_clie.objects.get(pk=id_ven_art)
        id_ven_art.remision_hecha = False
        id_ven_art.save()
        del_remision_linea_clie = Remision_linea_clie.objects.get(pk=id_rem_art)
        del_remision_linea_clie.delete()
        context['articulo_factura'] = Remision_linea_clie.objects.filter(codremision_id=id)
    if not context['articulo_factura']:
        remisiones_list.delete()
        return redirect('rem')
    return render(request,"Remisiones/remision_editar.html", context)

def ver_remision(request, id):
    remisiones_list = Remision_clie.objects.get(id=id)
    articulo_factura = Remision_linea_clie.objects.filter(codremision_id=id)

    context = {
        'rem': remisiones_list,
        'articulo_factura':articulo_factura
    }
    return render(request, "Remisiones/remision.html", context)

def eliminar_remision(request, id):
    
    enviado = False

    del_remision_linea_clie = Remision_linea_clie.objects.filter(codremision_id=id)
    del_remision_clie = Remision_clie.objects.get(id=id)
    if request.method =="POST":
        for i in del_remision_linea_clie:
            art_vent_clie = Factura_linea_clie.objects.get(pk=i.codproducto.pk)
            art_vent_clie.remision_hecha = False
            art_vent_clie.save()
        del_remision_clie.delete()

        return redirect('rem')

    context = {
        'enviado':enviado
    }
    return render(request, "Remisiones/delete_remision.html", context)
