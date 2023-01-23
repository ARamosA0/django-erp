from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

def remision_proveedores(request):
    remisiones_list = Remision_prov.objects.all()
    busquedaform = RemisionProvBusqueda()
    context ={
        'remisiones_list': remisiones_list,
        'busquedaform': busquedaform
    }
    if request.method == 'POST':
        busquedaform = RemisionProvBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Remision_prov.objects.all()
            data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
            data = data.filter(factura_proveedor__compra__id=busquedaform.cleaned_data['factura'])  if busquedaform.cleaned_data['factura'] else data
            data = data.filter(factura_proveedor__codprov__empresa__nombre=busquedaform.cleaned_data['proveedor'])|data.filter(factura_proveedor__codprov__persona__nombre=busquedaform.cleaned_data['proveedor'])  if busquedaform.cleaned_data['proveedor'] else data
            context['remisiones_list']=data
            context['busquedaform']=busquedaform
    return render(request, "RemisionesProv/estructura_crud_remprov.html",context)

def agregar_remision_proveedores(request,id):
    enviado = False
    
    if Remision_prov.objects.filter(factura_proveedor__compra__id=id).exists():
        productos_list = Compra_linea_prov.objects.filter(compra_cliente__compra__id=id).filter(remision_hecha=False)
    else:
        productos_list = Compra_linea_prov.objects.filter(compra_cliente__compra__id=id)

    if request.method == 'POST':
        rem_clie = Remision_prov()
        rem_clie.factura_proveedor=Compra_prov.objects.filter(compra__id=id).last()
        rem_clie.save()
        
        lista=request.POST.getlist('productos')
        for producto_seleccionado in lista:
            rem_linea_clie=Remision_linea_prov()
            rem_linea_clie.codremision=Remision_prov.objects.last()
            rem_linea_clie.codproducto=Compra_linea_prov.objects.get(pk=producto_seleccionado)
            
            actualizar=Compra_linea_prov.objects.get(id=producto_seleccionado)
            actualizar.remision_hecha=True
            actualizar.save()

            rem_linea_clie.save()
        return HttpResponseRedirect('?enviado=True')
    else:
        if 'enviado' in request.GET:
            enviado = True
    context = {
        'productos_list':productos_list,
        'enviado':enviado, 
    }
    return render(request, "RemisionesProv/formulario_insertar_remisionprov.html", context)
def ver_remision_proveedores(request, id):
    remisiones_list = Remision_prov.objects.get(id=id)
    articulo_factura = Remision_linea_prov.objects.filter(codremision_id=id)

    context = {
        'rem': remisiones_list,
        'articulo_factura':articulo_factura
    }
    return render(request, "RemisionesProv/remisionprov.html", context)

def editar_remision_proveedores(request, id):
    remisiones_list = Remision_prov.objects.get(id=id)
    articulo_factura = Remision_linea_prov.objects.filter(codremision_id=id)
    context = {
        'rem': remisiones_list,
        'articulo_factura':articulo_factura
    }
    if request.method == 'POST':
        id_rem_art = request.POST['id_rem_art']
        id_com_art = request.POST['id_com_art']
        id_com_art = Compra_linea_prov.objects.get(pk=id_com_art)
        id_com_art.remision_hecha = False
        id_com_art.save()
        del_remision_linea_prov = Remision_linea_prov.objects.get(pk=id_rem_art)
        del_remision_linea_prov.delete()
        context['articulo_factura']=Remision_linea_prov.objects.filter(codremision_id=id)
    if not context['articulo_factura']:
        remisiones_list.delete()
        return redirect('provrem')
    return render(request, 'RemisionesProv/remisionprov_editar.html',context)








    return render(request, "Remisiones/remision_editar.html", context)

def eliminar_remision_proveedores(request, id):
    enviado = False

    del_remision_linea_prov = Remision_linea_prov.objects.filter(codremision_id=id)
    del_remision_prov = Remision_prov.objects.get(id=id)
    if request.method =="POST":
        for i in del_remision_linea_prov:
            art_com_prov = Compra_linea_prov.objects.get(pk=i.codproducto.pk)
            art_com_prov.remision_hecha = False
            art_com_prov.save()
        del_remision_prov.delete()
        return redirect('provrem')

    context = {
        'enviado':enviado
    }
    return render(request, "RemisionesProv/delete_remisionprov.html", context)