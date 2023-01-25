from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

def trabajadores(request):
    trabajadores_list = Trabajador.objects.all()
    busquedaform = TrabajadorBusqueda()
    
    context = {
        'trabajadores_list':trabajadores_list,
        'contador':len(trabajadores_list),
        'busquedaform': busquedaform
    }

    if request.method == 'POST':
        busquedaform = TrabajadorBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Trabajador.objects.filter(borrado='0')
            data = data.filter(pk=busquedaform.cleaned_data['codigo']) if busquedaform.cleaned_data['codigo'] else data
            data = data.filter(tipo_trabajador=busquedaform.cleaned_data['tipo']) if busquedaform.cleaned_data['tipo'] else data
            if str(busquedaform.cleaned_data['persona']) == 'True':    
                data = data.filter(empresa_id=None)
                data = data.filter(persona_id__nombre=busquedaform.cleaned_data['nombre'])  if busquedaform.cleaned_data['nombre'] else data
                data = data.filter(persona_id__telefono=busquedaform.cleaned_data['telefono'])  if busquedaform.cleaned_data['telefono'] else data
                data = data.filter(persona_id__codprovincia_id=busquedaform.cleaned_data['provincia'])  if busquedaform.cleaned_data['provincia'] else data
                data = data.filter(persona_id__localidad=busquedaform.cleaned_data['localidad'])  if busquedaform.cleaned_data['localidad'] else data
            else:
                data = data.filter(persona_id=None)
                data = data.filter(empresa_id__nombre=busquedaform.cleaned_data['nombre'])  if busquedaform.cleaned_data['nombre'] else data
                data = data.filter(empresa_id__telefono=busquedaform.cleaned_data['telefono'])  if busquedaform.cleaned_data['telefono'] else data
                data = data.filter(empresa_id__codprovincia_id=busquedaform.cleaned_data['provincia'])  if busquedaform.cleaned_data['provincia'] else data
                data = data.filter(empresa_id__localidad=busquedaform.cleaned_data['localidad'])  if busquedaform.cleaned_data['localidad'] else data
                
            context['trabajadores_list']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = TrabajadorBusqueda()

    return render(request, "Trabajadores/estructura_crud_trabajadores.html", context) 

def agregar_trabajador(request):
    enviado_per = False
    enviado_emp = False
    
    if request.method == "POST":
        form_persona = AgregarPersona(request.POST)
        form_empresa = AgregarEmpresa(request.POST)
        form_trabajador = AgregarTrabajador(request.POST)


        if form_persona.is_valid() and form_trabajador.is_valid():
            form_persona.save()
            buscar_ultima_persona = Persona.objects.last()
            ultima_persona = buscar_ultima_persona.id

            tipo = form_trabajador.data.get("tipo_trabajador")
            trabajador = Trabajador()
            trabajador.persona_id = int(ultima_persona)
            trabajador.tipo = tipo
            trabajador.save()

            return HttpResponseRedirect('agregartrab?enviado_per=True')
        
        elif form_empresa.is_valid() and form_trabajador.is_valid():
            form_empresa.save()
            buscar_ultima_empresa = Empresa.objects.last()
            ultima_empresa = buscar_ultima_empresa.id

            tipo = form_trabajador.data.get("tipo_trabajador")
            trabajador = Trabajador()
            trabajador.empresa_id = int(ultima_empresa)
            trabajador.tipo = tipo
            trabajador.save()

            return HttpResponseRedirect('agregartrab?enviado_emp=True')
    else:
        form_persona = AgregarPersona
        form_empresa = AgregarEmpresa
        form_trabajador = AgregarTrabajador
        if 'enviado_per' in request.GET:
            enviado_per = True
        elif 'enviado_emp' in request.GET:
            enviado_emp = True
        

    context ={
        'form_persona':form_persona, 
        'form_empresa':form_empresa,
        'form_trabajador': form_trabajador,
        'enviado_per':enviado_per,
        'enviado_emp':enviado_emp,
    }

    return render(request, "Trabajadores/formulario_insertar_trabajador.html", context)

def ver_trabajador(request, id):
    trabajador_list = Trabajador.objects.get(id=id)
    context = {
        'trab': trabajador_list
    }
    return render(request, "Trabajadores/trabajador.html", context)

def editar_trabajador(request, id):
    enviado_per = False
    enviado_emp = False

    editar_per = True
    editar_emp = True

    trabajador = Trabajador.objects.get(id=id)

    persona_put = trabajador.persona_id 
    empresa_put = trabajador.empresa_id 

    if persona_put == None:
        persona_put = 0
        enviado_per = False
        enviado_emp = True

    elif empresa_put == None:
        empresa_put = 0
        enviado_emp = False
        enviado_per = True

    form_empresa = AgregarEmpresa(request.POST)
    form_persona = AgregarPersona(request.POST)
    form_trabajador = AgregarTrabajador(request.POST)

    if persona_put == 0:
        empresa = Empresa.objects.get(id= int(empresa_put))
        form_empresa = AgregarEmpresa(request.POST or None, instance=empresa)

        form_trabajador = AgregarTrabajador(request.POST or None, instance=trabajador)

        if form_empresa.is_valid():
            form_empresa.save()
            form_trabajador.save()
            return redirect('trabajador')

    elif empresa_put == 0:
        persona = Persona.objects.get(id= int(persona_put))
        form_persona = AgregarPersona(request.POST or None, instance=persona)

        form_trabajador = AgregarTrabajador(request.POST or None, instance=trabajador)

        if form_persona.is_valid():
            form_persona.save()
            form_trabajador.save()
            return redirect('trabajador')

    context = {
        'form_empresa':form_empresa,
        'form_persona':form_persona,
        'form_trabajador':form_trabajador,
        'enviado_per':enviado_per,
        'enviado_emp':enviado_emp,
        'editar_emp':editar_emp,
        'editar_per':editar_per
    }

    return render(request, "Trabajadores/formulario_insertar_trabajador.html", context)

def eliminar_trabajador(request, id):
    enviado = False
    
    trabajador = Trabajador.objects.get(id=id)

    persona_p = trabajador.persona_id 
    empresa_p = trabajador.empresa_id 

    if persona_p == None:
        persona_p = 0
    elif empresa_p == None:
        empresa_p = 0

    print(persona_p)
    print(empresa_p)

    red = request.POST.get('trabajador', '/erp/trabajador/')

    if persona_p == 0:
        empresa = Empresa.objects.get(id= int(empresa_p))

        if request.method =="POST":
            trabajador.delete()
            empresa.delete()
            return HttpResponseRedirect(red)
    elif empresa_p == 0:
        persona = Persona.objects.get(id= int(persona_p))

        if request.method =="POST":
            trabajador.delete()
            persona.delete()
            return HttpResponseRedirect(red)

    context = {
        'enviado':enviado
    }
    
    return render(request, "Trabajadores/delete_trabajador.html", context)