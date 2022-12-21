from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def crud(request):
    
    return render(request, 'estructura_crud.html')


def Busqueda(request, response):
    if(request.GET["prd"]):
        return render(request, 'estructura_crud.html') 
    return Httpresponse     