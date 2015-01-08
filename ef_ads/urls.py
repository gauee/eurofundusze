__author__ = 'gauee'
from django.conf.urls import patterns, url

from ef_ads import views


urlpatterns = patterns('ef_ads.views',
                       url(r'^$', views.index, name='ef_ogloszenia'),
                       url('^wykonania/$', views.employee_offer, name='employee_offer'),
                       url('^wykonania/([0-9]+)/$', views.employee_offer_number, name='employee_offer_number'),
                       url('^nowe_wykonanie/$', views.new_employee_offer, name='new_employee_offer'),
                       url('^zlecenia/$', views.employer_offer, name='employer_offer'),
                       url('^zlecenia/([0-9]+)/$', views.employer_offer_number, name='employer_offer_number'),
                       url('^nowe_zlecenie/$', views.new_employer_offer, name='new_employer_offer'),
)

