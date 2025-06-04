from django.db import models

# Create your models here.
class Obra(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField()
    foto = models.ImageField(upload_to='obras', null=True, blank=True)
    informacion = models.FileField(upload_to='obras', null=True, blank=True)
