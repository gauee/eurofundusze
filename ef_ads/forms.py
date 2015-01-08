# -*- coding: utf-8 -*-
TIME_FORMAT = '%Y-%m-%d'
__author__ = 'gauee'
import datetime

from django import forms

# Import the CaptchaField from 'django-simple-captcha'
from captcha.fields import CaptchaField
from phonenumber_field.formfields import PhoneNumberField


class ExtFileField(forms.FileField):
    widget = None

    def __init__(self, *args, **kwargs):
        self.widget = forms.ClearableFileInput(attrs={'accept': kwargs.pop('accept', None)})
        super(ExtFileField, self).__init__(*args, **kwargs)


class OfferForm(forms.Form):
    author = forms.CharField(label="Autor", widget=forms.TextInput(attrs={'placeholder': 'Imię Nazwisko'}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'placeholder': 'example@domain.com'}))
    phone = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': '+48 XXX XXX XXX'}))
    title = forms.CharField(label=u"Tytuł", widget=forms.TextInput(attrs={'placeholder': 'Tytuł ogłoszenia'}))
    content = forms.CharField(label=u"Treść", widget=forms.Textarea(attrs={'placeholder': 'Treść ogłoszenia'}))
    extraDoc = ExtFileField(label=u'Załącznik', accept='.pdf,.txt', help_text='max. 42 megabytes', required=False)
    captcha = CaptchaField(label="")


class EmployerOfferForm(OfferForm):
    start_date = forms.DateField(label=u"Czas rozpoczęcia", initial=datetime.date.today,
                                 widget=forms.DateInput(format=TIME_FORMAT, attrs={'placeholder': 'YYYY-MM-DD'}),
    )
    end_date = forms.DateField(label=u"Czas zakończenia", initial=datetime.date.today,
                               widget=forms.DateInput(format=TIME_FORMAT, attrs={'placeholder': 'YYYY-MM-DD'}),
    )
    budget = forms.IntegerField(label=u"Budżet", widget=forms.TextInput(attrs={'placeholder': 'Oczekiwany budżet'}))

    def __init__(self, *args, **kwargs):
        super(EmployerOfferForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['author', 'email', 'phone', 'title', 'content', 'start_date', 'end_date', 'budget',
                                'extraDoc', 'captcha']


class EmployeeOfferForm(OfferForm):
    experience = forms.CharField(label=u"Doświadczenie",
                                 widget=forms.Textarea(attrs={'placeholder': 'Doświadczenie w podobnych projektach'}))

    def __init__(self, *args, **kwargs):
        super(EmployeeOfferForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['author', 'email', 'phone', 'title', 'content', 'experience', 'extraDoc', 'captcha']


