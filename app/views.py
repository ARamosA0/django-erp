from django.shortcuts import render

# Create your views here.
def crud(response):
    return render(response, 'estructura_crud.html')

def buscar_proveedor(request):
    return render(request, 'formulario_busqueda.html')
