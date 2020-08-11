from django import forms
from .models import *

class UrlForms(forms.ModelForm):
    class Meta:
        model = short_url
        fields = ['long_url']