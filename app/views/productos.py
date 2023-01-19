from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

def productos(request):
    productos_list = Producto.objects.all()
    busquedaform = ProductoBusqueda()

    context = {
        'productos_list':productos_list,
        'busquedaform':busquedaform
    }

    if request.method == 'POST':
        busquedaform = ProductoBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Producto.objects.all()
            data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
            data = data.filter(nombre=busquedaform.cleaned_data['nombre'])  if busquedaform.cleaned_data['nombre'] else data
            context['productos_list']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = ProductoBusqueda()

    return render(request, "Productos/estructura_crud_prod.html", context)

def agregar_producto(request):
    return

def editar_producto(request, id):
    return

def ver_producto(request, id):
    return

def eliminar_producto(request, id):
    return