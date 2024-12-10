from django.shortcuts import render
from .models import articles

headlines = articles.objects.all()


def index(request):
    context = {
        'news' : headlines
    }
    return render(request,'index.html',context)

def home(request):
    context = {
        'news' : headlines
    }
    return render(request,'home.html',context)

def about_me(request):
    context = {
        'news' : headlines
    }
    return render(request,'about_me.html',context)

def blog(request,pk):
    headlines1 = articles.objects.get(id = pk)
    context = {
        'headlines1' : headlines1
    }
    return render(request,'blog.html',context)