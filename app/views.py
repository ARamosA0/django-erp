from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView, FormView,CreateView
from .models import *
from .forms import *

# Create your views here.


# class Proveedores(CreateView):
#     model = Proveedores
#     form_class = ProveedorBusqueda
#     template_name = "Pag/proveedores.html"
    # fields = '__all__'


def proveedores(request):
    proveedores_list = Proveedores.objects.all()

    if request.method == 'POST':
        busquedaform = ProveedorBusqueda(request.POST)
    else:
        busquedaform = ProveedorBusqueda()

    context ={
        'proveedores_list': proveedores_list,
        'busquedaform': busquedaform
    }
    return render(request, "Pag/proveedores.html", context)

# def buscar_proveedor(request):
    
#     data = Proveedores.objects.values('pk','persona_id','persona_id__nombre',
#                                              'persona_id__dni','persona_id__localidad',
#                                              'persona_id__direccion','persona_id__codpostal',
#                                              'persona_id__cuentabancaria','persona_id__telefono',
#                                              'persona_id__movil','persona_id__web',
#                                              'persona_id__codprovincia_id').filter(borrado='0')
    
#     data = data.filter(pk=request.POST['codigo'])  if request.POST['codigo'] else data
#     data = data.filter(persona_id__dni=request.POST['dni'])  if request.POST['dni'] else data
#     data = data.filter(persona_id__nombre=request.POST['nombre'])  if request.POST['nombre'] else data
#     data = data.filter(persona_id__telefono=request.POST['telefono'])  if request.POST['telefono'] else data
#     data = data.filter(persona_id__codprovincia_id=request.POST['provincia'])  if request.POST['provincia']!='0' else data
#     data = data.filter(persona_id__localidad=request.POST['localidad'])  if request.POST['localidad'] else data
#     data = data.filter(persona_id__web=request.POST['web'])  if request.POST['web'] else data
    
#     context = {'proveedores': data}
#     #print(data)
#     return  render(request,"find_test.html",context)


def agregar_proveedor(request):
    enviado = False

    if request.method == "POST":
        form = ProveedorAgregar(request.POST)
        if form. is_valid():
            form.save()

            buscar_ultima_persona = Persona.objects.last()
            ultima_persona = buscar_ultima_persona.id

            print(buscar_ultima_persona)

            proveedor = Proveedores()
            proveedor.persona_id = int(ultima_persona)
            proveedor.save()

            print(proveedor)

            return HttpResponseRedirect('agregarprov?enviado=True')
    else:
        form = ProveedorAgregar
        if 'enviado' in request.GET:
            enviado = True

    context ={
        'form':form, 
        'enviado':enviado
    }

    return render(request,"Formulario/formulario_insertar_proveedor.html", context)


def clientes(request):
    clientes_list = Clientes.objects.all()

    if request.method == 'POST':
        busquedaform = ProveedorBusqueda(request.POST)
    else:
        busquedaform = ProveedorBusqueda()

    context ={
        'clientes_list': clientes_list,
        'busquedaform': busquedaform
    }
    return render(request, "Pag/clientes.html", context)

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

            # print(cliente)

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
    return render(request, "Formulario/formulario_insertar_cliente.html", context)




        