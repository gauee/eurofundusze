from django.contrib import admin
from widget_exchange_rates.models import Rate
# Register your models here.


class AdminRate(admin.ModelAdmin):
    fields = ['currency','descr','visible']
    list_display = ('currency','descr','visible')

admin.site.register(Rate,AdminRate)