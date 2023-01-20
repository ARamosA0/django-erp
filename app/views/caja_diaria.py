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
        check = request.POST.get('check', None)
        nueva_caja = Caja_diaria()
        if crearcaja:
            if dinero_total.estado:
                montoinicial = request.POST.get("monto_inicial") 
                nueva_caja.monto_total_inicial = montoinicial
                nueva_caja.save()
                ultima_caja = Caja_diaria.objects.last()
                context=define_context(context,
                                    ultima_caja_context=ultima_caja,
                                    estado_busqueda=estado_busqueda)
            dinero_total.estado = True
            
            total_ventas_list = Libro_diario.objects.filter(tipo = 'Venta').filter(obtener_factura__fecha = datetime.now())
            total_compras_list = Libro_diario.objects.filter(tipo = 'Compra').filter(obtener_factura__fecha = datetime.now())
            total_ventas = 0
            total_compras = 0
            for ventas in total_ventas_list:
                total_factura_ventas = ventas.obtener_factura.totalfactura
                total_ventas += total_factura_ventas 

            for compras in total_compras_list:
                total_factura_compras = compras.obtener_factura.totalfactura
                total_compras += total_factura_compras

            print(total_ventas)
            print(total_compras)
            ultima_caja_inicial = Caja_diaria.objects.last()
            total = (ultima_caja_inicial.monto_total_inicial+total_ventas)-total_compras
            dinero_total.monto_total_final = total
            dinero_total.total_ventas = total_ventas
            dinero_total.total_compras = total_compras

            dinero_total.save()
            ultima_caja = Caja_diaria.objects.last()
            context=define_context(context,
                                ultima_caja_context=ultima_caja,
                                estado_busqueda=estado_busqueda)
            
        if check:
            if formbusqueda.is_valid():
                data = Caja_diaria.objects.filter(estado=True)
                data = data.filter(pk=formbusqueda.cleaned_data['fecha'])  if formbusqueda.cleaned_data['fecha'] else data
                context['caja_buscada']=data
                print(data)
                ultima_caja = Caja_diaria.objects.last()
                context=define_context(context,
                                        ultima_caja_context=ultima_caja,
                                        estado_busqueda=True,
                                        formbusqueda=formbusqueda)
            else:
                context['formbusqueda']=formbusqueda

    return render(request, 'CajaDiaria/caja_diaria.html', context)

def ver_caja(request, id):
    caja_detalle = Caja_diaria.objects.get(pk = id)
    context={
        'ultima_caja_context':caja_detalle
    }
    return render(request, 'CajaDiaria/detalle_caja.html', context)