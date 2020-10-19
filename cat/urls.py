from cat.models import Cat
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^panel/cat_list/$', views.cat_list, name='cat_list'),
    url(r'^panel/cat_add/$', views.cat_add, name='cat_add'),
    url(r'^panel/cat_delete/(?P<pk>\d+)$', views.cat_delete, name='cat_delete'),
]