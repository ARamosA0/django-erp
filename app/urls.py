from django.urls import path

from . import views

urlpatterns =[
    path('crud/', views.crud, name='crud'),
    path('', views.index, name='index'),
    path('proveedor/', views.form_busqueda, name="form_busqueda"),
    path('insertarproveedor', views.insertar_proveedor),
    path('findtest/',views.find_test),
]