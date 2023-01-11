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
        'busquedaform': busquedaform,
        'contador':len(proveedores_list),
        'num':0
    }
    if request.method == 'POST':
        busquedaform = ProveedorBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Proveedores.objects.filter(borrado='0')
            data = data.filter(pk=busquedaform.cleaned_data['codigo']) if busquedaform.cleaned_data['codigo'] else data
            data = data.filter(ruc=busquedaform.cleaned_data['ruc']) if busquedaform.cleaned_data['ruc'] else data
            if str(busquedaform.cleaned_data['empresa']) == 'True':
                data = data.filter(persona_id=None)
                data = data.filter(empresa_id__nombre=busquedaform.cleaned_data['nombre'])  if busquedaform.cleaned_data['nombre'] else data
                data = data.filter(empresa_id__telefono=busquedaform.cleaned_data['telefono'])  if busquedaform.cleaned_data['telefono'] else data
                data = data.filter(empresa_id__codprovincia_id=busquedaform.cleaned_data['provincia'])  if busquedaform.cleaned_data['provincia'] else data
                data = data.filter(empresa_id__localidad=busquedaform.cleaned_data['localidad'])  if busquedaform.cleaned_data['localidad'] else data
            else:
                data = data.filter(empresa_id=None)
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
        form_persona = AgregarPersona(request.POST)
        form_empresa = AgregarEmpresa(request.POST)
        form_proveedor = ProveedorProveedorInsertar(request.POST)
        if form_persona.is_valid() and form_proveedor.is_valid():
            form_persona.save()
            buscar_ultima_persona = Persona.objects.last()
            ultima_persona = buscar_ultima_persona.id

            rucproveedor = form_proveedor.data.get("ruc")
            proveedor = Proveedores()
            proveedor.persona_id = int(ultima_persona)
            proveedor.ruc = int(rucproveedor)

            proveedor.save()
            return HttpResponseRedirect('agregarprov?enviado=True')
        elif form_empresa.is_valid() and form_proveedor.is_valid():
            form_empresa.save()
            buscar_ultima_empresa = Empresa.objects.last()
            ultima_empresa = buscar_ultima_empresa.id

            rucproveedor = form_proveedor.data.get("ruc")
            proveedor = Proveedores()
            proveedor.empresa_id = int(ultima_empresa)
            proveedor.ruc = int(rucproveedor)

            proveedor.save()
            return HttpResponseRedirect('agregarprov?enviado=True')
    else:
        form_persona = AgregarPersona
        form_empresa = AgregarEmpresa
        form_proveedor = ProveedorProveedorInsertar
        if 'enviado' in request.GET:
            enviado = True

    context ={
        'form_persona':form_persona, 
        'form_empresa':form_empresa,
        'form_proveedor': form_proveedor,
        'enviado':enviado
    }

    return render(request,"Proveedores/formulario_insertar_proveedor.html", context)

def eliminar_proveedor(request, id):
    proveedor = Proveedores.objects.get(id=id)

    persona_p = proveedor.persona_id 
    empresa_p = proveedor.empresa_id 

    if persona_p == None:
        persona_p = 0
    elif empresa_p == None:
        empresa_p = 0

    print(persona_p)
    print(empresa_p)

    if persona_p == 0:
        empresa = Empresa.objects.get(id= int(empresa_p))
        proveedor.delete()
        empresa.delete()
    elif empresa_p == 0:
        persona = Persona.objects.get(id= int(persona_p))
        proveedor.delete()
        persona.delete()

    return redirect('prov')

def ver_proveedor(request, id):
    prov = Proveedores.objects.get(id=id)
    context = {
        'prov':prov,
    }

    return render(request, 'Proveedores/proveedor.html', context)

def editar_proveedor(request, id):

    proveedor = Proveedores.objects.get(id=id)

    persona_put = proveedor.persona_id 
    empresa_put = proveedor.empresa_id 

    if persona_put == None:
        persona_put = 0
    elif empresa_put == None:
        empresa_put = 0

    form_empresa = AgregarEmpresa(request.POST)
    form_persona = AgregarPersona(request.POST)

    if persona_put == 0:
        empresa = Empresa.objects.get(id= int(empresa_put))
        form_empresa = AgregarEmpresa(request.POST or None, instance=empresa)
        if form_empresa.is_valid():
            form_empresa.save()
            return redirect('prov')

    elif empresa_put == 0:
        persona = Persona.objects.get(id= int(persona_put))
        form_persona = AgregarPersona(request.POST or None, instance=persona)
        if form_persona.is_valid():
            form_persona.save()
            return redirect('prov')

    context = {
        'form_empresa':form_empresa,
        'form_persona':form_persona,
    }

    return render(request, "Proveedores/formulario_insertar_proveedor.html", context)

#CLIENTES
def clientes(request):
    clientes_list = Clientes.objects.all()
    busquedaform = ClienteBusqueda()
    context ={
        'clientes_list': clientes_list,
        'busquedaform': busquedaform
    }
    if request.method == 'POST':
        busquedaform = ClienteBusqueda(request.POST)
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
        busquedaform = ClienteBusqueda()

    return render(request, "Clientes/estructura_crud_clie.html", context)



