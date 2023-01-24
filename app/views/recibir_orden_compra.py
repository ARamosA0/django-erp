from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

def recibir_orden_compra_servicio(request):
    registro_orden_list = Recibir_orden_servicio.objects.all()

    context = {
        'registro_orden_list':registro_orden_list
    }

    return render(request, "RegistrarOrdenServicio/estructura_crud_registrarorden.html", context)

def agregar_recibir_orden_compra_servicio(request, id):
    #Lista de los servicios correspondiente a la orden. 
    ##Se usa para una muestra grafica de los servicios a agregar
    orden_compra_servicio_list = Servicio_compra.objects.filter(orden_compra=id)

    #De los datos listados, se debe hacer la suma de los precios 
    ##El campo 'costo_total' del modelo Recibir_orden_servicio necesita la suma de todos los precios
    ##para registrar la orden
    precio_total = 0
    for ordenes in orden_compra_servicio_list:
        precio_total += float(ordenes.precio_compra) 

    #Formulario para registrar la orden de compra de servicio
    ##Realiza el mismo proceso de agregado de datos, solo que obtiene los datos directamente del formulario creado.
    enviado = False
    orden_compra_list = Orden_compra_servicio.objects.get(id=id)
    
    if request.method == 'POST':
        registro_orden = Recibir_orden_servicio()
        registro_orden.orden_compra_referencia_id = orden_compra_list.pk 
        registro_orden.fecha_pedido = request.POST.get('datePickerRegister', False) 
        registro_orden.costo_total = request.POST.get('costoTotal', False)
        registro_orden.save()

        return HttpResponseRedirect(f'{orden_compra_list.pk}?enviado=True')
    else:
        if 'enviado' in request.GET:
            enviado = True

    context = {
        'servicios': orden_compra_servicio_list,
        'orden_compra':orden_compra_list,
        'precio_total':precio_total,
        'enviado': enviado
    }

    return render(request, "RegistrarOrdenServicio/formulario_insertar_registrarorden.html", context)

def eliminar_recibir_orden_compra_servicio(request, id):
    enviado = False
    del_registro_orden_compra_servicio = Recibir_orden_servicio.objects.filter(id=id)
    red = request.POST.get('regorden','/erp/regitrarorden/')
    if request.method =="POST":
        del_registro_orden_compra_servicio.delete()
        return HttpResponseRedirect(red)
    context = {
        'enviado':enviado
    }
    return render(request, "RegistrarOrdenServicio/delete_registrarordencompraservicio.html", context)