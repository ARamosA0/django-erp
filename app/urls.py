from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns =[
    # Pagina Principal
    path('', TemplateView.as_view(template_name="Inicio/inicio.html")),
    #Pag Provedores
    path('prov/', proveedores, name="prov")
    #Pag Insertar Proveedores
    path('insertarproveedor', views.insertar_proveedor)
]