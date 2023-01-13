from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView, FormView,CreateView
from django.shortcuts import redirect
from .models import *
from .forms import *

# #PROVEEDORES

# def proveedores(request):
#     proveedores_list = Proveedores.objects.all()
#     busquedaform = ProveedorBusqueda()
#     context ={
#         'proveedores_list': proveedores_list,
#         'busquedaform': busquedaform,
#         'contador':len(proveedores_list),
#         'num':0
#     }
#     if request.method == 'POST':
#         busquedaform = ProveedorBusqueda(request.POST)
#         if busquedaform.is_valid():
#             data = Proveedores.objects.filter(borrado='0')
#             data = data.filter(pk=busquedaform.cleaned_data['codigo']) if busquedaform.cleaned_data['codigo'] else data
#             data = data.filter(ruc=busquedaform.cleaned_data['ruc']) if busquedaform.cleaned_data['ruc'] else data
#             if str(busquedaform.cleaned_data['empresa']) == 'True':
#                 data = data.filter(persona_id=None)
#                 data = data.filter(empresa_id__nombre=busquedaform.cleaned_data['nombre'])  if busquedaform.cleaned_data['nombre'] else data
#                 data = data.filter(empresa_id__telefono=busquedaform.cleaned_data['telefono'])  if busquedaform.cleaned_data['telefono'] else data
#                 data = data.filter(empresa_id__codprovincia_id=busquedaform.cleaned_data['provincia'])  if busquedaform.cleaned_data['provincia'] else data
#                 data = data.filter(empresa_id__localidad=busquedaform.cleaned_data['localidad'])  if busquedaform.cleaned_data['localidad'] else data
#             else:
#                 data = data.filter(empresa_id=None)
#                 data = data.filter(persona_id__nombre=busquedaform.cleaned_data['nombre'])  if busquedaform.cleaned_data['nombre'] else data
#                 data = data.filter(persona_id__telefono=busquedaform.cleaned_data['telefono'])  if busquedaform.cleaned_data['telefono'] else data
#                 data = data.filter(persona_id__codprovincia_id=busquedaform.cleaned_data['provincia'])  if busquedaform.cleaned_data['provincia'] else data
#                 data = data.filter(persona_id__localidad=busquedaform.cleaned_data['localidad'])  if busquedaform.cleaned_data['localidad'] else data
#             context['proveedores_list']=data
#             context['busquedaform']=busquedaform
#     return render(request, "Proveedores/estructura_crud.html", context)



# def agregar_proveedor(request):
#     enviado_per = False
#     enviado_emp = False

#     if request.method == "POST":
#         form_persona = AgregarPersona(request.POST)
#         form_empresa = AgregarEmpresa(request.POST)
#         form_proveedor = ProveedorProveedorInsertar(request.POST)
#         if form_persona.is_valid() and form_proveedor.is_valid():
#             form_persona.save()
#             buscar_ultima_persona = Persona.objects.last()
#             ultima_persona = buscar_ultima_persona.id

#             rucproveedor = form_proveedor.data.get("ruc")
#             proveedor = Proveedores()
#             proveedor.persona_id = int(ultima_persona)
#             proveedor.ruc = int(rucproveedor)

#             proveedor.save()
#             return HttpResponseRedirect('agregarprov?enviado_per=True')
#         elif form_empresa.is_valid() and form_proveedor.is_valid():
#             form_empresa.save()
#             buscar_ultima_empresa = Empresa.objects.last()
#             ultima_empresa = buscar_ultima_empresa.id

#             rucproveedor = form_proveedor.data.get("ruc")
#             proveedor = Proveedores()
#             proveedor.empresa_id = int(ultima_empresa)
#             proveedor.ruc = int(rucproveedor)

#             proveedor.save()
#             return HttpResponseRedirect('agregarprov?enviado_emp=True')
#     else:
#         form_persona = AgregarPersona
#         form_empresa = AgregarEmpresa
#         form_proveedor = ProveedorProveedorInsertar
#         if 'enviado_per' in request.GET:
#             enviado_per = True
#         elif 'enviado_emp' in request.GET:
#             enviado_emp = True

#     context ={
#         'form_persona':form_persona, 
#         'form_empresa':form_empresa,
#         'form_proveedor': form_proveedor,
#         'enviado_per':enviado_per,
#         'enviado_emp':enviado_emp
#     }

