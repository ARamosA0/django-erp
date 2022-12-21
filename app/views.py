from django.shortcuts import render

# Create your views here.
def buscar_proveedor(request):
    return render(request, 'formulario_busqueda.html')