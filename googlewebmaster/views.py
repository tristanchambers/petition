from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def googlewebmaster(request):
    return HttpResponse("google-site-verification: %s.html" % settings.GOOGLE_SITE_VERIFICATION_CODE, content_type="text/plain")
