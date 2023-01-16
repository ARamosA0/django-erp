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



    return render(request, "CompraProv/agregar_fac_prov.html", context)