__author__ = 'gauee'
from django.conf.urls import patterns,url
from utils import views



urlpatterns = patterns('utils.views',
    url('usefullink/change/up/([0-9]+)/$', views.change_up, name='change_up'),
    url('usefullink/change/down/([0-9]+)/$', views.change_down, name='change_down'),
)