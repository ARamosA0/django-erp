from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *


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
    enviado_per = False
    enviado_emp = False

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
            return HttpResponseRedirect('agregarprov?enviado_per=True')
        elif form_empresa.is_valid() and form_proveedor.is_valid():
            form_empresa.save()
            buscar_ultima_empresa = Empresa.objects.last()
            ultima_empresa = buscar_ultima_empresa.id

            rucproveedor = form_proveedor.data.get("ruc")
            proveedor = Proveedores()
            proveedor.empresa_id = int(ultima_empresa)
            proveedor.ruc = int(rucproveedor)

            proveedor.save()
            return HttpResponseRedirect('agregarprov?enviado_emp=True')
    else:
        form_persona = AgregarPersona
        form_empresa = AgregarEmpresa
        form_proveedor = ProveedorProveedorInsertar
        if 'enviado_per' in request.GET:
            enviado_per = True
        elif 'enviado_emp' in request.GET:
            enviado_emp = True

    context ={
        'form_persona':form_persona, 
        'form_empresa':form_empresa,
        'form_proveedor': form_proveedor,
        'enviado_per':enviado_per,
        'enviado_emp':enviado_emp
    }

    return render(request,"Proveedores/formulario_insertar_proveedor.html", context)

def eliminar_proveedor(request, id):
    enviado = False
    
    proveedor = Proveedores.objects.get(id=id)

    persona_p = proveedor.persona_id 
    empresa_p = proveedor.empresa_id 

    if persona_p == None:
        persona_p = 0
    elif empresa_p == None:
        empresa_p = 0

    print(persona_p)
    print(empresa_p)

    red = request.POST.get('prov', '/erp/prov/')

    if persona_p == 0:
        empresa = Empresa.objects.get(id= int(empresa_p))

        if request.method =="POST":
            proveedor.delete()
            empresa.delete()
            return HttpResponseRedirect(red)
    elif empresa_p == 0:
        persona = Persona.objects.get(id= int(persona_p))

        if request.method =="POST":
            proveedor.delete()
            persona.delete()
            return HttpResponseRedirect(red)

    context = {
        'enviado':enviado
    }
    
    return render(request, "Proveedores/delete_proveedor.html", context)

def ver_proveedor(request, id):
    prov = Proveedores.objects.get(id=id)
    context = {
        'prov':prov,
    }

    return render(request, 'Proveedores/proveedor.html', context)

def editar_proveedor(request, id):
    enviado_per = False
    enviado_emp = False

    editar_per = True
    editar_emp = True

    proveedor = Proveedores.objects.get(id=id)

    persona_put = proveedor.persona_id 
    empresa_put = proveedor.empresa_id 

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
        'enviado_per':enviado_per,
        'enviado_emp':enviado_emp,
        'editar_emp':editar_emp,
        'editar_per':editar_per
    }

    return render(request, "Proveedores/formulario_insertar_proveedor.html", context)
