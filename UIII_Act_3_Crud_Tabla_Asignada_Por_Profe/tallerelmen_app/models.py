
from django.db import models

# Create your models here.

class Producto(models.Model):
    Id_Producto=models.CharField(primary_key=True,max_length=6)
    Precio=models.CharField(max_length=100)
    Marca=models.CharField(max_length=100)
    Calidad=models.CharField(max_length=100)
    Recibido=models.CharField(max_length=100)
    Proovedor=models.CharField(max_length=100)
    Cantidad=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Marca
