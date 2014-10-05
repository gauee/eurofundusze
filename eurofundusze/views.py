__author__ = 'gauee'
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('base.html', locals())



def contact(request):
    return render_to_response('contact.html', locals())

def multimedia(request):
    return render_to_response('multimedia.html', locals())

def sitemap(request):
    return render_to_response('sitemap.xml',locals())