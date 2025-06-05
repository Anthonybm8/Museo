from django.db import models
from Aplicaciones.Obra.models import Obra

# Create your models here.
class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    obra = models.ManyToManyField(Obra, blank=True)
    foto = models.ImageField(upload_to='artistas', null=True, blank=True)
    biografia = models.FileField(upload_to='artistas', null=True, blank=True)