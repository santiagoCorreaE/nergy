from django.db import models

# Create your models here.

"""
nombre = models.CharField(max_length=50)


"""

class Variable(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class Tipo_nodo(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Tipo_ubicacion(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Tipo_sensor(models.Model):
    nombre = models.CharField(max_length=50)
    referencia = models.CharField(max_length=50)
    variable = models.ForeignKey(Variable)

    def __str__(self):
        return self.nombre

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=50)
    tipo_ubicacion = models.ForeignKey(Tipo_ubicacion)
    
    def __str__(self):
        return self.nombre

class Nodo(models.Model):
    ubicacion = models.ForeignKey(Ubicacion)
    tipo_nodo = models.ForeignKey(Tipo_nodo)
    nombre = models.CharField(max_length=50)
    ciclo = models.PositiveSmallIntegerField()
    en_campo = models.BooleanField()
    
    def __str__(self):
        return self.nombre

class Sensor(models.Model):
    nodo = models.ForeignKey(Nodo)
    tipo_sensor = models.ForeignKey(Tipo_sensor)
    posicion = models.PositiveSmallIntegerField()
    fecha_instalacion = models.DateTimeField()
    on = models.BooleanField()
    
    def __str__(self):
        return self.tipo_sensor.nombre

class Lectura(models.Model):
    sensor = models.ForeignKey(Sensor)
    valor = models.DecimalField(max_digits=8, decimal_places=3)
    fecha = models.DateTimeField()
    
    def __str__(self):
        return str(self.valor)
