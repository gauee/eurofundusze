from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode

# Create your models here.

class Message(models.Model):
    author = models.ForeignKey(User)
    content = models.TextField(max_length=1024)
    create_date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return smart_unicode(self.author)

class News(Message):
    title = models.CharField(max_length=64)
    descr = models.CharField(max_length=256)

    def __unicode__(self):
        return smart_unicode(self.author) + " | " + smart_unicode(self.create_date) + " | " + smart_unicode(self.descr)

class Comment(Message):
    news = models.ForeignKey(News)


