from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
class Rate(models.Model):
    currency = models.CharField(max_length=3)
    descr = models.CharField(max_length=64)
    visible = models.BooleanField()

    def __str__(self):
        # return self.currency + ", " + self.descr + ", " + str(self.visible)
        return self.currency + ", " + str(self.visible)