#     return render(request,"Proveedores/formulario_insertar_proveedor.html", context)

# def eliminar_proveedor(request, id):
#     enviado = False
    
#     proveedor = Proveedores.objects.get(id=id)

#     persona_p = proveedor.persona_id 
#     empresa_p = proveedor.empresa_id 

#     if persona_p == None:
#         persona_p = 0
#     elif empresa_p == None:
#         empresa_p = 0

#     print(persona_p)
#     print(empresa_p)

#     red = request.POST.get('prov', '/erp/prov/')

#     if persona_p == 0:
#         empresa = Empresa.objects.get(id= int(empresa_p))

#         if request.method =="POST":
#             proveedor.delete()
#             empresa.delete()
#             return HttpResponseRedirect(red)
#     elif empresa_p == 0:
#         persona = Persona.objects.get(id= int(persona_p))

#         if request.method =="POST":
#             proveedor.delete()
#             persona.delete()
#             return HttpResponseRedirect(red)

#     context = {
#         'enviado':enviado
#     }
    
#     return render(request, "Proveedores/delete_proveedor.html", context)

# def ver_proveedor(request, id):
#     prov = Proveedores.objects.get(id=id)
#     context = {
#         'prov':prov,
#     }

#     return render(request, 'Proveedores/proveedor.html', context)

# def editar_proveedor(request, id):
#     enviado_per = False
#     enviado_emp = False

#     editar_per = True
#     editar_emp = True

#     proveedor = Proveedores.objects.get(id=id)

#     persona_put = proveedor.persona_id 
#     empresa_put = proveedor.empresa_id 

#     if persona_put == None:
#         persona_put = 0
#         enviado_per = False
#         enviado_emp = True

#         # if not enviado_per:
#         #     editar_per = True

#     elif empresa_put == None:
#         empresa_put = 0
#         enviado_emp = False
#         enviado_per = True

#         # if not enviado_emp:
#         #     editar_emp = True

#     form_empresa = AgregarEmpresa(request.POST)
#     form_persona = AgregarPersona(request.POST)

#     if persona_put == 0:
#         empresa = Empresa.objects.get(id= int(empresa_put))
#         form_empresa = AgregarEmpresa(request.POST or None, instance=empresa)
#         if form_empresa.is_valid():
#             form_empresa.save()
#             return redirect('prov')

#     elif empresa_put == 0:
#         persona = Persona.objects.get(id= int(persona_put))
#         form_persona = AgregarPersona(request.POST or None, instance=persona)
#         if form_persona.is_valid():
#             form_persona.save()
#             return redirect('prov')

#     context = {
#         'form_empresa':form_empresa,
#         'form_persona':form_persona,
#         'enviado_per':enviado_per,
#         'enviado_emp':enviado_emp,
#         'editar_emp':editar_emp,
#         'editar_per':editar_per
#     }

#     return render(request, "Proveedores/formulario_insertar_proveedor.html", context)

#CLIENTES
# def clientes(request):
#     clientes_list = Clientes.objects.all()
#     busquedaform = ClienteBusqueda()
#     context ={
#         'clientes_list': clientes_list,
#         'busquedaform': busquedaform
#     }
#     if request.method == 'POST':
#         busquedaform = ClienteBusqueda(request.POST)
#         if busquedaform.is_valid():
#             data = Clientes.objects.filter(borrado='0')
#             data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
#             data = data.filter(persona_id__dni=busquedaform.cleaned_data['dni'])  if busquedaform.cleaned_data['dni'] else data
#             data = data.filter(persona_id__nombre=busquedaform.cleaned_data['nombre'])  if busquedaform.cleaned_data['nombre'] else data
#             data = data.filter(persona_id__telefono=busquedaform.cleaned_data['telefono'])  if busquedaform.cleaned_data['telefono'] else data
#             data = data.filter(persona_id__codprovincia_id=busquedaform.cleaned_data['provincia'])  if busquedaform.cleaned_data['provincia'] else data
#             data = data.filter(persona_id__localidad=busquedaform.cleaned_data['localidad'])  if busquedaform.cleaned_data['localidad'] else data
#             context['clientes_list']=data
#             context['busquedaform']=busquedaform
#     else:
#         busquedaform = ClienteBusqueda()

#     return render(request, "Clientes/estructura_crud_clie.html", context)



