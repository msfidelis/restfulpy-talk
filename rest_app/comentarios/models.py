from django.db import models
 
class Comentario(models.Model):
	titulo = models.CharField("Titulo", max_length=255)
	comentario = models.TextField("Comentario")

##
# Model de Postagem
##
class Post(models.Model):
	user = models.CharField("Usuario", max_length=100)
	conteudo = models.CharField("Conteudo", max_length=140)