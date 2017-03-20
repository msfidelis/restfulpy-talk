from comentarios.models import Comentario
from comentarios.serializers import ComentarioSerializer
from rest_framework import mixins
from rest_framework import generics

##
# Lista dos comentarios. 
##  
class ComentarioList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    
    ##
    # Pega a lista de todos os comentarios
    # curl -H 'Accept: application/json; indent=2' -X GET http://127.0.0.1:8000/comentarios/
    ##
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    ##
    # Cria um novo comentario via POST
    # curl -H 'Accept: application/json; indent=2' -X POST --data "titulo=teste"  --data "comentario=matheus, seu lindo" http://127.0.0.1:8000/comentarios/ 
    ##
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

##
# Detail dos comentarios
##  
class ComentarioDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    
    ##
    # Pega as informacoes um registro
    # curl -H 'Accept: application/json; indent=2' -X GET http://localhost:8000/comentarios/12/
    ##
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    ##
    # Altera as informacoes de um registro em especifico
    # curl -H 'Accept: application/json; indent=2' --data "id=12" --data "comentario=comentario alterado" --data "titulo=titulo alterado" -X PUT http://localhost:8000/comentarios/12/
    ##
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
 
    ##
    # Deleta um registro infomado pelo ID
    ##
    def delete(self, request, pk=None):
        return self.destroy(self, request, pk=None)