# def agregar_cliente(request):
#     enviado = False
#     codformpago=""
#     reg_porventa=False
#     if request.method == 'POST':
#         in_cliente_per = AgregarPersona(request.POST)
#         in_cliente = ClienteClienteInsertar(request.POST)
#         if in_cliente_per.is_valid() and in_cliente.is_valid():
#             in_cliente_per.save()
#             buscar_ultima_persona = Persona.objects.last()
#             ultima_persona = buscar_ultima_persona.id
#             #Se extrae la data como string del formulario
#             codformpago = in_cliente.data.get("codformapago")  
#             cliente = Clientes()
#             cliente.persona_id = int(ultima_persona)
#             cliente.codformapago_id = int(codformpago)
#             cliente.save()
#             if 'registro_from_ventas' in request.GET:
#                 return HttpResponseRedirect('agregarclie?enviado=True&registro_from_ventas=True')
#             return HttpResponseRedirect('agregarclie?enviado=True')
#     else:
#         in_cliente_per= AgregarPersona()
#         in_cliente=ClienteClienteInsertar()
#         if 'enviado' in request.GET:
#             enviado = True
#             if 'registro_from_ventas' in request.GET:
#                 reg_porventa = True
#     context = {
#         'in_cliente_per':in_cliente_per,
#         'in_cliente':in_cliente,
#         'enviado':enviado,
#         'reg_porventa':reg_porventa
#     }
#     return render(request, "Clientes/formulario_insertar_cliente.html", context)

# def ver_cliente(request, id):
#     cliente_list = Clientes.objects.get(persona__id=id)
#     context = {
#         'clie': cliente_list
#     }
#     return render(request, "Clientes/cliente.html", context)

# def editar_cliente(request, id):
#     enviado = False
#     codformpago=""
#     persona_put = Persona.objects.get(id=id)
#     cliente_put = Clientes.objects.get(persona__id=id)
#     if request.method == 'POST':
#         in_cliente_per = AgregarPersona(request.POST, instance=persona_put)
#         in_cliente = ClienteClienteInsertar(request.POST, instance=cliente_put)
#         if in_cliente_per.is_valid() and in_cliente.is_valid():
#             in_cliente_per.save()
#             buscar_ultima_persona = Persona.objects.last()
#             ultima_persona = buscar_ultima_persona.id
#             #Se extrae la data como string del formulario
#             codformpago = in_cliente.data.get("codformapago")  
#             print(codformpago)
#             print(type(codformpago))    
#             cliente = Clientes()
#             cliente.persona_id = int(ultima_persona)
#             cliente.codformapago_id = int(codformpago)
#             cliente.save()
#             return redirect('clie')
#     else:
#         in_cliente_per= AgregarPersona(instance=persona_put)
#         in_cliente=ClienteClienteInsertar(instance=cliente_put)
#         if 'enviado' in request.GET:
#             enviado = True
#     context = {
#         'cliente_put':cliente_put,
#         'in_cliente_per':in_cliente_per,
#         'in_cliente':in_cliente,
#         'enviado':enviado, 
#     }    
#     return render(request, "Clientes/formulario_insertar_cliente.html", context)

# def eliminar_cliente(request, id):
#     enviado=False
#     del_cliente = Clientes.objects.filter(persona__id=id)
#     del_persona = Persona.objects.filter(id=id)
#     red = request.POST.get('clie','/erp/clie/')
#     if request.method =="POST":
#         del_cliente.delete()
#         del_persona.delete()
#         return HttpResponseRedirect(red)
#     context = {
#         'enviado':enviado
#     }
#     return render(request, "Clientes/delete_cliente.html", context)
        

#ARTICULOS

# def articulos(request):
#     articulos_list = Articulos.objects.all()
#     busquedaform = ArticuloBusqueda()
#     context ={
#         'articulos_list': articulos_list,
#         'busquedaform': busquedaform
#     }

#     if request.method == 'POST':
#         busquedaform = ArticuloBusqueda(request.POST)
#         if busquedaform.is_valid():
#             data = Articulos.objects.all()
#             data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
#             data = data.filter(referencia=busquedaform.cleaned_data['referencia'])  if busquedaform.cleaned_data['referencia'] else data
#             data = data.filter(familia=busquedaform.cleaned_data['familia'])  if busquedaform.cleaned_data['familia'] else data
#             data = data.filter(descripcion=busquedaform.cleaned_data['descripcion'])  if busquedaform.cleaned_data['descripcion'] else data
#             data = data.filter(proveedor_id=busquedaform.cleaned_data['proveedor'])  if busquedaform.cleaned_data['proveedor'] else data
#             data = data.filter(ubicacion=busquedaform.cleaned_data['ubicacion'])  if busquedaform.cleaned_data['ubicacion'] else data
#             context['articulos_list']=data
#             context['busquedaform']=busquedaform
#     else:
#         busquedaform = ArticuloBusqueda()

