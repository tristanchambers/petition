from django.conf.urls import url
from . import views
from django.views.generic import RedirectView


    # https://docs.djangoproject.com/en/1.10/topics/http/urls/

urlpatterns = [
    url(r'^$', views.home),
    url(r'^petition/$', RedirectView.as_view(url='/')),
    url(r'^petition/(?P<slug>[-\w]+)/csv$', views.petition_csv),
    url(r'^petition/(?P<slug>[-\w]+)/$', views.petition_detail),
]
