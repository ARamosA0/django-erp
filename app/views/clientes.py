from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

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
            context['clientes_list']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = ClienteBusqueda()

    return render(request, "Clientes/estructura_crud_clie.html", context)



def agregar_cliente(request):
    enviado_per = False
    enviado_emp = False
    reg_porventa = False
    if request.method == "POST":
        form_persona = AgregarPersona(request.POST)
        form_empresa = AgregarEmpresa(request.POST)
        form_cliente = ClienteClienteInsertar(request.POST)
        if form_persona.is_valid() and form_cliente.is_valid():
            form_persona.save()
            buscar_ultima_persona = Persona.objects.last()
            ultima_persona = buscar_ultima_persona.id

            ruccliente = form_cliente.data.get("ruc")
            codformapago = form_cliente.data.get("codformapago")
            cliente = Clientes()
            cliente.persona_id = int(ultima_persona)
            cliente.ruc = int(ruccliente)
            cliente.codformapago_id = int(codformapago)

            cliente.save()
            if 'registro_from_ventas' in request.GET:
                return HttpResponseRedirect('agregarclie?enviado_per=True&registro_from_ventas=True')
            return HttpResponseRedirect('agregarclie?enviado_per=True')
        elif form_empresa.is_valid() and form_cliente.is_valid():
            form_empresa.save()
            buscar_ultima_empresa = Empresa.objects.last()
            ultima_empresa = buscar_ultima_empresa.id

            ruccliente = form_cliente.data.get("ruc")
            codformapago = form_cliente.data.get("codformapago")
            cliente = Clientes()
            cliente.empresa_id = int(ultima_empresa)
            cliente.ruc = int(ruccliente)
            cliente.codformapago_id = int(codformapago)

            cliente.save()
            if 'registro_from_ventas' in request.GET:
                return HttpResponseRedirect('agregarclie?enviado_per=True&registro_from_ventas=True')
            return HttpResponseRedirect('agregarclie?enviado_per=True')
    else:
        form_persona = AgregarPersona
        form_empresa = AgregarEmpresa
        form_cliente = ClienteClienteInsertar
        if 'enviado_per' in request.GET:
            enviado_per = True
            if 'registro_from_ventas' in request.GET:
                reg_porventa = True
        elif 'enviado_emp' in request.GET:
            enviado_emp = True
            if 'registro_from_ventas' in request.GET:
                reg_porventa = True
        

    context ={
        'form_persona':form_persona, 
        'form_empresa':form_empresa,
        'form_cliente': form_cliente,
        'enviado_per':enviado_per,
        'enviado_emp':enviado_emp,
        'reg_porventa':reg_porventa
    }

    return render(request,"Clientes/formulario_insertar_cliente.html", context)

def ver_cliente(request, id):
    cliente_list = Clientes.objects.get(id=id)
    context = {
        'clie': cliente_list
    }
    return render(request, "Clientes/cliente.html", context)

def editar_cliente(request, id):
    enviado_per = False
    enviado_emp = False

    editar_per = True
    editar_emp = True

    cliente = Clientes.objects.get(id=id)

    persona_put = cliente.persona_id 
    empresa_put = cliente.empresa_id 

    if persona_put == None:
        persona_put = 0
        enviado_per = False
        enviado_emp = True

        # if not enviado_per:
        #     editar_per = True

    elif empresa_put == None:
        empresa_put = 0
        enviado_emp = False
        enviado_per = True

        # if not enviado_emp:
        #     editar_emp = True

    form_empresa = AgregarEmpresa(request.POST)
    form_persona = AgregarPersona(request.POST)

    if persona_put == 0:
        empresa = Empresa.objects.get(id= int(empresa_put))
        form_empresa = AgregarEmpresa(request.POST or None, instance=empresa)
        if form_empresa.is_valid():
            form_empresa.save()
            return redirect('clie')

    elif empresa_put == 0:
        persona = Persona.objects.get(id= int(persona_put))
        form_persona = AgregarPersona(request.POST or None, instance=persona)
        if form_persona.is_valid():
            form_persona.save()
            return redirect('clie')

    context = {
        'form_empresa':form_empresa,
        'form_persona':form_persona,
        'enviado_per':enviado_per,
        'enviado_emp':enviado_emp,
        'editar_emp':editar_emp,
        'editar_per':editar_per
    }

    return render(request, "Clientes/formulario_insertar_cliente.html", context)

def eliminar_cliente(request, id):
    enviado = False
    
    cliente = Clientes.objects.get(id=id)

    persona_p = cliente.persona_id 
    empresa_p = cliente.empresa_id 

    if persona_p == None:
        persona_p = 0
    elif empresa_p == None:
        empresa_p = 0

    print(persona_p)
    print(empresa_p)

    red = request.POST.get('clie', '/erp/clie/')

    if persona_p == 0:
        empresa = Empresa.objects.get(id= int(empresa_p))

        if request.method =="POST":
            cliente.delete()
            empresa.delete()
            return HttpResponseRedirect(red)
    elif empresa_p == 0:
        persona = Persona.objects.get(id= int(persona_p))

        if request.method =="POST":
            cliente.delete()
            persona.delete()
            return HttpResponseRedirect(red)

    context = {
        'enviado':enviado
    }
    
    return render(request, "Proveedores/delete_proveedor.html", context)
        
