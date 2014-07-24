from django import forms
from django.contrib import admin
from .models import Comment,News
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.admin import SummernoteModelAdmin

class AdminNewsForm(forms.ModelForm):
    class Meta:
        model = News
        widgets = {
            'foo': SummernoteWidget(),
            'bar': SummernoteInplaceWidget(),
        }

class AdminComment(admin.ModelAdmin):
    class Meta:
        model = Comment

class AdminNews(SummernoteModelAdmin):
    form = AdminNewsForm

    list_display = ('create_date','title','descr')
    fieldsets= [
        (None,{'fields' :[
            ('title')
        ]
        }),
        (None,{'fields' :[
            ('descr')
        ]
        }),
        (None,{'fields' :[
            ('content',)
        ]
        }),
    ]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author_id', None) is None:
            obj.author = request.user
        obj.save()

admin.site.register(Comment,AdminComment)
admin.site.register(News,AdminNews)