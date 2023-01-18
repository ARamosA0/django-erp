from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *


def caja_diaria(request):
    formbusqueda = DateFormSearch()
    tipo_pago = Formapago.objects.all()
    context = {
        'formbusqueda':formbusqueda,
        'tipo_pago':tipo_pago,
    }
    return render(request, 'CajaDiaria/caja_diaria.html', context)