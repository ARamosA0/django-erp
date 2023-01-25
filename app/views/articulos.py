from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *


def articulos(request):
    articulos_list = Articulos.objects.all()
    busquedaform = ArticuloBusqueda()
    context ={
        'articulos_list': articulos_list,
        'contador':len(articulos_list),
        'busquedaform': busquedaform
    }

    if request.method == 'POST':
        busquedaform = ArticuloBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Articulos.objects.all()
            data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
            data = data.filter(nombre=busquedaform.cleaned_data['nombre'])  if busquedaform.cleaned_data['nombre'] else data
            data = data.filter(familia=busquedaform.cleaned_data['familia'])  if busquedaform.cleaned_data['familia'] else data
            data = data.filter(descripcion=busquedaform.cleaned_data['descripcion'])  if busquedaform.cleaned_data['descripcion'] else data
            data = data.filter(tipo=busquedaform.cleaned_data['tipo'])  if busquedaform.cleaned_data['tipo'] else data
            data = data.filter(proveedor_id=busquedaform.cleaned_data['proveedor'])  if busquedaform.cleaned_data['proveedor'] else data
            data = data.filter(ubicacion=busquedaform.cleaned_data['ubicacion'])  if busquedaform.cleaned_data['ubicacion'] else data
            context['articulos_list']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = ArticuloBusqueda()

    return render(request, "Articulos/estructura_crud_art.html",context)

def agregar_articulo(request):
    enviado = False
    if request.method == 'POST':
        in_articulo_per = AgregarArticulo(request.POST,request.FILES)
        if in_articulo_per.is_valid():
            
            in_articulo_per.save()
            return HttpResponseRedirect('agregarart?enviado=True')
    else:
        in_articulo_per= AgregarArticulo()
        if 'enviado' in request.GET:
            enviado = True
    context = {
        'in_articulo_per':in_articulo_per,
        'enviado':enviado, 
        'img_obj': in_articulo_per.instance,
        'search_list_prov':Proveedores.objects.all()
    }
    return render(request, "Articulos/formulario_insertar_articulo.html", context)

def ver_articulo(request,id):
    articulo_list = Articulos.objects.get(id=id)
    context = {
        'art': articulo_list
    }
    return render(request, "Articulos/articulo.html", context)

def editar_articulo(request, id):
    articulo_put = Articulos.objects.get(id=id)
    in_articulo_per = AgregarArticulo(request.POST or None, instance=articulo_put)
    if in_articulo_per.is_valid():
            in_articulo_per.save()       
            return redirect('art')
    context = {
        'in_articulo_per':in_articulo_per,
        'search_list_prov':Proveedores.objects.all()
    }    
    return render(request, "Articulos/formulario_insertar_articulo.html", context)

def eliminar_articulo(request,id):
    enviado = False
    del_articulo = Articulos.objects.filter(id=id)
    red = request.POST.get('art','/erp/art/')
    if request.method =="POST":
        del_articulo.delete()
        return HttpResponseRedirect(red)
    context = {
        'enviado':enviado
    }
    return render(request, "Articulos/delete_articulo.html", context)