#     return render(request, "Articulos/estructura_crud_art.html",context)

# def agregar_articulo(request):
#     enviado = False
#     if request.method == 'POST':
#         in_articulo_per = AgregarArticulo(request.POST,request.FILES)
#         if in_articulo_per.is_valid():
            
#             in_articulo_per.save()
#             return HttpResponseRedirect('agregarart?enviado=True')
#     else:
#         in_articulo_per= AgregarArticulo()
#         if 'enviado' in request.GET:
#             enviado = True
#     context = {
#         'in_articulo_per':in_articulo_per,
#         'enviado':enviado, 
#         'img_obj': in_articulo_per.instance,
#     }
#     return render(request, "Articulos/formulario_insertar_articulo.html", context)

# def ver_articulo(request,id):
#     articulo_list = Articulos.objects.get(id=id)
#     context = {
#         'art': articulo_list
#     }
#     return render(request, "Articulos/articulo.html", context)

# def editar_articulo(request, id):
#     articulo_put = Articulos.objects.get(id=id)
#     in_articulo_per = AgregarArticulo(request.POST or None, instance=articulo_put)
#     if in_articulo_per.is_valid():
#             in_articulo_per.save()       
#             return redirect('art')
#     context = {
#         'in_articulo_per':in_articulo_per,
#     }    
#     return render(request, "Articulos/formulario_insertar_articulo.html", context)

# def eliminar_articulo(request,id):
#     enviado = False
#     del_articulo = Articulos.objects.filter(id=id)
#     red = request.POST.get('art','/erp/art/')
#     if request.method =="POST":
#         del_articulo.delete()
#         return HttpResponseRedirect(red)
#     context = {
#         'enviado':enviado
#     }
#     return render(request, "Articulos/delete_articulo.html", context)


#FAMILIAS, CATEGORIAS

# def familias(request):
#     familias_list = Familia.objects.all()
#     busquedaform = FamiliaBusqueda()
#     context ={
#         'familias_list': familias_list,
#         'busquedaform': busquedaform
#     }
#     if request.method == 'POST':
#         busquedaform = FamiliaBusqueda(request.POST)
#         if busquedaform.is_valid():
            
#             data = Familia.objects.all()
#             data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
#             data = data.filter(nombre=busquedaform.cleaned_data['nombre'])  if busquedaform.cleaned_data['nombre'] else data
#             context['familias_list']=data
#             context['busquedaform']=busquedaform
#     else:
#         busquedaform = FamiliaBusqueda()
#     return render(request, "Familias/estructura_crud_fam.html",context)


# def agregar_familia(request):
#     enviado = False
#     if request.method == 'POST':
#         in_familia_per = AgregarFamilia(request.POST)
#         if in_familia_per.is_valid():
#             in_familia_per.save()
#             return HttpResponseRedirect('agregarfam?enviado=True')
#     else:
#         in_familia_per= AgregarFamilia()
#         if 'enviado' in request.GET:
#             enviado = True
#     context = {
#         'in_familia_per':in_familia_per,
#         'enviado':enviado, 
#     }
#     return render(request, "Familias/formulario_insertar_familia.html", context)

# def ver_familia(request, id):
#     familia_list = Familia.objects.get(id=id)
#     context = {
#         'fam': familia_list
#     }
#     return render(request, "Familias/familia.html", context)

# def editar_familia(request, id):
#     familia_put = Familia.objects.get(id=id)
#     in_familia_per = AgregarFamilia(request.POST or None, instance=familia_put)
#     if in_familia_per.is_valid():
#             in_familia_per.save()       
#             return redirect('fam')
    
#     context = {
#         'in_familia_per':in_familia_per,
#     }    
#     return render(request, "Familias/formulario_insertar_familia.html", context)

