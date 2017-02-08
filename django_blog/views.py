from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    # article = models.Article.objects.get(pk=1)
    articleList = models.Article.objects.all()
    return render(request, 'django_blog/index.html', {'articles': articleList})

def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'django_blog/article_page.html', {'article': article})

def about(request):
    return render(request, 'django_blog/about.html')

def contact(request):
    return render(request, 'django_blog/contact.html')
