from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns =[
    # Pagina Principal
    path('', TemplateView.as_view(template_name="Inicio/inicio.html"), name="inicio"),
    #Pag Provedores
    path('prov/', proveedores, name="prov"),
    # path('prove/', Proveedores.as_view())
    #Pag Insertar Proveedores
    path('prov/insertarproveedor', insertar_proveedor, name="inprov"),
    #Pag Clientes
    path('clie/', clientes, name="clie"),
]
