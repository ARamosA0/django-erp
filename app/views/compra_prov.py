from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

from datetime import datetime

def define_context(context={},**kwargs):
    return {**context,**kwargs}
def compra_prov(request):

    context = {

    }

    return render(request, "CompraProv/compraprov_crud.html", context)

def agregar_compra_prov(request):


    context={
        'nueva_factura_form':NuevaFactura({'fecha': datetime.now(),'iva':8}),
        'nombre_factura':'Nueva operación de compra',
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
        
        if not estado_registro and not cancelado:
            prov = Proveedores.objects.filter(ruc=ruc_prov)
            if ruc_prov!='':
                nombre_prov = prov[0] if prov else "RUC INVÁLIDO"
                context = define_context(context,ruc_prov=ruc_prov,
                                        nombre_prov=nombre_prov,nueva_factura_form=nueva_factura)
            
            if prov!=[] and reg_com_clie==ruc_prov:
                nueva_factura.save()
                last_factura = Factura.objects.last()
                fac_prov = Compra_prov()
                fac_prov.codprov = prov[0]
                fac_prov.compra = last_factura
                fac_prov.save()
                compra_prov = Compra_prov.objects.last()
                context = define_context(context,mensaje_registro='succeed',nombre_factura='COMPRA N° '+str(last_factura.pk),
                                                estado_registro=True,iva_factura=last_factura.iva,compra_prov=compra_prov)

        else:
            if cancelado and ruc_prov:
                last = Factura.objects.filter(pk=int(nombre_factura[10:]))
                last[0].delete()
                return redirect("agcompra")
            

            '''
            realizar todas las operaciones siguientes
            los botones estarán desahabilitados hasta que cancele la compra eliminandola con el botón cancelar
            '''
 


    return render(request, "CompraProv/agregar_fac_prov.html", context)