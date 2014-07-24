__author__ = 'gauee'
from django.conf.urls import url

from news import views

urlpatterns = [
    # ex: /news/
    url(r'^$', views.index, name='index'),
    # ex: /news/5/
    url(r'^(?P<news_id>[0-9]+)/$', views.detail, name='detail'),
]