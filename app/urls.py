from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns =[
    path('', TemplateView.as_view(template_name="Inicio/inicio.html")),
    # path('crud/', CrudList.as_view()),
    # path('busqueda/', Busqueda.as_view()),
    # path('proveedores/', Proveedores.as_view())
    path('prov/', proveedores, name="prov")
    # path('proveedor/', views.form_busqueda, name="form_busqueda"),
    # path('insertarproveedor', views.insertar_proveedor)
]