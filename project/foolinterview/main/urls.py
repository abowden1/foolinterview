from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^a/(?P<uuid>.+)$', views.article, name='article'),
    url(r'^shuffle$', views.shuffle, name='shuffle'),
    url(r'post/$', views.addcomment, name='addcomment')
]