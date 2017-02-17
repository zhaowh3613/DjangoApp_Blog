from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^post/$', views.post, name='post'),
    url(r'^post_action/$', views.post_action, name='post_action'),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
]
