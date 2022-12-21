from django.urls import path

from . import views

urlpatterns =[
    path('proveedores/buscar_proveedor', views.buscar_proveedor, name='buscar_proveedor')
]