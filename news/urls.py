from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^panel/news_list/$', views.news_list, name='news_list'),
    url(r'^panel/news_add/$', views.news_add, name='news_add'),
    url(r'^panel/news_delete/(?P<pk>\d+)/$', views.news_delete, name='news_delete'),
    url(r'^news/(?P<word>.*)/$', views.news_detail, name='news_detail'),
]