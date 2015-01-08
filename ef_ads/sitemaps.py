__author__ = 'gauee'
from django.contrib import sitemaps

from .models import EmployerOffer, EmployeeOffer


class EmployeeOfferSitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return EmployeeOffer.objects.all()

    def lastmod(self, obj):
        return obj.modified_date


class EmployerOfferSitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return EmployerOffer.objects.all()

    def lastmod(self, obj):
        return obj.modified_date
