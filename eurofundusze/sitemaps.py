__author__ = 'gauee'
import datetime

from django.contrib import sitemaps
from django.core.urlresolvers import reverse


class Sitemap(sitemaps.Sitemap):
    def __init__(self, names):
        self.names = names

    def items(self):
        return self.names

    def changefreq(self, obj):
        return 'weekly'

    def lastmod(self, obj):
        return datetime.datetime.now()

    def location(self, obj):
        return reverse(obj)


class EfFlatPagesSitemap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return ['main', 'about', 'license']

    def lastmod(self, obj):
        return obj.date


