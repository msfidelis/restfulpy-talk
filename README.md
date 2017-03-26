

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

## Configurando as rotas 

As rotas, inicialmente são criadas a partir do arquivo urls.py do core da aplicação, no caso o arquivo *rest_api/urls.py*. Nele iremos fazer um esquema. Ao invés de usarmos ele para definir TODAS as rotas do nosso sistema, vamos configurá-lo para que ele inclua outros arquivos de rotas dentro dos nossos módulos, fazendo com que eles sejam independentes da aplicação principal. 

* Edite o arquito *rest_api/urls.py* de forma que fique parecido com o abaixo

``` python
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^posts/', include('posts.urls')),
]
```

* Agora CRIE o arquivo urls.py dentro do módulo posts, e nele iremos criar as rotas somente da responsabilidade do módulo. O arquivo deverá ficar em *posts/urls.py*

``` python
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from posts import views
 
urlpatterns = [
    url(r'^posts/$', views.Post.as_view(), name="postagens"),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name="postagens-detail"),
]
``` 

Aqui fizemos algumas coisas: Primeiro importamos alguns módulos essenciais do Django. Depois importamos o arquivo views de dentro do módulo posts. ELE NÃO EXISTE AINDA. 

Depois criamos duas rotas utilizando expressões regulares simples. 

