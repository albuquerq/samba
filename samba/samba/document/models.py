from django.db import models

from geo.models import Municipio
# Create your models here.

class Plano(models.Model):

	ano = models.IntegerField()
	nome = models.CharField(max_length=200)
	municipio = models.ForeignKey(Municipio)
