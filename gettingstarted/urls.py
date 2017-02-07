from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('petition.urls')),
    # https://docs.djangoproject.com/en/1.9/topics/auth/default/#module-django.contrib.auth.views
    url('^', include('django.contrib.auth.urls')),
]
