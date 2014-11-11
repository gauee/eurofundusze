from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from . import views

admin.autodiscover()

blog_urls = [
    url(r'^', include('zinnia.urls.capabilities')),
    url(r'^search/', include('zinnia.urls.search')),
    url(r'^sitemap/', include('zinnia.urls.sitemap')),
    url(r'^trackback/', include('zinnia.urls.trackback')),
    url(r'^blog/tags/', include('zinnia.urls.tags')),
    url(r'^blog/feeds/', include('zinnia.urls.feeds')),
    url(r'^blog/random/', include('zinnia.urls.random')),
    url(r'^blog/authors/', include('zinnia.urls.authors')),
    url(r'^blog/categories/', include('zinnia.urls.categories')),
    url(r'^blog/comments/', include('zinnia.urls.comments')),
    url(r'^blog/', include('zinnia.urls.entries')),
    url(r'^blog/', include('zinnia.urls.archives')),
    url(r'^blog/', include('zinnia.urls.shortlink')),
    url(r'^blog/', include('zinnia.urls.quick_entry'))
];

urlpatterns = patterns('',
                       # Examples:
                       # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                           'document_root': settings.MEDIA_ROOT, }),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^contact/$',views.contact),
                       url(r'^multimedia/$',views.multimedia),
                       # url(r'^ogloszenia/',include('ef_ads.urls')),
                       url(r'^utils/',include('utils.urls')),
                       url(r'^privacy_policy/$',views.privacy_policy),

                       # Zinnia
                       url(r'^', include('zinnia.urls', namespace='zinnia')),
                       url(r'^comments/', include('django_comments.urls')),
                       url(r'^', include(blog_urls, namespace='zinnia')),

                       #Django social auth
                       # url(r'', include('social_auth.urls', namespace='social')),
)

