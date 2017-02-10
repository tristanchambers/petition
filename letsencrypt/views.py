from django.shortcuts import render
from django.http import HttpResponse, Http404
import os

# Create your views here.


def challenge_reply(request, slug):
    acme_key = os.environ.get('ACME_CHALLENGE_KEY')
    acme_name = os.environ.get('ACME_CHALLENGE_NAME')
    if slug == acme_name:
        return HttpResponse(acme_key)
    else:
        raise Http404("Not found")
