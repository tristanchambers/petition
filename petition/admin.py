from django.contrib import admin

# Register your models here.
# https://docs.djangoproject.com/en/1.10/ref/contrib/admin/

from .models import Petition
from .models import Signature
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class SignatureInline(admin.TabularInline):
    model = Signature

class PetitionAdmin(admin.ModelAdmin):
    inlines = [
        SignatureInline,
    ]

class SignatureResource(resources.ModelResource):

    class Meta:
        model = Signature

class SignatureIEAdmin(ImportExportModelAdmin):
    resource_class = SignatureResource

admin.site.register(Signature, SignatureIEAdmin)
admin.site.register(Petition, PetitionAdmin)
