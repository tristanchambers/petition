from django.conf.urls import url
from . import views
from django.views.generic import RedirectView
from petition.views import PetitionCreate, PetitionUpdate, PetitionDelete

    # https://docs.djangoproject.com/en/1.10/topics/http/urls/

urlpatterns = [
    url(r'^$', views.home),
#    url(r'^petition/(?P<slug>[-\w]+)/csv$', views.petition_csv),
    url(r'new/$', PetitionCreate.as_view(), name='petition-add'),
    url(r'(?P<slug>[-\w]+)/edit/$', PetitionUpdate.as_view(), name='petition-update'),
    url(r'(?P<slug>[-\w]+)/delete/$', PetitionDelete.as_view(), name='petition-delete'),
    url(r'^(?P<slug>[-\w]+)/$', views.petition_detail),
]