# def eliminar_familia(request,id):
#     enviado = False
#     del_familia = Familia.objects.filter(id=id)
#     red = request.POST.get('fam','/erp/fam/')
#     if request.method =="POST":
#         del_familia.delete()
#         return HttpResponseRedirect(red)
#     context = {
#         'enviado':enviado
#     }
#     return render(request, "Familias/delete_familia.html", context)

# def suma_importes(context):
#     art_fac = Factura_linea_clie.objects.filter(factura_cliente_id = Factura_clie.objects.last().pk)
#     suma_importes = 0
#     for i in art_fac:
#         suma_importes += i.importe
#     factura_last = Factura.objects.last()
#     total_iva = suma_importes * (factura_last.iva/100) 
#     total_fac = suma_importes + total_iva
#     context['articulo_factura'] = art_fac
#     context['suma_importe'] = suma_importes
#     context['total_fac'] = total_fac


# #VENTAS CLIENTES
# def reg_venta(request):
#     nueva_factura_form = NuevaFactura()
#     iva_factura = 8
#     context = {
#         'nueva_factura_form': nueva_factura_form,
#         'iva_factura':iva_factura,
#         'suma_importe':0,
#         'total_fac':0
#     }
#     #Buequeda de persona
#     if 'dni_cliente' in request.GET:
#         cod = request.GET['dni_cliente']
#         if  cod != '':
#             cliente = Clientes.objects.filter(persona_id__dni=cod)
#             context['dni_cliente'] = cod
#             context['nombre_cliente'] = cliente[0] if cliente else "cliente inexistente"
#     #Registro en tabla factura clie
#     if 'registro_cli_fac' in request.GET:
#         fac_clie = Factura_clie()
#         fac_clie.factura = Factura.objects.last()
#         fac_clie.codcliente = Clientes.objects.filter(persona_id__dni=cod)[0]
#         fac_clie.save()
#     #eliminacion factura linea cliente
#     if 'factura_cliente_id' in request.GET:
#         del_flc = Factura_linea_clie.objects.filter(pk=request.GET['factura_cliente_id'])
#         print('==========================',del_flc)
#         if del_flc != []:
#             del_flc.delete()
#             suma_importes(context)
#         # context['articulo_factura'] = Factura_linea_clie.objects.filter(factura_cliente_id = Factura_clie.objects.last().pk)
        

#     if request.method == 'POST':
#         nueva_factura = NuevaFactura(request.POST)
#         validfac_cliente_list_form = request.POST.get("validfac_cliente_list_form", None)
#         validfac_finalform = request.POST.get("validfac_finalform", None)

#         # Crea Factura
#         if nueva_factura.is_valid():
#             nueva_factura.save()
#             print('CREO FACTURA')
#             context['nueva_factura_form'] = nueva_factura
#             context['iva_factura'] = nueva_factura.cleaned_data['iva']
#             return render(request, "VentaClientes/registroventa.html", context)
        
#         # fac_cliente_list_form
#         if validfac_cliente_list_form:
#             nomarticulo = request.POST["nomarticulo"] 
#             articulo_data = Articulos.objects.get(referencia=nomarticulo)
#             fac_clie_last = Factura_clie.objects.last()
#             fac_clie_last_id = fac_clie_last.factura.id
#             factura_linea_clie = Factura_linea_clie()
#             factura_linea_clie.factura_cliente = Factura_clie.objects.last()
#             factura_linea_clie.codproducto = Articulos.objects.get(referencia=nomarticulo)
#             factura_linea_clie.precio = articulo_data.precio_compra
#             cantidad = request.POST["cantidad_art"]
#             factura_linea_clie.cantidad = cantidad
#             descuento = request.POST["descuento_art"]
#             factura_linea_clie.dsctoproducto = descuento
#             factura_linea_clie.importe = (articulo_data.precio_compra * int(cantidad)) - float(descuento)
#             factura_linea_clie.save()    
#             suma_importes(context)

#         #Modifica Factura
#         if validfac_finalform:
#             factura_put = Factura.objects.last()
#             factura_put.totalfactura = request.POST["total_fac"]
#             factura_put.save()
#             fac_clie_last = Factura_clie.objects.last()
#             fac_clie_last_id = fac_clie_last.factura.id
#             art_fac = Factura_linea_clie.objects.filter(factura_cliente_id = fac_clie_last_id)
#             context['articulo_factura'] = art_fac
        
#     return render(request, "VentaClientes/registroventa.html", context)


