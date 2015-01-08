__author__ = 'gauee'
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from .forms import RegistrationForm


def index(request):
    return render_to_response('base.html', locals())

def contact(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            emailTo = request.POST.get('emailTo')
            emailFrom = request.POST.get('emailFrom')
            name = request.POST.get('name')
            content = request.POST.get('content')

            # sending email
            send_mail("Eurofundusze - Prosze o kontakt", content, name + "<" + emailFrom + ">", [emailTo],
                      fail_silently=False)

            return HttpResponseRedirect("/contact")
        else:
            return render(request, "contact.html",
                          {"form": form})
    else:
        form = RegistrationForm()
        return render(request, "contact.html",
                      {"form": form})

def multimedia(request):
    return render_to_response('multimedia.html', locals())

def sitemap(request):
    return render_to_response('sitemap.xml',locals())

def privacy_policy(request):
    return render_to_response('privacy_policy.html',locals())

