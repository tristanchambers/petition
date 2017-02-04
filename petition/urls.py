from django.conf.urls import url
from . import views

    # https://docs.djangoproject.com/en/1.10/topics/http/urls/

urlpatterns = [
    url(r'^petitions/$', views.petition_list),
    url(r'^petition/(?P<slug>[-\w]+)/csv$', views.petition_csv),
    url(r'^petition/(?P<slug>[-\w]+)/$', views.petition_detail),
]
