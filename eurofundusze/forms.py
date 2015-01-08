# -*- coding: utf-8 -*-
__author__ = 'gauee'

from django import forms

# Import the CaptchaField from 'django-simple-captcha'
from captcha.fields import CaptchaField


# Supporting emails address
EMAILS_ADDR = (
    ('redakcja@eurofundusze.eu', 'Redakcja'),
    ('reklama@eurofundusze.eu', 'Reklama'),
    ('admin@eurofundusze.eu', 'Administrator'),
)

# Create form class for the Registration form
class RegistrationForm(forms.Form):
    emailTo = forms.ChoiceField(label="Odbiorca", widget=forms.Select, choices=EMAILS_ADDR)
    name = forms.CharField(label="Dane", widget=forms.TextInput(attrs={'placeholder': 'Imię Nazwisko'}))
    emailFrom = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'placeholder': 'example@domain.com'}))
    content = forms.CharField(label=u"Treść", widget=forms.Textarea(attrs={'placeholder': 'Treść wiadomości'}))
    captcha = CaptchaField(label="")
