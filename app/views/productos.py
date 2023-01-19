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
    enviado = False
    if request.method == 'POST':
        prod = Producto()
        prod.nombre=request.POST["nombre_producto"]
        prod.cantidad=request.POST["cantidad_producto"]
        prod.descripcion_producto=request.POST["descripcion_producto"]
        prod.precio_final=request.POST["precio_final_producto"]
        prod.save()
        return HttpResponseRedirect('agregarprod?enviado=True')
    else:
        if 'enviado' in request.GET:
            enviado = True
    context = {
        'enviado':enviado, 
    }
    return render(request, "Productos/formulario_insertar_producto.html", context)

def agregar_articulo_a_producto(request,id):
    articulos_list = Articulos.objects.all()
    enviado = False

    
    if request.method == 'POST':
        #articulo_seleccionado=request.POST.getlist('test[]')
        articulo_seleccionado=request.POST.get('test[]')
        prod_detalle=Producto_detalle()
        prod_detalle.producto=Producto.objects.get(id=id)
        prod_detalle.articulo=Articulos.objects.get(pk=articulo_seleccionado)
        prod_detalle.cantidad=request.POST["cantidad"]
        prod_detalle.save()
        return HttpResponseRedirect('?enviado=True')
    else:
        if 'enviado' in request.GET:
            enviado = True
    context = {
        'articulos_list':articulos_list,
        'enviado':enviado,
    }
    return render(request, "Productos/insertar_articulos.html", context)

def editar_producto(request, id):
    producto_put = Producto.objects.get(id=id)
    in_producto_per = AgregarProducto(request.POST or None, instance=producto_put)
    if in_producto_per.is_valid():
            in_producto_per.save()       
            return redirect('prod')
    context = {
        'in_producto_per':in_producto_per,
    }    
    return render(request, "Productos/formulario_insertar_producto.html", context)
    

def ver_producto(request, id):
    productos_list = Producto.objects.get(id=id)
    context = {
        'prod': productos_list
    }
    return render(request, "Productos/producto.html", context)
    

def eliminar_producto(request, id):
    enviado = False
    del_producto = Producto.objects.filter(id=id)
    red = request.POST.get('prod','/erp/prod/')
    if request.method =="POST":
        del_producto.delete()
        return HttpResponseRedirect(red)
    context = {
        'enviado':enviado
    }
    return render(request, "Productos/delete_producto.html", context)