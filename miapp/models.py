from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)  
    email = models.EmailField() 

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)  
    email = models.EmailField() 
    profesion = models.CharField(max_length=40)

class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()
#------------------------LO DE ARRIBA FUE PRACTICA-----------------------------------------------------    
class Carta(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    precio_USD = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    class Meta:
        ordering = ["nombre"]
        
    def __str__(self):
        return f"{self.nombre} de tipo {self.tipo}"

class Dibujo(models.Model):
    nombre = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    precio_USD = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return f"{self.nombre} de {self.autor}"

class Figura(models.Model):
    nombre = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    precio_USD = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return f"{self.nombre}"
    
class Camiseta(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    forma = models.CharField(max_length=100)
    precio_USD = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.nombre} manga {self.forma}"    

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")   
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"    

