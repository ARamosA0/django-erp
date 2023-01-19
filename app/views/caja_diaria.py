from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *
from datetime import datetime

def define_context(context={},**kwargs):
    return {**context,**kwargs}

def caja_diaria(request):
    formbusqueda = DateFormSearch({'fechabusqueda':datetime.now()})
    tipo_pago = Formapago.objects.all()
    dinero_total = Caja_diaria.objects.last()
    estado_busqueda = False
    context = {
        'formbusqueda':formbusqueda,
        'tipo_pago':tipo_pago,
        'ultima_caja_context':dinero_total,
    }
    
    if(dinero_total == None):
        caja_diaria = Caja_diaria()
        caja_diaria.estado = True
        caja_diaria.save()
        dinero_total = Caja_diaria.objects.last()
        
    

    if request.method == 'POST':
        crearcaja = request.POST.get('crearcaja',None)
        nueva_caja = Caja_diaria()
        if crearcaja:
            if dinero_total.estado:
                montoinicial = request.POST.get("monto_inicial") 
                nueva_caja.monto_total_inicial = montoinicial
                nueva_caja.neto = dinero_total.monto_total_final
                nueva_caja.save()
                ultima_caja = Caja_diaria.objects.last()
                context=define_context(context,
                                    ultima_caja_context=ultima_caja,
                                    estado_busqueda=estado_busqueda)
            dinero_total.estado = True
            dinero_total.save()
            # total_ventas = Factura_clie.objects.
            ultima_caja = Caja_diaria.objects.last()
            context=define_context(context,
                                ultima_caja_context=ultima_caja,
                                estado_busqueda=estado_busqueda)
            
        if formbusqueda.is_valid():
            data = Caja_diaria.objects.filter(estado=True)
            data = data.filter(pk=formbusqueda.cleaned_data['fecha'])  if formbusqueda.cleaned_data['fecha'] else data
            context['caja_buscada']=data
            ultima_caja = Caja_diaria.objects.last()
            context=define_context(context,
                                    ultima_caja_context=ultima_caja,
                                    estado_busqueda=True,
                                    formbusqueda=formbusqueda)
        else:
            context['formbusqueda']=formbusqueda

    return render(request, 'CajaDiaria/caja_diaria.html', context)