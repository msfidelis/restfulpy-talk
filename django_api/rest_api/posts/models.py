from django.db import models

##
# Model de Postagem
##
class Post(models.Model):
    user = models.CharField("Usuario", max_length=100)
    conteudo = models.CharField("Conteudo", max_length=140)
