from django.urls import path

from . import views

urlpatterns =[
    path('', views.crud, name='crud'),
    path('principal/', views.index, name='index')
]