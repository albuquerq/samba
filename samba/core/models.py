from django.db import models
from django.contrib.admin.models import AbstractBaseUser
# Create your models here.

class Usuario(AbstractBaseUser):

	USERNAME_FIELD = 'email'

	nome = models.CharField(max_length=200, required=True)
	sobrenome = models.CharField(max_length=200)
	email = models.EmailField(required=True, unique=True)
	senha = models.PasswordField(required=True)
	is_active = models.BooleanField(default=True)

	REQUIRED_FIELDS = ['nomes', 'email', 'senha']
	
	def get_full_name(self):
		if self.sobrenome:
			return '{} {}'.formart(self.nome, self.sobrenome)
		return self.nome

	def get_short_name(self):
		return self.nome