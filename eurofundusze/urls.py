from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap

from . import views
from sitemaps import Sitemap
from ef_ads.sitemaps import EmployeeOfferSitemap, EmployerOfferSitemap


sitemaps = {'tags': TagSitemap,
            'blog': EntrySitemap,
            'authors': AuthorSitemap,
            'categories': CategorySitemap,
            'employeeOffers': EmployeeOfferSitemap,
            'employerOffers': EmployerOfferSitemap,
            'flatpages': Sitemap(['ef_kontakt', 'ef_multimedia', 'ef_ogloszenia', ]), }

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
                       url(r'^contact/$', views.contact, name='ef_kontakt'),
                       url(r'^multimedia/$', views.multimedia, name='ef_multimedia'),
                       url(r'^ogloszenia/', include('ef_ads.urls')),
                       url(r'^utils/', include('utils.urls')),
                       url(r'^privacy_policy/$', views.privacy_policy),
                       url(r'^logout$', views.logout, name='logout'),


                       # Captcha
                       url(r'^captcha/', include('captcha.urls')),

                       # Zinnia
                       url(r'^', include('zinnia.urls', namespace='zinnia')),
                       url(r'^comments/', include('django_comments.urls')),
                       url(r'^', include(blog_urls, namespace='zinnia')),

                       # Django social auth
                       url('', include('social.apps.django_app.urls', namespace='social')),
                       url('', include('django.contrib.auth.urls', namespace='auth')),
)
# ) + static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += patterns('django.contrib.sitemaps.views',
                        url(r'^sitemap.xml$', 'index',
                            {'sitemaps': sitemaps}),
                        url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap',
                            {'sitemaps': sitemaps}), )
