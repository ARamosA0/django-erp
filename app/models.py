from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Provincias(models.Model):
    nombreprovincia = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreprovincia

class Formapago(models.Model):
    nombrefp = models.CharField(max_length=100)
    borrado = models.CharField(max_length=1, default=0)

    def __str__(self):
        return self.nombrefp

class Entidades(models.Model):
    nombreentidad = models.CharField(max_length=100)
    borrado = models.CharField(max_length=1, default=0)

    def __str__(self):
        return self.nombreentidad

class Familia(models.Model):
    nombre = models.CharField(max_length=100)
    borrado = models.CharField(max_length=1, default=0)

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=100)
    codprovincia = models.ForeignKey(Provincias, on_delete=models.CASCADE)
    localidad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=500)
    codpostal = models.CharField(max_length=100)
    cuentabancaria = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    movil = models.CharField(max_length=100)
    web = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    estructurajuridica = models.CharField(max_length=100)
    ruc = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    codprovincia = models.ForeignKey(Provincias, on_delete=models.CASCADE)
    localidad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=500)
    codpostal = models.CharField(max_length=100)
    cuentabancaria = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    movil = models.CharField(max_length=100)
    web = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Clientes(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, primary_key=True)
    codformapago = models.ForeignKey(Formapago, on_delete=models.CASCADE)
    borrado = models.CharField(max_length=1, default=0)

    def __str__(self):
        return self.persona.nombre

class Proveedores(models.Model):
    # persona = models.OneToOneField(Persona, on_delete=models.CASCADE, primary_key=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)
    borrado = models.CharField(max_length=1, default=0)

    def __str__(self):
        # return self.persona.nombre
        return self.persona, self.empresa

CHOICES = (("1", "1"),
    ("0", "0"))
def upload_path(instance, filename):
    return '/'.join(['articulos',str(instance.referencia),filename])

class Ubicaciones(models.Model):
    nombre = models.CharField(max_length=100)
    borrado = models.CharField(max_length=1, default=0)
    def __str__(self):
        return self.nombre

class Impuestos(models.Model):
    nombre = models.CharField(max_length=100)
    valor = models.FloatField(validators=[MinValueValidator(0.0)])
    borrado = models.CharField(max_length=1, default=0)
    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    referencia = models.CharField(max_length=20)
    familia = models.ForeignKey(Familia,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500)
    impuesto = models.ForeignKey(Impuestos, on_delete=models.CASCADE)
    proveedor_1 = models.OneToOneField(Proveedores,on_delete=models.CASCADE,related_name='proveedor_1')
    proveedor_2 = models.OneToOneField(Proveedores,on_delete=models.CASCADE,related_name='proveedor_2')
    descripcion_corta = models.CharField(max_length=100)
    ubicacion = models.ForeignKey(Ubicaciones, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    stock_minimo = models.PositiveIntegerField()
    aviso_minimo = models.CharField(max_length=1,choices=CHOICES,default="0")
    datos_producto = models.CharField(max_length=500)
    fecha_alta = models.DateTimeField()
    embalaje = models.CharField(max_length=1,choices=CHOICES,default="0")
    unidades_por_caja = models.PositiveIntegerField()
    precio_ticket = models.CharField(max_length=1,choices=CHOICES,default="0")
    modificar_ticker = models.CharField(max_length=1,choices=CHOICES,default="0")
    observaciones = models.CharField(max_length=500)
    precio_compra = models.FloatField(validators=[MinValueValidator(0.0)])
    precio_almacen = models.FloatField(validators=[MinValueValidator(0.0)])
    precio_tienda = models.FloatField(validators=[MinValueValidator(0.0)])
    precio_con_iva = models.FloatField(validators=[MinValueValidator(0.0)])
    imagen = models.ImageField(upload_to=upload_path, null=True)








# class Facturas(models.Model):
#     fecha = models.DateField(auto_now='True')
#     iva = models.IntegerField()
#     codcliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
#     estado = models.CharField(max_length=100)
#     totalfactura = models.FloatField()
#     fechavencimiento = models.DateField(auto_now='True')
#     borrado = models.CharField(max_length=1, default=0)

#     def __str__(self):
#         return self.iva

# class Factura_linea_tmp(models.Model):
#     numlinea = models.IntegerField()
#     codfamilia = models.ForeignKey(Familia, on_delete=models.CASCADE)
#     codigo = models.CharField(max_length=100)
#     cantidad = models.FloatField()
#     precio = models.FloatField()
#     importe = models.FloatField()
#     dcto = models.FloatField()

#     def __str__(self):
#         return self.numlinea

# class Factura_linea(models.Model):
#     numlinea
#     codfamilia
#     codigo
#     cantidad
#     precio
#     importe
#     dcto       
