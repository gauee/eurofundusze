from django.contrib import admin
from utils.models import UsefulLink

# Register your models here.

class AdminUsefulLink(admin.ModelAdmin):
    fields = ['name', 'href']
    list_display = ('name', 'href', 'inc_pos')

    def inc_pos(self, obj):
        return '<a href=/utils/usefullink/change/up/%s>Down</a>' \
               ' / ' \
               '<a href=/utils/usefullink/change/down/%s>Up</a>' % (
        str(obj.order), str(obj.order))

    inc_pos.allow_tags = True
    inc_pos.short_description = 'Order'

    ordering = ['order']


admin.site.register(UsefulLink, AdminUsefulLink)