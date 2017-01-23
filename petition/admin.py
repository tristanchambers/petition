from django.contrib import admin

# Register your models here.
# https://docs.djangoproject.com/en/1.10/ref/contrib/admin/

from .models import Petition
from .models import Signature

class SignatureInline(admin.StackedInline):
    model = Signature

class PetitionAdmin(admin.ModelAdmin):
    inlines = [
        SignatureInline,
    ]

admin.site.register(Signature)
admin.site.register(Petition, PetitionAdmin)
