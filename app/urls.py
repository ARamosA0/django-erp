from django.urls import path

from . import views

urlpatterns =[
    path('', views.crud, name='crud'),
    path('insertarproveedor', views.insertar_proveedor)
]