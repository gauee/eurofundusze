from django.shortcuts import render,redirect,HttpResponseRedirect
from utils.models import UsefulLink
from django.db.models import Max,Min

# Create your views here.
def change_up(request, pos):
    maxId = UsefulLink.objects.all().aggregate(Max('order')).get('order__max')
    pos = int(pos)

    if pos < maxId:
        objectOne = UsefulLink.objects.filter(order=pos)[0]
        objectTwo = UsefulLink.objects.filter(order=(pos+1))[0]
        objectOne.setOrder(pos+1)
        objectTwo.setOrder(pos)
        objectOne.save()
        objectTwo.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def change_down(request, pos):
    pos = int(pos)
    minId = UsefulLink.objects.all().aggregate(Min('order')).get('order__min')

    if pos > minId:
        objectOne = UsefulLink.objects.filter(order=pos)[0]
        objectTwo = UsefulLink.objects.filter(order=(pos-1))[0]
        objectOne.setOrder(pos-1)
        objectTwo.setOrder(pos)
        objectOne.save()
        objectTwo.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))