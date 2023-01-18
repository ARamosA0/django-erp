from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *
from datetime import datetime


def caja_diaria(request):
    formbusqueda = DateFormSearch()
    formnuevacaja = NuevaCaja()
    tipo_pago = Formapago.objects.all()
    context = {
        'formbusqueda':formbusqueda,
        'tipo_pago':tipo_pago,
        'formnuevacaja':formnuevacaja
    }
    if formbusqueda.is_valid():
            data = Caja_diaria.objects.filter(borrado='0')
            data = data.filter(pk=formbusqueda.cleaned_data['fechabusqueda'])  if formbusqueda.cleaned_data['fechabusqueda'] else data
            context['clientes_list']=data
            context['formbusqueda']=formbusqueda
    else:
        formbusqueda = DateFormSearch()

    return render(request, 'CajaDiaria/caja_diaria.html', context)