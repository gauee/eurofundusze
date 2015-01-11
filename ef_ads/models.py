# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
OFFER_STATUS = (
    ('D', 'Draft'),
    ('P', 'Public'),
    ('A', 'Archive')
)


class Offer(models.Model):
    created_date = models.DateTimeField(default=timezone.now(), verbose_name='Data dodania')
    modified_date = models.DateTimeField(default=timezone.now(), verbose_name='Data zmiany')
    author = models.CharField(max_length=200, verbose_name=u'Autor zgłoszenia')
    email = models.EmailField()
    phone_number = PhoneNumberField()
    title = models.CharField(max_length=200, verbose_name=u'Tytuł ogłoszenia')
    content = models.CharField(max_length=1024, verbose_name=u'Tresc ogloszenia')
    status = models.CharField(max_length=1, choices=OFFER_STATUS)
    extraDoc = models.FileField(blank=True,
                                upload_to=lambda instance, filename:
                                'ogloszenia/{0}/{1}/{2}/{3}/{4}_{5}'.format(
                                    instance.author,
                                    instance.created_date.year,
                                    instance.created_date.month,
                                    instance.created_date.day,
                                    getLastId(),
                                    filename.encode('utf-8')))

    def save(self, *args, **kwargs):
        if not self.status:
            self.status = 'D'
        super(Offer, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "/ogloszenia/"


def getLastId():
    o = Offer.objects.all()
    if o:
        return Offer.objects.latest('id').id
    return 0

class EmployerOffer(Offer):
    start_date = models.DateField()
    finish_date = models.DateField()
    budget = models.IntegerField()

    def get_absolute_url(self):
        return super(EmployerOffer, self).get_absolute_url() + "zlecenia/%d" % self.id


class EmployeeOffer(Offer):
    experience = models.CharField(max_length=1024)

    def get_absolute_url(self):
        return super(EmployeeOffer, self).get_absolute_url() + "wykonania/%d" % self.id

