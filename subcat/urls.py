from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^panel/subcat_list/$', views.subcat_list, name='subcat_list'),
    url(r'^panel/subcat_add/$', views.subcat_add, name='subcat_add'),
    url(r'^panel/subcat_delete/(?P<pk>\d+)$', views.subcat_delete, name='subcat_delete'),
]