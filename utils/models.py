# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Max

# Create your models here.


class UsefulLink(models.Model):
    name = models.CharField(max_length=200,verbose_name='Nazwa linku')
    href = models.CharField(max_length=200,verbose_name='Adres linku')
    order = models.IntegerField()

    #Meta info
    class Meta:
        verbose_name = 'Przydatny Link'
        verbose_name_plural = 'Przydatne Linki'

    def save(self, *args, **kwargs):
        if not self.order:
            maxId = UsefulLink.objects.all().aggregate(Max('order')).get('order__max')
            if maxId == None:
                maxId = 0
            maxId = maxId+1
            self.order = maxId

        super(UsefulLink, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s, %s, %s' % (self.name, self.href, str(self.order))

    def setOrder(self,order):
        self.order = order
