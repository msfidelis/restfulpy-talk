# -*- coding: UTF-8 -*-

from rest_framework import serializers
from comentarios.models import Comentario, Post
 
class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('id', 'titulo', 'comentario')

##
# Serializer do model Post
# Aqui são definidos todos os campos que vão ser acessíveis ao usuário
##
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'conteudo')
        
