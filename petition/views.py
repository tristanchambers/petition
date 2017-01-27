from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseForbidden
import csv
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    signatures = Signature.objects.filter(petition=primary_key)
    paginator = Paginator(signatures, 25) # Show 25 signatures per page

    num_signatures = len(signatures)

    # pagination logic
    page = request.GET.get('page')
    try:
        signatures = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        signatures = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        signatures = paginator.page(paginator.num_pages)

    # If this is a form submission, process the request
    # check if the user already signed the petition
    signed = request.session.get('has_signed', False)
    signer_name = request.session.get('signer_name', "")
    if request.method == "POST":
        if not signed:
            signform_data = SignatureForm(request.POST)
            if signform_data.is_valid():
                signature = signform_data.save(commit=False)
                signature.petition = petition
                signature.save()
                request.session['has_signed'] = True
                request.session['signer_name'] = signature.first_name
                signed = True
                signer_name = signature.first_name
    # Either way render the petition details
    signform = SignatureForm()
    goal_progress = len(signatures) * (100/petition.goal)
    return render(
        request,
        'petition/petition_detail.html',
        {
            'petition': petition,
            'signatures': signatures,
            'signform': signform,
            'signed': signed,
            'signer_name': signer_name,
            'num_signatures': num_signatures,
            'goal_progress': goal_progress,
        },
    )

def petition_csv(request, primary_key):
    if request.user.has_perm('petition.change_petition'):
        signatures = Signature.objects.filter(petition=primary_key)
        response = HttpResponse(content_type='text/csv')
        # TODO date.today().strftime("%Y-%m-%d")
        response['Content-Disposition'] = 'attachment; filename="petition.csv"'
        fieldnames = [
            'first_name',
            'last_name',
            'street_address',
            'city',
            'state',
            'email',
            'comment',
            'dont_show_name',
            'opt_in',
            ]
        writer = csv.DictWriter(response, fieldnames=fieldnames)
        writer.writeheader()
        for signature in signatures:
            writer.writerow({
                'first_name': signature.first_name,
                'last_name': signature.last_name,
                'street_address': signature.street_address,
                'city': signature.city,
                'state': signature.state,
                'email': signature.email,
                'comment': signature.comment,
                'dont_show_name': signature.dont_show_name,
                'opt_in': signature.opt_in,
            })
        return response
    else:
        return HttpResponseForbidden()
