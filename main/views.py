from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from news.models import News

# Create your views here.


def home(request):

    site = Main.objects.get(name = "My Site Settings")
    news = News.objects.all()

    return render(request, 'front/home.html', {'site':site, 'news': news})


def about(request):

    site = Main.objects.get(name = "My Site Settings")

    return render(request, 'front/about.html', {'site':site}) 