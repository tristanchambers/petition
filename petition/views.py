from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
# https://docs.djangoproject.com/en/1.10/topics/http/views/

from .models import Petition
from .models import Signature

def petition_list(request):
    petitions = Petition.objects.all()
    return render(request, 'petition/petition_list.html', {'petitions': petitions})

def petition_detail(request, primary_key):
    petition = get_object_or_404(Petition, pk=primary_key)
    signatures = Signature.objects.filter(petition=1)
    return render(request, 'petition/petition_detail.html', {'petition': petition, 'signatures': signatures})
