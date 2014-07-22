from django.contrib import admin

# Register your models here.
from .models import Comment,News

class AdminComment(admin.ModelAdmin):
    class Meta:
        model = Comment

class AdminNews(admin.ModelAdmin):
    class Meta:
        model = News

admin.site.register(Comment,AdminComment)
admin.site.register(News,AdminNews)