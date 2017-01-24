from django.conf.urls import url
from . import views

    # https://docs.djangoproject.com/en/1.10/topics/http/urls/

urlpatterns = [
    url(r'^petitions/$', views.petition_list),
    url(r'^petitions/(?P<primary_key>\d+)/$', views.petition_detail),
]
