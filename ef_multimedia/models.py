from django.db import models
import logging
import re

# Create your models here.

logger = logging.getLogger(__name__)
url_pattern = "watch?v="

class Video_YU(models.Model):
    video_title = models.CharField(max_length=200)
    video_yu_url = models.CharField(max_length=200)
    video_yu_id = models.CharField(max_length=100)

    # this is not needed if small_image is created at set_image
    def save(self, *args, **kwargs):
        print 'saving Video Youtube'
        print self.video_yu_url

        idx = self.video_yu_url.find(url_pattern)
        self.video_yu_id = self.video_yu_url[(idx+url_pattern.__len__()):]
        print self.video_yu_id
        print self.getIframeUrl()
        super(Video_YU, self).save(*args, **kwargs)

    #Meta info
    class Meta:
        verbose_name = 'Film Youtube'
        verbose_name_plural = 'Filmy Youtube'

    def getIframeUrl(self):
        return '<iframe width="280" height="157" src="//www.youtube.com/embed/%s" frameborder="0" allowfullscreen=""></iframe>'%self.video_yu_id