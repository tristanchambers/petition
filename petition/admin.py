from django.contrib import admin

# Register your models here.
# https://docs.djangoproject.com/en/1.10/ref/contrib/admin/

from .models import Petition
from .models import Signature
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Set up import/export utility on signatures
class SignatureResource(resources.ModelResource):

    class Meta:
        model = Signature

# Set up custom Signature admin settings
class SignatureIEAdmin(ImportExportModelAdmin):
    resource_class = SignatureResource
    list_display = ('first_name', 'last_name','city', 'state', 'created_date')

# Register admin forms
admin.site.register(Signature, SignatureIEAdmin)
admin.site.register(Petition)
