from django.urls import path

from . import views

urlpatterns =[
    path('', views.crud, name='crud'),
    path('proveedor/', views.form_busqueda, name="form_busqueda")
    path('insertarproveedor', views.insertar_proveedor)
]