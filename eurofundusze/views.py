__author__ = 'gauee'
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.core.mail import send_mail
from django.contrib.auth import logout as auth_logout

from .forms import RegistrationForm


INDEX_PAGE = 'base.html'

def index(request):
    context = RequestContext(request,
                             {'request': request,
                              'user': request.user})
    return render_to_response(INDEX_PAGE,
                              context_instance=context)


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
    context = RequestContext(request,
                             {'request': request,
                              'user': request.user})
    return render_to_response('multimedia.html', context_instance=context)


def sitemap(request):
    return render_to_response('sitemap.xml', locals())


def privacy_policy(request):
    return render_to_response('privacy_policy.html', locals())


def logout(request):
    context = {}
    try:
        auth_logout(request)
    except:
        context['error'] = 'Some error occured.'

    populateContext(request, context)
    return HttpResponseRedirect("/")


def populateContext(request, context):
    context['authenticated'] = request.user.is_authenticated()
    if context['authenticated']:
        context['username'] = request.user.username

