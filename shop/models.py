from django.db import models

# Create your models here.
class Employee(models.Model):
    nombre= models.CharField(max_length=50)
    precio= models.PositiveIntegerField()
    stock= models.PositiveSmallIntegerField()
    fecha_ingreso=models.DateField()
    oferta=models.BooleanField()
    descripcion=models.TextField(blank=True)

    def __str__(self) -> str:
        return self.nombre