from django.db import models

# Create your models here.
    class Artista(models.Model): 
    generoMusica = models.CharField(max_length=200)
    tematica= models.CharField(max_length=200)
    auspisiador = models.CharField(max_length=200)
    