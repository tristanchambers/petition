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
            'state',
            'email',
            'dont_show_name',
            'opt_in',
        )