# ALBANARES
def albanar(request):
    return 

# FACTURA ALBANARES
def fac_albanar(request):
    return 
#UBICACIONES
# def ubicaciones(request):
#     ubicaciones_list = Ubicaciones.objects.all()
#     busquedaform = UbicacionesBusqueda()
#     context ={
#         'ubicaciones_list': ubicaciones_list,
#         'busquedaform': busquedaform
#     }
#     if request.method == 'POST':
#         busquedaform = UbicacionesBusqueda(request.POST)
#         if busquedaform.is_valid():
#             data = Ubicaciones.objects.all()
#             data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
#             data = data.filter(nombre=busquedaform.cleaned_data['nombre'])  if busquedaform.cleaned_data['nombre'] else data
#             context['ubicaciones_list']=data
#             context['busquedaform']=busquedaform
#     else:
#         busquedaform = UbicacionesBusqueda()
#     return render(request, "Ubicaciones/estructura_crud_ubi.html",context)

# def agregar_ubicacion(request):
#     enviado = False
#     if request.method == 'POST':
#         in_ubicaciones_per = AgregarUbicaciones(request.POST)
#         if in_ubicaciones_per.is_valid():
#             in_ubicaciones_per.save()
#             return HttpResponseRedirect('agregarubi?enviado=True')
#     else:
#         in_ubicaciones_per= AgregarUbicaciones()
#         if 'enviado' in request.GET:
#             enviado = True
#     context = {
#         'in_ubicaciones_per':in_ubicaciones_per,
#         'enviado':enviado, 
#     }
#     return render(request, "Ubicaciones/formulario_insertar_ubicacion.html", context)

# def ver_ubicacion(request,id):
#     ubicacion_list = Ubicaciones.objects.get(id=id)
#     context = {
#         'ubi': ubicacion_list
#     }
#     return render(request, "Ubicaciones/ubicacion.html", context)

# def editar_ubicacion(request, id):
#     ubicacion_put = Ubicaciones.objects.get(id=id)
#     in_ubicaciones_per = AgregarUbicaciones(request.POST or None, instance=ubicacion_put)
#     if in_ubicaciones_per.is_valid():
#             in_ubicaciones_per.save()       
#             return redirect('ubi')
#     context = {
#         'in_ubicaciones_per':in_ubicaciones_per,
#     }    
#     return render(request, "Ubicaciones/formulario_insertar_ubicacion.html", context)

# def eliminar_ubicacion(request,id):
#     enviado = False
#     del_ubicacion = Ubicaciones.objects.filter(id=id)
#     red = request.POST.get('ubi','/erp/ubi/')
#     if request.method =="POST":
#         del_ubicacion.delete()
#         return HttpResponseRedirect(red)
#     context = {
#         'enviado':enviado
#     }
#     return render(request, "Ubicaciones/delete_ubicacion.html", context)

#EMBALAJES
# def embalajes(request):
#     embalajes_list = Embalajes.objects.all()
#     busquedaform = EmbalajeBusqueda()
#     context ={
#         'embalajes_list': embalajes_list,
#         'busquedaform': busquedaform
#     }
#     if request.method == 'POST':
#         busquedaform = EmbalajeBusqueda(request.POST)
#         if busquedaform.is_valid():
#             data = Embalajes.objects.all()
#             data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
#             data = data.filter(nombre=busquedaform.cleaned_data['nombre'])  if busquedaform.cleaned_data['nombre'] else data
#             context['embalajes_list']=data
#             context['busquedaform']=busquedaform
#     else:
#         busquedaform = EmbalajeBusqueda()
#     return render(request, "Embalajes/estructura_crud_emb.html",context)

# def agregar_embalaje(request):
#     enviado = False
#     if request.method == 'POST':
#         in_embalaje_per = AgregarEmbalaje(request.POST)
#         if in_embalaje_per.is_valid():
#             in_embalaje_per.save()
#             return HttpResponseRedirect('agregaremb?enviado=True')
#     else:
#         in_embalaje_per= AgregarEmbalaje()
#         if 'enviado' in request.GET:
#             enviado = True
#     context = {
#         'in_embalaje_per':in_embalaje_per,
#         'enviado':enviado, 
#     }
#     return render(request, "Embalajes/formulario_insertar_embalaje.html", context)