def agregar_cliente(request):
    enviado = False
    codformpago=""
    if request.method == 'POST':
        in_cliente_per = AgregarPersona(request.POST)
        in_cliente = ClienteClienteInsertar(request.POST)
        if in_cliente_per.is_valid() and in_cliente.is_valid():
            in_cliente_per.save()
            buscar_ultima_persona = Persona.objects.last()
            ultima_persona = buscar_ultima_persona.id
            #Se extrae la data como string del formulario
            codformpago = in_cliente.data.get("codformapago")  
            cliente = Clientes()
            cliente.persona_id = int(ultima_persona)
            cliente.codformapago_id = int(codformpago)
            cliente.save()
            return HttpResponseRedirect('agregarclie?enviado=True')
    else:
        in_cliente_per= AgregarPersona()
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
        in_cliente_per = AgregarPersona(request.POST, instance=persona_put)
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
        in_cliente_per= AgregarPersona(instance=persona_put)
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
    enviado = False
    del_cliente = Clientes.objects.filter(persona__id=id)
    del_persona = Persona.objects.filter(id=id)
    red = request.POST.get('clie','/erp/clie/')
    if request.method =="POST":
        del_cliente.delete()
        del_persona.delete()
        return HttpResponseRedirect(red)
    context = {
        'enviado':enviado
    }
    return render(request, "Clientes/de/eliminar/8/erp/clie/lete_cliente.html", context)
        

#ARTICULOS

def articulos(request):
    articulos_list = Articulos.objects.all()
    busquedaform = ArticuloBusqueda()
    context ={
        'articulos_list': articulos_list,
        'busquedaform': busquedaform
    }

    if request.method == 'POST':
        busquedaform = ArticuloBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Articulos.objects.all()
            data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
            
            data = data.filter(referencia=busquedaform.cleaned_data['referencia'])  if busquedaform.cleaned_data['referencia'] else data
            data = data.filter(familia=busquedaform.cleaned_data['familia'])  if busquedaform.cleaned_data['familia'] else data
            data = data.filter(descripcion=busquedaform.cleaned_data['descripcion'])  if busquedaform.cleaned_data['descripcion'] else data
            #data = data.filter(proveedor_1_id__persona_id__nombre=busquedaform.cleaned_data['proveedor_1'])  if busquedaform.cleaned_data['proveedor_1'] else data
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
    }    
    return render(request, "Articulos/formulario_insertar_articulo.html", context)

def eliminar_articulo(request,id):
    enviado = False
    del_articulo = Articulos.objects.filter(id=id)
    if request.method =="POST":
        del_articulo.delete()
        return HttpResponseRedirect('?enviado=True')
    context = {
        'enviado':enviado
    }
    return render(request, "Articulos/delete_articulo.html", context)

#FAMILIAS, CATEGORIAS

def familias(request):
    familias_list = Familia.objects.all()
    busquedaform = FamiliaBusqueda()
    context ={
        'familias_list': familias_list,
        'busquedaform': busquedaform
    }
    if request.method == 'POST':
        busquedaform = FamiliaBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Familia.objects.filter(borrado='0')
            data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
            data = data.filter(nombre=busquedaform.cleaned_data['nombre'])  if busquedaform.cleaned_data['nombre'] else data
            context['familias_list']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = FamiliaBusqueda()
    return render(request, "Familias/estructura_crud_fam.html",context)

# FACTURA ALBANARES
def fac_albanar(request):
    return 
def agregar_familia(request):
    enviado = False
    if request.method == 'POST':
        in_familia_per = AgregarFamilia(request.POST)
        if in_familia_per.is_valid():
            in_familia_per.save()
            return HttpResponseRedirect('agregarfam?enviado=True')

    else:
        in_familia_per= AgregarFamilia()
        if 'enviado' in request.GET:
            enviado = True
    context = {
        'in_familia_per':in_familia_per,
        'enviado':enviado, 
    }
    return render(request, "Familias/formulario_insertar_familia.html", context)

def ver_familia(request, id):
    familia_list = Familia.objects.get(id=id)
    context = {
        'fam': familia_list
    }
    return render(request, "Familias/familia.html", context)

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
    if request.method =="POST":
        del_familia.delete()
        return HttpResponseRedirect('?enviado=True')
    context = {
        'enviado':enviado
    }
    return render(request, "Familias/delete_familia.html", context)


#VENTAS CLIENTES
def reg_venta(request):
    elemento_venta_form = NuevoElemento()
    codigoarticulo = elemento_venta_form.data.get("codigoarticulo") 
    if request.method == 'POST': 
        articulo_venta = Articulos.objects.filter(id=codigoarticulo)
    context ={
        'elemento_venta_form': elemento_venta_form,
    }
    # Al buscar el codigo de barras del producto se autocompleta la descripcion.
    # El precio incrementa con la cantidad y se  reduce con el descuento
    # Al darle agregar el producto se agrega a una lista
    # La lista se muestra en una tabla con las opciones de eliminar y editar. 
    # Solo se podra editar la cantidad 
    
    return render(request, "VentaClientes/registroventa.html", context)

# FACTURAS VENTAS CLIENTE
def facturas(request):
    return

# ALBANARES
def albanar(request):
    return 
