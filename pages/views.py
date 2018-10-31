from django.shortcuts import render
from django.http import HttpResponse
import os
# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def about_view(request, *arg, **kwargs):
    return render(request, 'about.html', {})

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html',{})