# def ver_embalaje(request,id):
#     embalaje_list = Embalajes.objects.get(id=id)
#     context = {
#         'emb': embalaje_list
#     }
#     return render(request, "Embalajes/embalaje.html", context)

# def editar_embalaje(request, id):  
#     embalaje_put = Embalajes.objects.get(id=id)
#     in_embalaje_per = AgregarEmbalaje(request.POST or None, instance=embalaje_put)
#     if in_embalaje_per.is_valid():
#             in_embalaje_per.save()       
#             return redirect('emb')
    
#     context = {
#         'in_embalaje_per':in_embalaje_per,
#     }    
#     return render(request, "Embalajes/formulario_insertar_embalaje.html", context)

# def eliminar_embalaje(request,id):
#     enviado = False
#     del_embalaje = Embalajes.objects.filter(id=id)
#     red = request.POST.get('emb','/erp/emb/')
#     if request.method =="POST":
#         del_embalaje.delete()
#         return HttpResponseRedirect(red)
#     context = {
#         'enviado':enviado
#     }
#     return render(request, "Embalajes/delete_embalaje.html", context)

#ENTIDAD
# def entidad(request):
#     entidades_list = Entidades.objects.all()
#     busquedaform = EntidadBusqueda()
#     context ={
#         'entidades_list': entidades_list,
#         'busquedaform': busquedaform
#     }
#     if request.method == 'POST':
#         busquedaform = EntidadBusqueda(request.POST)
#         if busquedaform.is_valid():
#             data = Entidades.objects.all()
#             data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
#             data = data.filter(nombreentidad=busquedaform.cleaned_data['nombreentidad'])  if busquedaform.cleaned_data['nombreentidad'] else data
#             context['entidades_list']=data
#             context['busquedaform']=busquedaform
#     else:
#         busquedaform = EntidadBusqueda()
#     return render(request, "Entidades/estructura_crud_ent.html",context)

# def agregar_entidad(request):
#     enviado = False
#     if request.method == 'POST':
#         in_entidades_per = AgregarEntidad(request.POST)
#         if in_entidades_per.is_valid():
#             in_entidades_per.save()
#             return HttpResponseRedirect('agregarent?enviado=True')
#     else:
#         in_entidades_per= AgregarEntidad()
#         if 'enviado' in request.GET:
#             enviado = True
#     context = {
#         'in_entidades_per':in_entidades_per,
#         'enviado':enviado, 
#     }
#     return render(request, "Entidades/formulario_insertar_entidad.html", context)

# def editar_entidad(request, id):
#     entidad_put = Entidades.objects.get(id=id)
#     in_entidades_per = AgregarEntidad(request.POST or None, instance=entidad_put)
#     if in_entidades_per.is_valid():
#             in_entidades_per.save()       
#             return redirect('ent')
    
#     context = {
#         'in_entidades_per':in_entidades_per,
#     }    
#     return render(request, "Entidades/formulario_insertar_entidad.html", context)

# def ver_entidad(request,id):
#     entidad_list = Entidades.objects.get(id=id)
#     context = {
#         'ent': entidad_list
#     }
#     return render(request, "Entidades/entidad.html", context)
    
# def eliminar_entidad(request,id):
#     enviado = False
#     del_entidad = Entidades.objects.filter(id=id)
#     red = request.POST.get('ent','/erp/ent/')
#     if request.method =="POST":
#         del_entidad.delete()
#         return HttpResponseRedirect(red)
#     context = {
#         'enviado':enviado
#     }
#     return render(request, "Entidades/delete_entidad.html", context)
    
# FORMAS DE PAGO
# def formas_de_pago(request):
#     formas_de_pago_list = Formapago.objects.all()
#     busquedaform = FormasPagoBusqueda()
    
#     context = {
#         'formas_de_pago_list':formas_de_pago_list,
#         'busquedaform':busquedaform
#     }

#     if request.method == 'POST':
#         busquedaform = FormasPagoBusqueda(request.POST)
#         if busquedaform.is_valid():
#             data = Formapago.objects.all()
#             data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
#             data = data.filter(nombre=busquedaform.cleaned_data['fpago'])  if busquedaform.cleaned_data['fpago'] else data
#             context['formas_de_pago_list']=data
#             context['busquedaform']=busquedaform
#     else:
#         busquedaform = FamiliaBusqueda()

#     return render(request, "FormasPago/estructura_crud_forpag.html", context)

