from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
# https://docs.djangoproject.com/en/1.10/topics/http/views/

from .models import Petition
from .models import Signature
from .forms import SignatureForm

def petition_list(request):
    petitions = Petition.objects.all()
    return render(request, 'petition/petition_list.html', {'petitions': petitions})

def petition_detail(request, primary_key):
    petition = get_object_or_404(Petition, pk=primary_key)
    signatures = Signature.objects.filter(petition=1)
    # If this is a form submission, process the request
    # check if the user already signed the petition
    signed = request.session.get('has_signed', False)
    if request.method == "POST":
        if not signed:
            signform_data = SignatureForm(request.POST)
            if signform_data.is_valid():
                signature = signform_data.save(commit=False)
                signature.petition = petition
                signature.save()
                request.session['has_signed'] = True

    # Either way render the petition details
    signform = SignatureForm()
    return render(
        request,
        'petition/petition_detail.html',
        {
            'petition': petition,
            'signatures': signatures,
            'signform': signform,
            'signed': signed,
        },
    )
