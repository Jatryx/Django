from django.db import models

# Create your models here.
class Contenido(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, null=True, verbose_name="apellido")
    email = models.EmailField(null=True, verbose_name="email")
    telefono = models.IntegerField(null=True, verbose_name="telefono")

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + "Apellido: " + self.apellido
        return fila