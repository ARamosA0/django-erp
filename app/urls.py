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
    #Insertar Cliente
   
    #Pag Familias
    path('fam/', familias, name="fam"),
<<<<<<< HEAD
    #Editar Cliente
    path('fam/editar/<int:id>/', editar_familia, name="edfam"),
    #Insertar familia
    path('fam/agregarfam', agregar_familia, name="afam")
=======
    #Insertar Familia
    path('fam/agregarfam', agregar_familia, name="afam"),
    #Eliminar Familia
    path('fam/eliminar/<int:id>/', eliminar_familia, name="delfam"),
    #Editar Familia
    path('fam/editar/<int:id>/', editar_familia, name="edfam"),
    #Ver Familia
    path('fam/ver/<int:id>/', ver_familia, name="verfam"),
>>>>>>> 19a757544ede77e1315bc8be1d1775c006aff636
]
