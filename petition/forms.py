from django import forms

from .models import Signature

class SignatureForm(forms.ModelForm):

    class Meta:
        model = Signature
        fields = (
            'first',
            'last',
            'street',
            'city',
            'zip_code',
            'email',
            'show_name',
            'opt_in',
        )
