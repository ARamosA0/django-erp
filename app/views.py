from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView, FormView,CreateView
from django.shortcuts import redirect
from .models import *
from .forms import *

#PROVEEDORES

def proveedores(request):
    proveedores_list = Proveedores.objects.all()
    busquedaform = ProveedorBusqueda()
    context ={
        'proveedores_list': proveedores_list,
        'busquedaform': busquedaform
    }
    if request.method == 'POST':
        busquedaform = ProveedorBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Proveedores.objects.filter(borrado='0')
            data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
            data = data.filter(persona_id__dni=busquedaform.cleaned_data['dni'])  if busquedaform.cleaned_data['dni'] else data
            data = data.filter(persona_id__nombre=busquedaform.cleaned_data['nombre'])  if busquedaform.cleaned_data['nombre'] else data
            data = data.filter(persona_id__telefono=busquedaform.cleaned_data['telefono'])  if busquedaform.cleaned_data['telefono'] else data
            data = data.filter(persona_id__codprovincia_id=busquedaform.cleaned_data['provincia'])  if busquedaform.cleaned_data['provincia'] else data
            data = data.filter(persona_id__localidad=busquedaform.cleaned_data['localidad'])  if busquedaform.cleaned_data['localidad'] else data
            context['proveedores_list']=data
            context['busquedaform']=busquedaform

    return render(request, "Proveedores/estructura_crud.html", context)



def agregar_proveedor(request):
    enviado = False

    if request.method == "POST":
        form = ProveedorAgregar(request.POST)
        if form. is_valid():
            form.save()
            buscar_ultima_persona = Persona.objects.last()
            ultima_persona = buscar_ultima_persona.id
            proveedor = Proveedores()
            proveedor.persona_id = int(ultima_persona)
            proveedor.save()
            return HttpResponseRedirect('agregarprov?enviado=True')
    else:
        form = ProveedorAgregar
        if 'enviado' in request.GET:
            enviado = True

    context ={
        'form':form, 
        'enviado':enviado
    }

    return render(request,"Proveedores/formulario_insertar_proveedor.html", context)

#CLIENTES

def clientes(request):
    clientes_list = Clientes.objects.all()
    busquedaform = ProveedorBusqueda()
    context ={
        'clientes_list': clientes_list,
        'busquedaform': busquedaform
    }
    if request.method == 'POST':
        busquedaform = ProveedorBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Clientes.objects.filter(borrado='0')
            data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
            data = data.filter(persona_id__dni=busquedaform.cleaned_data['dni'])  if busquedaform.cleaned_data['dni'] else data
            data = data.filter(persona_id__nombre=busquedaform.cleaned_data['nombre'])  if busquedaform.cleaned_data['nombre'] else data
            data = data.filter(persona_id__telefono=busquedaform.cleaned_data['telefono'])  if busquedaform.cleaned_data['telefono'] else data
            data = data.filter(persona_id__codprovincia_id=busquedaform.cleaned_data['provincia'])  if busquedaform.cleaned_data['provincia'] else data
            data = data.filter(persona_id__localidad=busquedaform.cleaned_data['localidad'])  if busquedaform.cleaned_data['localidad'] else data
            context['clientes_list']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = ProveedorBusqueda()

    return render(request, "Clientes/estructura_crud_clie.html", context)



def agregar_cliente(request):
    enviado = False
    codformpago=""
    if request.method == 'POST':
        in_cliente_per = ProveedorAgregar(request.POST)
        in_cliente = ClienteClienteInsertar(request.POST)
        if in_cliente_per.is_valid() and in_cliente.is_valid():
            in_cliente_per.save()
            buscar_ultima_persona = Persona.objects.last()
            ultima_persona = buscar_ultima_persona.id
            #Se extrae la data como string del formulario
            codformpago = in_cliente.data.get("codformapago")  
            print(codformpago)
            print(type(codformpago))
            cliente = Clientes()
            cliente.persona_id = int(ultima_persona)
            cliente.codformapago_id = int(codformpago)
            cliente.save()
            return HttpResponseRedirect('agregarclie?enviado=True')
    else:
        in_cliente_per= ProveedorAgregar()
        in_cliente=ClienteClienteInsertar()
        if 'enviado' in request.GET:
            enviado = True
    context = {
        'in_cliente_per':in_cliente_per,
        'in_cliente':in_cliente,
        'enviado':enviado, 
    }
    return render(request, "Clientes/formulario_insertar_cliente.html", context)


def ver_cliente(request, id):
    cliente_list = Clientes.objects.get(persona__id=id)
    context = {
        'clie': cliente_list
    }
    return render(request, "Clientes/cliente.html", context)

def editar_cliente(request, id):
    enviado = False
    codformpago=""
    persona_put = Persona.objects.get(id=id)
    cliente_put = Clientes.objects.get(persona__id=id)
    if request.method == 'POST':
        in_cliente_per = ProveedorAgregar(request.POST, instance=persona_put)
        in_cliente = ClienteClienteInsertar(request.POST, instance=cliente_put)
        if in_cliente_per.is_valid() and in_cliente.is_valid():
            in_cliente_per.save()
            buscar_ultima_persona = Persona.objects.last()
            ultima_persona = buscar_ultima_persona.id
            #Se extrae la data como string del formulario
            codformpago = in_cliente.data.get("codformapago")  
            print(codformpago)
            print(type(codformpago))
            cliente = Clientes()
            cliente.persona_id = int(ultima_persona)
            cliente.codformapago_id = int(codformpago)
            cliente.save()
            return redirect('clie')
    else:
        in_cliente_per= ProveedorAgregar(instance=persona_put)
        in_cliente=ClienteClienteInsertar(instance=cliente_put)
        if 'enviado' in request.GET:
            enviado = True
    context = {
        'cliente_put':cliente_put,
        'in_cliente_per':in_cliente_per,
        'in_cliente':in_cliente,
        'enviado':enviado, 
    }    
    return render(request, "Clientes/formulario_insertar_cliente.html", context)

def eliminar_cliente(request, id):
    del_cliente = Clientes.objects.filter(persona__id=id)
    del_persona = Persona.objects.filter(id=id)
    if request.method =="POST":
        del_cliente.delete()
        del_persona.delete()
        return HttpResponseRedirect('clie')
    return render(request, "Formulario/form_delete.html")
        


#ARTICULOS

def articulos(request):
    # clientes_list = Clientes.objects.all()
    # busquedaform = ArticuloBusqueda()
    # context ={
    #     'clientes_list': clientes_list,
    #     'busquedaform': busquedaform
    # }
    return render(request, "Articulos/estructura_crud_art.html")

#FAMILIAS, CATEGORIAS

def familias(request):
    # clientes_list = Clientes.objects.all()
    # busquedaform = FamiliaBusqueda()
    # context ={
    #     'clientes_list': clientes_list,
    #     'busquedaform': busquedaform
    # }
    return render(request, "Categorias/estructura_crud_cat.html")

