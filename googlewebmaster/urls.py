from django.conf.urls import url
from . import views
from django.conf import settings

# https://docs.djangoproject.com/en/1.10/topics/http/urls/

urlpatterns = [
    # send key for any request under the path
    url(r'^%s\.html$' % settings.GOOGLE_SITE_VERIFICATION_CODE, views.googlewebmaster),
]
