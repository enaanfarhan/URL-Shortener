from django.shortcuts import render
from .models import *
from .forms import *
from .shortener import *


# Create your views here.
def Make(request):
    form = UrlForms(request.POST)
    a = ""
    if request.method == 'POST':
        if form.is_valid():
            NewUrl = form.save(commit=False)
            a = shortener().issue_token()
            NewUrl.save()
        else:
            form = UrlForms()
            a = "Invalid Url"
    return render(request, 'home.html', { 'form':form, 'a':a })