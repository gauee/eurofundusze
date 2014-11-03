# -*- coding: utf-8 -*-
from django.db import models
import logging
from django.utils import timezone
import re

# Create your models here.

logger = logging.getLogger(__name__)
url_pattern = "watch?v="

class Video_YU(models.Model):
    video_title = models.CharField(max_length=200,verbose_name=u'Tytuł filmu')
    video_yu_url = models.CharField(max_length=200,verbose_name='Adres url z serwisu Youtube')
    video_yu_id = models.CharField(max_length=100)
    video_yu_create_time = models.DateTimeField(default=timezone.now(),verbose_name='Data dodania')

    # this is not needed if small_image is created at set_image
    def save(self, *args, **kwargs):
        if not self.video_yu_id:
            self.video_yu_create_time = timezone.now()

        print self.video_yu_create_time
        idx = self.video_yu_url.find(url_pattern)
        self.video_yu_id = self.video_yu_url[(idx+url_pattern.__len__()):]
        super(Video_YU, self).save(*args, **kwargs)

    #Meta info
    class Meta:
        verbose_name = 'Film Youtube'
        verbose_name_plural = 'Filmy Youtube'

    def getIframeUrl(self):
        return '<iframe width="280" height="157" src="//www.youtube.com/embed/%s" frameborder="0" allowfullscreen=""></iframe>'%self.video_yu_id