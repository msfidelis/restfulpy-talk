

# Step - 1: Ambiente

## Criando um Virtualenv

* Instalação do Virtualenv

```
    $ sudo pip install virtualenv
```

* Criando um Virtualenv

```
    $ mkdir rest_django; cd rest_django
    $ virtualenv myvenv
```

* Iniciando o Virtualenv

```
    source ./myvenv/bin/activate
```

## Instalando as dependências

* Instalação do Python 

```
 $ sudo apt-get install python # Debian Like
 $ brew install python # MacOS
```

* Instalação do PIP (Python Package Manager)

O Pip já vem integrado na instalação do Python utilizando o Homebrew do MacOS

```
 $ sudo apt-get install python-pip # Debian Like
```

* Instalando o Django Framework e o Django REST

```
$ pip install django
$ pip install djangorestframework
```

# Step - 2 : Iniciando o Projeto

## Criando a estrutura do projeto

Quando o Django for instalado, um novo pacote chamado django-admin.py estará disponível para ser acessado. Utilizaremos ele para iniciar e manipular projetos Django. 

* Iniciando a estrutura do projeto

Vamos utilizar o django-admin.py para criar toda a estrutura de pasta inicial do projeto. Neste exemplo estarei chamando de rest_api

```
 $ django-admin.py startproject rest_api
```

A estrutura básica do Django em si é muito minimalista. Esta é a estrutura de diretórios que será criada

```
rest_api/
├── manage.py
└── rest_api
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

1 directory, 5 files
```

## Nosso primeiro módulo

O Django por padrão nos permite gerenciar nossa aplicação por módulos. O que criamos até agora foi o core da aplicação, vamos nosso primeiro chamado *posts*

* Criando o nosso módulo POSTS

```
 $ cd rest_api
 $ django-admin.py startapp posts
```

Após a execução do comando será criado um diretório chamado *posts* na estrutura do nosso projeto, com o mínimo necessário para nosso projeto funcionar. 

```
rest_api/
├── manage.py
├── posts
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── rest_api
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
``` 

# Step - 3: Configurando o projeto

## Configurações dos módulos

Agora já temos toda a estrutura padrão do Django. Mas ainda não implementamos as funcionalidades do Django REST.

* Incluir o Django REST e o módulo posts no projeto

Precisamos editar o arquivo *rest_api/settings.py* adicionar as linhas *rest_framework* e o módulo *posts*: 

```
INSTALLED_APPS = [
    ...

    'posts',
    'rest_framework'
]
``` 
Sempre que quisermos adicionar um novo módulo, precisamos incluir o mesmo na lista *INSTALED_APPS* do *settings.py*

## Configurando as rotas em urls.py

As rotas, inicialmente são criadas a partir do arquivo urls.py do core da aplicação, no caso o arquivo *rest_api/urls.py*. Nele iremos fazer um esquema. Ao invés de usarmos ele para definir TODAS as rotas do nosso sistema, vamos configurá-lo para que ele inclua outros arquivos de rotas dentro dos nossos módulos, fazendo com que eles sejam independentes da aplicação principal. 

* Edite o arquito *rest_api/urls.py* de forma que fique parecido com o abaixo

``` python
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('posts.urls')),
]
```

* Agora CRIE o arquivo urls.py dentro do módulo posts, e nele iremos criar as rotas somente da responsabilidade do módulo. O arquivo deverá ficar em *posts/urls.py*

``` python
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from posts import views
 
urlpatterns = [
    url(r'^posts/$', views.PostList.as_view(), name="postagens"),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name="postagens-detail"),
]
``` 

Aqui fizemos algumas coisas: Primeiro importamos alguns módulos essenciais do Django. Depois importamos o arquivo views de dentro do módulo posts. ELE NÃO EXISTE AINDA. 

Depois criamos duas rotas utilizando expressões regulares simples a partir de 2 raw strings. 

Todos os requests enviados para: 
> /posts/

serão redirecionados para a classe PostList dentro do arquivo views.py

Todos os requests enviados para a url informando um integer: 
> /posts/{algum integer}

serão redirecionados para a classe PostDetail dentro do arquivo views.py

## Models, Serializers e Migrations

* Criando nosso primeiro Model

Os models são a representação dos nossos dados. Em um model no Django, podemos definir a estrutura das nossas tabelas e o Django se encarregará de tratá-las como entidades. Esse passo é muito importante para que será possível criar uma migração de dados diretamente pelo Django. O Django nos disponibiliza o arquivo *models.py*. Conforme nossa aplicação crescer seria legal também dividir isso em demais classes. Vamos editar o arquivo *posts/models.py*

```python
from django.db import models

class Post(models.Model):
    user = models.CharField("Usuario", max_length=100)
    mensagem = models.CharField("Mensagem", max_length=140)
```

* Criando nosso primeiro Serializer

Os serializers são um filtro sobre os dados que serão manipulados dentro da nossa API. Eles definem o que pode e o que não pode ser acessado via API e de que forma. Vamos criar nosso arquivo *serializers.py* em *posts/serializers.py*

```python
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
```

## Criando nossa primeira Migration

As migrations funcionam como um versionamento da estrutura do banco de dados. Com ela podemos aplicar e dar rollback no banco do nosso projeto. 

* Criando a migration 

```
$ python manage.py makemigrations


Migrations for 'posts':
  posts/migrations/0001_initial.py:
```

* Rodando a migration

```
$ python manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, posts, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying posts.0001_initial... OK
  Applying sessions.0001_initial... OK
```

Por default o Django trabalha com o SQlite, mas você pode alterar o mesmo para qualquer tipo de banco SQL para escalar seu projeto.

* Criando nossos Controllers em views.py

O arquivo views.py irá conter todas as nossas classes controladoras. Pode se assemelhar a um controller. Eu gosto de separar por arquivos de responsabilidade, mas para deixar simplista, vamos deixar tudo dentro do arquivo views mesmo. 

Crie o arquivo *posts/views.py*


``` python
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
```

* Classe PostList

Essa classe será responsável pela rota */posts/* e irá conter 2 verbos 

### Listar todas as postagens
> GET /posts/

### Criar uma nova postagem:
> POST /posts/

* Classe PostDetail

Essa classe será responsável pelos outros verbos

### Retornar a infomação do ID 1 
> GET /posts/1

### Atualizar as informações do ID 1 
> PUT /posts/1

### Deletar o ID 1 
> DELETE /posts/1


# Rodando o servidor

```
 $ python manage.py runserver
```

Agora acesse o servidor pelo browser

> http://localhost:8000/posts
