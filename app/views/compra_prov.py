from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

def compra_prov(request):
    
    context = {

    }

    return render(request, "CompraProv/compraprov_crud.html", context)