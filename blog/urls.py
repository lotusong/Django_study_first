# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [

   url(r'^$', views.index, name='index'),
   url(r'^index/$', views.index, name='index'),
   url(r'^article/$', views.article, name='article'),
   url(r'^photo/$', views.photo, name='photo'),
   url(r'^about/$', views.about, name='about'),
   url(r'^contact/$', views.contact, name='contact'),
   url(r'^article/(?P<id>[0-9]+)/$',views.detail, name='detail'),
   url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives, name='archives'),
   url(r'^category/(?P<id>[0-9]+)/$',views.category, name='category'),
   url(r'^tag/(?P<id>[0-9]+)/$', views.tag, name='tag'),
]
