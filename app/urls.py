from django.urls import path
from django.views.generic import TemplateView
from .views import *
# from . import views

urlpatterns =[
    # Pagina Principal
    path('', TemplateView.as_view(template_name="Inicio/inicio.html"), name="inicio"),
    
    #Pag Provedores
    path('prov/', proveedores, name="prov"),
    # path('prove/', Proveedores.as_view())
    #Pag Insertar Proveedores
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


    #Venta
    path('venta', reg_venta, name="venta"),

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
    path('ent/', entidades, name="ent"),
    #Insertar Entidad
    path('ent/agregarent', agregar_entidad, name="aent"),
    #Eliminar Entidad
    path('ent/eliminar/<int:id>/', eliminar_entidad, name="delent"),
    #Editar Entidad
    path('ent/editar/<int:id>/', editar_entidad, name="edent"),
    #Ver Entidad
    path('ent/ver/<int:id>/', ver_entidad, name="verent"),
]
