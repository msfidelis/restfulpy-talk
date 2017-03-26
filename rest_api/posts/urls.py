# -*- coding: UTF-8 -*-

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from posts import views
 
urlpatterns = [
    url(r'^posts/$', views.PostList.as_view(), name="postagens"),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name="postagens_detail"),
]