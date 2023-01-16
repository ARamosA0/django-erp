from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

def factura(request):
    factura_list = Factura_clie.objects.all()
    busquedaform = FacturaBusqueda()
    context ={
        'factura_list': factura_list,
        'busquedaform': busquedaform
    }
    if request.method == 'POST':
        busquedaform = FacturaBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Factura_clie.objects.all()
            data = data.filter(codcliente__persona__dni=busquedaform.cleaned_data['dnicliente'])  if busquedaform.cleaned_data['dnicliente'] else data
            data = data.filter(factura_id=busquedaform.cleaned_data['numfactura'])  if busquedaform.cleaned_data['numfactura'] else data
            data = data.filter(factura__fecha=busquedaform.cleaned_data['fechafac'])  if busquedaform.cleaned_data['fechafac'] else data
            context['factura_list']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = FamiliaBusqueda()
    return render(request, "FacturaClie/factura_crud.html",context)


def ver_factura(request, id):
    factura_clie = Factura_clie.objects.get(factura__id=id)
    art_fac = Factura_linea_clie.objects.filter(factura_cliente_id = id)
    context = {
        'fac': factura_clie,
        'art_fac':art_fac
    }
    return render(request, "FacturaClie/facturaclie.html", context)

def editar_familia(request, id):
    familia_put = Familia.objects.get(id=id)
    in_familia_per = AgregarFamilia(request.POST or None, instance=familia_put)
    if in_familia_per.is_valid():
            in_familia_per.save()       
            return redirect('fam')
    
    context = {
        'in_familia_per':in_familia_per,
    }    
    return render(request, "Familias/formulario_insertar_familia.html", context)

def eliminar_familia(request,id):
    enviado = False
    del_familia = Familia.objects.filter(id=id)
    red = request.POST.get('fam','/erp/fam/')
    if request.method =="POST":
        del_familia.delete()
        return HttpResponseRedirect(red)
    context = {
        'enviado':enviado
    }
    return render(request, "Familias/delete_familia.html", context)