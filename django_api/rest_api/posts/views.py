# -*- coding: UTF-8 -*-

from posts.models import Post
from posts.serializers import PostSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework import mixins
from rest_framework import generics

##
# Listagem e criação de Post[
# HTTP Verbs:
# @get - Retorna toda a lista de postagens
# @post - Cria uma nova postagem
##
class PostList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    ##
    # Retorna uma lista de postagens existentes
    # curl -H 'Accept: application/json; indent=2' -X get http://localhost:8000/posts/
    ##
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    ##
    # Cria um novo post nop banco de dados e retorna o mesmo
    # curl -H 'Accept: application/json; indent=2' --data "conteudo=Novo Conteúdo" --data "user=@fidelissauro" -X POST http://localhost:8000/posts/
    # contet = text
    # user = text
    ##
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

##
# Detail do Post
# HTTP Verbs:
# @get /id - Pega informações de um post em específico
# @put /id - Atualiza as informações de um registro
# @delete /id - Deleta um registro informado 
##
class PostDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    
    ##
    # Pega as informacoes um registro
    # curl -H 'Accept: application/json; indent=2' -X GET http://localhost:8000/posts/1/
    ##
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    ##
    # Altera as informacoes de um registro em especifico
    # curl -H 'Accept: application/json; indent=2' --data "id=1" --data "conteudo=Conteúdo Alterado" --data "user=@fidelissauro" -X PUT http://localhost:8000/posts/1/
    ##
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
 
    ##
    # Deleta um registro infomado pelo ID
    # curl -H 'Accept: application/json; indent=2' -X DELETE http://localhost:8000/posts/1/
    ##
    def delete(self, request, pk=None):
        return self.destroy(self, request, pk=None)