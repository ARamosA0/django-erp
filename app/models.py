from django.db import models

# Create your models here.

class Provincias(models.Model):
    nombreprovincia = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreprovincia

class Formapago(models.Model):
    nombrefp = models.CharField(max_length=100)
    borrado = models.CharField(max_length=1)

    def __str__(self):
        return self.nombrefp

class Entidades(models.Model):
    nombreentidad = models.CharField(max_length=100)
    borrado = models.CharField(max_length=1)

    def __str__(self):
        return self.nombreentidad


class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    nif = models.CharField(max_length=100)
    direccion = models.CharField(max_length=500)
    codprovincia = models.ForeignKey(Provincias, on_delete=models.RESTRICT, default='Null')
    localidad = models.CharField(max_length=100)
    codformapago = models.ForeignKey(Formapago, on_delete=models.RESTRICT, default='Null')
    codentidad = models.ForeignKey(Entidades, on_delete=models.RESTRICT, default='Null')
    cuentabancaria = models.CharField(max_length=100)
    codpostal = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    movil = models.CharField(max_length=100)
    web = models.CharField(max_length=100)
    borrado = models.CharField(max_length=1)

    def __str__(self):
        return self.nombre

class Proveedores(models.Model):
    nombre = models.CharField(max_length=100)
    nif = models.CharField(max_length=100)
    direccion = models.CharField(max_length=500)
    codprovincia = models.ForeignKey(Provincias, on_delete=models.RESTRICT, default='Null')
    localidad = models.CharField(max_length=100)
    codentidad = models.ForeignKey(Entidades, on_delete=models.RESTRICT, default='Null')
    cuentabancaria = models.CharField(max_length=100)
    codpostal = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    movil = models.CharField(max_length=100)
    web = models.CharField(max_length=100)
    borrado = models.CharField(max_length=1)

    def __str__(self):
        return self.nombre


