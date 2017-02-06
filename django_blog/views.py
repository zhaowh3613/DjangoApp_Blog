from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    # article = models.Article.objects.get(pk=1)
    articleList = models.Article.objects.all()
    return render(request, 'django_blog/index.html', {'articles': articleList})
