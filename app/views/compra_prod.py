from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *

#VENTAS CLIENTES
def compra(request):
   
    #Buequeda de persona
   
    #Registro en tabla factura clie
    
    #eliminacion factura linea cliente
   
        # context['articulo_factura'] = Factura_linea_clie.objects.filter(factura_cliente_id = Factura_clie.objects.last().pk)
        

        # Crea Factura
       
        
       

        #Modifica Factura
        
        
    return render(request, "CompraProductos/compraproductos.html")