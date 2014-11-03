from django.contrib import admin
from ef_multimedia.models import Video_YU
import logging

logger = logging.getLogger(__name__)

# Register your models here.
class AdminVideo_YU(admin.ModelAdmin):
    fields = ['video_title','video_yu_url','video_yu_create_time']
    list_display = ('video_title','video_yu_url')


admin.site.register(Video_YU,AdminVideo_YU)