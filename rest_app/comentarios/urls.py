from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from comentarios import views
 
urlpatterns = [
    url(r'^comentarios/$', views.ComentarioList.as_view(), name="comentarios"),
    url(r'^comentarios/(?P<pk>[0-9]+)/$', views.ComentarioDetail.as_view(), name="comentarios-detail"),
    url(r'^$', views.ComentarioList.as_view()),

    url(r'^posts/$', views.PostList.as_view(), name="postagens"),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name="postagens"),
]