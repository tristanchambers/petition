from django.conf.urls import include, url
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
admin.autodiscover()

from petition.models import Petition
info_dict = {
    'queryset': Petition.objects.all(),
}

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('petition.urls')),
    url(r'', include('letsencrypt.urls')),
    url(r'', include('googlewebmaster.urls')),
    # the sitemap
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
        name='django.contrib.sitemaps.views.sitemap'),
]
