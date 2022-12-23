from django.db import models

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
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, primary_key=True)
    # persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True, blank=True)
    # empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)
    borrado = models.CharField(max_length=1, default=0)

    def __str__(self):
        return self.persona.nombre
        # return self.persona.nombre, self.empresa.nombre


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