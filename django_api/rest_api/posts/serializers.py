# -*- coding: UTF-8 -*-

from rest_framework import serializers
from posts.models import Post
 
##
# Serializer do model Post
# Aqui são definidos todos os campos que vão ser acessíveis ao usuário
##
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'conteudo')
        
