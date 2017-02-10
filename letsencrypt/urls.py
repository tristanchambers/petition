from django.conf.urls import url
from . import views

# https://docs.djangoproject.com/en/1.10/topics/http/urls/

urlpatterns = [
    # send key for any request under the path
    url(r'^\.well-known/acme-challenge/(?P<slug>.*)$', views.challenge_reply),
]
