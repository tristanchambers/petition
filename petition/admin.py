from django.contrib import admin

# Register your models here.
# https://docs.djangoproject.com/en/1.10/ref/contrib/admin/

from .models import Petition
from .models import Signature

admin.site.register(Petition)
admin.site.register(Signature)
