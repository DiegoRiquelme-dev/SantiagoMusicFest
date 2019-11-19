from django.db import models


# Create your models here.


class Artista(models.Model):
    
    nombre = models.CharField(max_length=200)
    generoMusical= models.CharField(max_length=200)
    stage = models.CharField(max_length=200)
    



