# -*- coding: utf-8 -*-
__author__ = 'gauee'
from django import template

register = template.Library()


@register.inclusion_tag('ads_navigation.html')
def get_ads_navigation():
    return {}