# def agregar_fpago(request):
#     enviado = False
#     if request.method == 'POST':
#         in_fpago_per = AgregarFormaPago(request.POST)
#         if in_fpago_per.is_valid():
#             in_fpago_per.save()
#             return HttpResponseRedirect('agregarformapago?enviado=True')

#     else:
#         in_fpago_per = AgregarFormaPago()
#         if 'enviado' in request.GET:
#             enviado = True

#     context = {
#         'in_fpago_per':in_fpago_per,
#         'enviado':enviado, 
#     }
#     return render(request, "FormasPago/formulario_insertar_formapago.html", context)

# def ver_fpago(request, id):
#     fpago_list = Formapago.objects.get(id=id)
#     context = {
#         'fpago_list': fpago_list
#     }
#     return render(request, "FormasPago/formapago.html", context)

# def editar_fpago(request, id):
#     fpago_put = Formapago.objects.get(id=id)
#     in_fpago_per = AgregarFormaPago(request.POST or None, instance=fpago_put)
#     if in_fpago_per.is_valid():
#             in_fpago_per.save()       
#             return redirect('fpago')
    
#     context = {
#         'in_fpago_per':in_fpago_per,
#     }    
#     return render(request, "FormasPago/formulario_insertar_formapago.html", context)

# def eliminar_fpago(request, id):
#     enviado = False
#     del_fpago = Formapago.objects.filter(id=id)
#     red = request.POST.get('fpago','/erp/formapago/')

#     if request.method =="POST":
#         del_fpago.delete()
#         return HttpResponseRedirect(red)

#     context = {
#         'enviado':enviado
#     }
#     return render(request, "FormasPago/delete_formapago.html", context)

# IMPUESTOS
# def impuestos(request):
#     impuestos_list = Impuestos.objects.all()
#     busquedaform = ImpuestoBusqueda()

#     context = {
#         'impuestos_list':impuestos_list,
#         'busquedaform':busquedaform
#     }

#     if request.method == 'POST':
#         busquedaform = ImpuestoBusqueda(request.POST)
#         if busquedaform.is_valid():
#             data = Impuestos.objects.all()
#             data = data.filter(pk=busquedaform.cleaned_data['codigo'])  if busquedaform.cleaned_data['codigo'] else data
#             data = data.filter(nombre=busquedaform.cleaned_data['nombre'])  if busquedaform.cleaned_data['nombre'] else data
#             data = data.filter(nombre=busquedaform.cleaned_data['valor'])  if busquedaform.cleaned_data['valor'] else data
#             context['impuestos_list']=data
#             context['busquedaform']=busquedaform
#     else:
#         busquedaform = FamiliaBusqueda()

#     return render(request, "Impuestos/estructura_crud_imp.html", context) 

# def agregar_impuesto(request):
#     enviado = False
#     if request.method == 'POST':
#         in_imp_per = AgregarImpuesto(request.POST)
#         if in_imp_per.is_valid():
#             in_imp_per.save()
#             return HttpResponseRedirect('agregarimpuesto?enviado=True')
#     else:
#         in_imp_per = AgregarImpuesto()
#         if 'enviado' in request.GET:
#             enviado = True
#     context = {
#         'in_imp_per':in_imp_per,
#         'enviado':enviado, 
#     }
#     return render(request, "Impuestos/formulario_insertar_impuesto.html", context)

# def editar_impuesto(request, id):
#     imp_put = Impuestos.objects.get(id=id)
#     in_imp_per = AgregarImpuesto(request.POST or None, instance=imp_put)
#     if in_imp_per.is_valid():
#             in_imp_per.save()       
#             return redirect('imp')
#     context = {
#         'in_imp_per':in_imp_per,
#     }    
#     return render(request, "Impuestos/formulario_insertar_impuesto.html", context)

# def ver_impuesto(request, id):
#     imp_list = Impuestos.objects.get(id=id)
#     context = {
#         'imp_list': imp_list
#     }
#     return render(request, "Impuestos/impuesto.html", context)

# def eliminar_impuesto(request, id):
#     enviado = False
#     del_imp = Impuestos.objects.filter(id=id)
#     red = request.POST.get('imp','/erp/impuestos/')

#     if request.method =="POST":
#         del_imp.delete()
#         return HttpResponseRedirect(red)
#     context = {
#         'enviado':enviado
#     }
#     return render(request, "Impuestos/delete_impuesto.html", context)