from django import forms

from .models import Signature

class SignatureForm(forms.ModelForm):

    class Meta:
        model = Signature
        fields = (
            'first_name',
            'last_name',
            'street_address',
            'city',
            'state',
            'email',
            'comment',
            'dont_show_name',
            'opt_in',
        )
