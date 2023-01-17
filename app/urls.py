from django.urls import path
from django.views.generic import TemplateView
from app.views.articulos import *
from app.views.clientes import *
from app.views.embalajes import *
from app.views.entidad import *
from app.views.familias import *
from app.views.formas_pago import *
from app.views.impuestos import *
from app.views.proveedores import *
from app.views.ubicaciones import *
from app.views.provincia import *
from app.views.ventas_clie import *
from app.views.factura_clie import *
from app.views.compra_prov import *
from app.views.remisiones import *

urlpatterns =[
    # Pagina Principal
    path('', TemplateView.as_view(template_name="Inicio/inicio.html"), name="inicio"),
    
    #Pag Provedores
    path('prov/', proveedores, name="prov"),
    path('prov/agregarprov', agregar_proveedor, name="aprov"),
    path('prov/eliminar/<int:id>', eliminar_proveedor, name="delprov"),
    path('prov/ver/<int:id>', ver_proveedor, name="verprov"),
    path('prov/editar/<int:id>', editar_proveedor, name="edprov"),
    
    
    #Pag Clientes
    path('clie/', clientes, name="clie"),
    #Insertar Cliente
    path('clie/agregarclie', agregar_cliente, name="aclie"),
    #Eliminar Cliente
    path('clie/eliminar/<int:id>/', eliminar_cliente, name="delclie"),
    #Editar Cliente
    path('clie/editar/<int:id>/', editar_cliente, name="edclie"),
    #Ver Cliente
    path('clie/ver/<int:id>/', ver_cliente, name="verclie"),


    #Pag Articulos
    path('art/', articulos, name="art"),
    #Insertar Articulo
    path('art/agregarart', agregar_articulo, name="aart"),
    #Eliminar Articulo
    path('art/eliminar/<int:id>/', eliminar_articulo, name="delart"),
    #Editar Articulo
    path('art/editar/<int:id>/', editar_articulo, name="edart"),
    #Ver Articulo
    path('art/ver/<int:id>/', ver_articulo, name="verart"),


    #Pag Familias
    path('fam/', familias, name="fam"),
    #Insertar Familia
    path('fam/agregarfam', agregar_familia, name="afam"),
    #Eliminar Familia
    path('fam/eliminar/<int:id>/', eliminar_familia, name="delfam"),
    #Editar Familia
    path('fam/editar/<int:id>/', editar_familia, name="edfam"),
    #Ver Familia
    path('fam/ver/<int:id>/', ver_familia, name="verfam"),


   
   
    #Pag Ubicaciones
    path('ubi/', ubicaciones, name="ubi"),
    #Insertar Ubicacion
    path('ubi/agregarubi', agregar_ubicacion, name="aubi"),
    #Eliminar Ubicacion
    path('ubi/eliminar/<int:id>/', eliminar_ubicacion, name="delubi"),
    #Editar Ubicacion
    path('ubi/editar/<int:id>/', editar_ubicacion, name="edubi"),
    #Ver Ubicacion
    path('ubi/ver/<int:id>/', ver_ubicacion, name="verubi"),


    #Pag Embalajes
    path('emb/', embalajes, name="emb"),
    #Insertar Embalaje
    path('emb/agregaremb', agregar_embalaje, name="aemb"),
    #Eliminar Embalaje
    path('emb/eliminar/<int:id>/', eliminar_embalaje, name="delemb"),
    #Editar Embalaje
    path('emb/editar/<int:id>/', editar_embalaje, name="edemb"),
    #Ver Embalaje
    path('emb/ver/<int:id>/', ver_embalaje, name="veremb"),


    #Pag Entidades
    path('ent/', entidad, name="ent"),
    #Insertar Entidad
    path('ent/agregarent', agregar_entidad, name="aent"),
    #Eliminar Entidad
    path('ent/eliminar/<int:id>/', eliminar_entidad, name="delent"),
    #Editar Entidad
    path('ent/editar/<int:id>/', editar_entidad, name="edent"),
    #Ver Entidad
    path('ent/ver/<int:id>/', ver_entidad, name="verent"),
    
    #Pag Formas de pago
    path('formapago/', formas_de_pago, name="fpago"),
    path('formapago/ver/<int:id>', ver_fpago, name="verfpago"),
    path('formapago/agregarformapago', agregar_fpago, name="afpago"),
    path('formapago/editar/<int:id>', editar_fpago, name="edfpago"),
    path('formapago/eliminar/<int:id>', eliminar_fpago, name="delfpago"),
    
    #Pag Impuestos
    path('impuestos/', impuestos, name="imp"),
    path('impuestos/agregarimpuesto', agregar_impuesto, name="aimp"),
    path('impuestos/ver/<int:id>', ver_impuesto, name="verimp"),
    path('impuestos/editar/<int:id>', editar_impuesto, name="edimp"),
    path('impuestos/eliminar/<int:id>', eliminar_impuesto, name="delimp"),

    #Pag Provincias
    path('provi/', provincia, name="provi"),
    path('provi/agregarprovi', agregar_provincia, name="aprov"),
    #Eliminar Provincia
    path('provi/eliminar/<int:id>/', eliminar_provincia, name="delprovi"),
    #Editar Provincia
    path('provi/editar/<int:id>/', editar_provincia, name="edprovi"),
    #Ver Provincia
    path('provi/ver/<int:id>/', ver_provincia, name="verprovi"),

    #Venta
    path('venta', reg_venta, name="venta"),

    #Factura Cliente
    path('facturaclie/', factura, name='facturaclie'),
    path('facturaclie/ver/<int:id>', ver_factura, name="verfacturaclie"),
    path('facturaclie/eliminar/referenciaarticulo/<int:id>', ver_factura_eliminar_articulo, name="eliminarartref"),
    path('facturaclie/editar/<int:id>', editar_factura, name="edfacturaclie"),
    path('facturaclie/eliminar/<int:id>', eliminar_factura, name="delfacturaclie"),


    #Pag Remision
    path('rem/', remisiones, name="rem"),
    #Insertar Remision
    path('rem/agregarrem/<int:id>/', agregar_remision, name="arem"),
    #Eliminar Remision
    path('rem/eliminar/<int:id>/', eliminar_remision, name="delrem"),
    #Editar Remision
    path('rem/editar/<int:id>/', editar_remision, name="edrem"),
    #Ver Remision
    path('rem/ver/<int:id>/', ver_remision, name="verrem"),


    #Compra Proveedor
    path('compra', compra_prov, name="compraprov"),
    #Agregar factura
    path('agregarcom', agregar_compra_prov, name="agcompra" ),
]
