# -*- coding: utf-8 -*-
from django.contrib import admin

from ef_ads.models import EmployeeOffer, EmployerOffer


def make_published(modeladmin, request, queryset):
    queryset.update(status='P')


make_published.short_description = u"Oznacz ofertę jako publiczną"


# Register your models here.
class AdminEmployeeOffer(admin.ModelAdmin):
    fields = ['status', 'created_date', 'modified_date', 'author', 'email', 'phone_number', 'title', 'content',
              'experience', 'extraDoc']
    list_display = ('modified_date', 'author', 'email', 'title', 'status')
    actions = [make_published]


class AdminEmployerOffer(admin.ModelAdmin):
    fields = ['status', 'start_date', 'finish_date', 'budget', 'created_date', 'modified_date', 'author', 'email',
              'phone_number', 'title', 'content', 'extraDoc']
    list_display = ('modified_date', 'author', 'email', 'title', 'budget', 'status')
    actions = [make_published]


admin.site.register(EmployeeOffer, AdminEmployeeOffer)
admin.site.register(EmployerOffer, AdminEmployerOffer)