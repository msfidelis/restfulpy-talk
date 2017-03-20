from django.db import models
 
class Comentario(models.Model):
	titulo = models.CharField("Titulo", max_length=255)
	comentario = models.TextField("Comentario")