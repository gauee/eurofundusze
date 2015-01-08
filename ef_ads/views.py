# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect

from .forms import EmployeeOfferForm, EmployerOfferForm
from .models import EmployeeOffer, EmployerOffer


# Create your views here.
EMPLOYEE_OFFER_HEADLINES = [u'Tytuł', 'Autor', 'Data']
EMPLOYER_OFFER_HEADLINES = [u'Tytuł', 'Autor', 'Data']


def index(request):
    return render_to_response('ogloszenia.html', locals())


def employee_offer(request):
    objects = EmployeeOffer.objects.filter(status='P').order_by('-created_date')
    headlines = EMPLOYEE_OFFER_HEADLINES

    offers = []
    for o in objects:
        tmp = []
        tmp.append(o.title)
        tmp.append(o.author)
        tmp.append(o.created_date)
        offer = []
        offer.append('/ogloszenia/wykonania/' + str(o.id) + '/')
        offer.append(tmp)
        offers.append(offer)

    return render_to_response('offer_list.html', {'headlines': headlines, 'offers': offers})


def employee_offer_number(request, offerNum):
    object = EmployeeOffer.objects.filter(id=offerNum)[0]
    offer = [
        ['Autor', object.author],
        ['Tytuł', object.title],
        ['Data powstania', object.created_date],
        ['Data ostatniej modyfikacji', object.modified_date],
        ['Adres email', object.email],
        ['Numer telefonu', object.phone_number],
        [u'Treść ogłoszenia', object.content],
    ]
    attachment = addAttachmentIfExist(object)
    return render_to_response('offer_details.html', {'offer': offer, 'attachment': attachment})


dateFormat = "%d/%m/%Y"


def addAttachmentIfExist(object):
    attachment = []
    if object.extraDoc:
        attachment.append([u'Załącznik', object.extraDoc])
    return attachment


def employer_offer_number(request, offerNum):
    object = EmployerOffer.objects.filter(id=offerNum)[0]

    timeDistance = object.start_date.__format__(dateFormat) + " - " + object.finish_date.__format__(dateFormat)
    budgetVal = str(object.budget) + u' zł'
    offer = [
        ['Autor', object.author],
        ['Tytuł', object.title],
        ['Data powstania', object.created_date],
        ['Data ostatniej modyfikacji', object.modified_date],
        ['Adres email', object.email],
        ['Numer telefonu', object.phone_number],
        [u'Budżet', budgetVal],
        ['Termin realizacji', timeDistance],
        [u'Treść ogłoszenia', object.content],
    ]
    attachment = addAttachmentIfExist(object)
    return render_to_response('offer_details.html', {'offer': offer, 'attachment': attachment})


def new_employee_offer(request):
    if request.method == 'POST':
        print 'Post request'
        form = EmployeeOfferForm(request.POST, request.FILES)
        if form.is_valid():
            offer = EmployeeOffer()
            initBaseOffer(request, offer)
            offer.experience = request.POST.get('experience')

            offer.save()

            return HttpResponseRedirect("/ogloszenia/nowe_wykonanie")
        else:
            return render(request, "add_offer.html",
                          {'form': form})

    print 'Get request'
    form = EmployeeOfferForm()
    return render(request, "add_offer.html",
                  {'form': form})


def employer_offer(request):
    objects = EmployerOffer.objects.filter(status='P').order_by('-created_date')
    headlines = EMPLOYER_OFFER_HEADLINES

    offers = []
    for o in objects:
        tmp = []
        tmp.append(o.title)
        tmp.append(o.author)
        tmp.append(o.created_date)
        offer = []
        offer.append('/ogloszenia/zlecenia/' + str(o.id) + '/')
        offer.append(tmp)
        offers.append(offer)

    return render_to_response('offer_list.html', {'headlines': headlines, 'offers': offers})


def new_employer_offer(request):
    if request.method == 'POST':
        print 'Post request'
        form = EmployerOfferForm(request.POST, request.FILES)
        if form.is_valid():
            offer = EmployerOffer()
            initBaseOffer(request, offer)
            offer.budget = request.POST.get('budget')
            offer.start_date = request.POST.get('start_date')
            offer.finish_date = request.POST.get('end_date')

            offer.save()

            return HttpResponseRedirect("/ogloszenia/nowe_zlecenie")
        else:
            return render(request, "add_offer.html",
                          {'form': form})

    print 'Get request'
    form = EmployerOfferForm()
    return render(request, "add_offer.html",
                  {'form': form})


def initBaseOffer(request, offer):
    offer.author = request.POST.get('author')
    offer.content = request.POST.get('content')
    offer.email = request.POST.get('email')
    offer.phone_number = request.POST.get('phone')
    offer.title = request.POST.get('title')
    if request.FILES:
        offer.extraDoc = request.FILES['extraDoc']
    else:
        print 'No files in request'

