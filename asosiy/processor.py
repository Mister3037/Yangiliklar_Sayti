from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.views.generic import TemplateView

from .models import *

def latest_news(request):
    latest_news = Yangiliklar.objects.all().order_by("-publish_time")[:10]

    content = {
        "latest_news": latest_news
    }
    return content

