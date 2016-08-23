from django.db import models


class UF(models.Model):
	"""
	UF: Unidade da federação, corresponde a um estado do país.
	"""
	nome = models.CharField(max_length=100)
	sigla = models.CharField(max_length=4)
	regiao = models.CharField(max_length=50)

	def __str__(self):
		return self.nome

class Municipio(models.Model):
	"""
	Representa uma cidade.
	"""
	nome = models.CharField(max_length=200)
	cod_ibge = models.IntegerField()
	descricao = models.TextField()
	UF = models.ForeignKey("UF")
	
	#avatar = models.ImageField(upload_to="municipios")

	lat = models.FloatField()
	lng = models.FloatField()
	alt = models.FloatField()

	def __str__(self):
		return self.nome
