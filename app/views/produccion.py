from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *


def produccion(request):
    context = {}
    return render(request, 'Produccion/produccion_crud.html', context)