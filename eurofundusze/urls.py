from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'eurofundusze.views.index'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^news/', include('news.urls')),
                       (r'^summernote/', include('django_summernote.urls')),
)
