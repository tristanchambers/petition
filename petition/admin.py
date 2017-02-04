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
class SignatureAdmin(ImportExportModelAdmin):
    resource_class = SignatureResource # Set up import/export resource
    list_display = ('first_name', 'last_name','city', 'state', 'created_date')
    list_display_links = ('first_name', 'last_name')
    list_filter = ('petition__title', 'state', 'city')

class PetitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'signatures_num')
    view_on_site = True

# Register admin forms
admin.site.register(Signature, SignatureAdmin)
admin.site.register(Petition, PetitionAdmin)
