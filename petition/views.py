from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseForbidden
import csv
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# https://docs.djangoproject.com/en/1.10/topics/http/views/

from .models import Petition
from .models import Signature
from .forms import SignatureForm

COMMON_FIELDS = [
        'title',
        'hero_image',
        'address_to',
        'teaser_text',
        'description',
        'letter',
        'thank_you_message',
        'goal',
        'region_city',
        'region_state',
]


def home(request):
    return render(request, 'petition/home.html', {'body_id': "home-page"})

class Petitions(ListView):
    model = Petition

def petition_list(request):
    petitions = Petition.objects.all()
    return render(request, 'petition/petition_list.html', {'petitions': petitions})

class PetitionCreate(LoginRequiredMixin, CreateView):
    model = Petition
    fields = COMMON_FIELDS
    fields.append('slug')
#    fields.append('created_by')

    def form_valid(self, form):
        petition = form.save(commit=False)
        petition.created_by = self.request.user
        petition.save()
        return HttpResponseRedirect(petition.get_absolute_url())

class PetitionUpdate(LoginRequiredMixin, UpdateView):
    model = Petition
    fields = COMMON_FIELDS

class PetitionDelete(LoginRequiredMixin, DeleteView):
    model = Petition
    success_url = '/' # TODO: pick a better location for post-delete landing

def petition_detail(request, slug):
    petition = get_object_or_404(Petition, slug=slug)
    primary_key = petition.pk
    signatures = Signature.objects.filter(petition=primary_key).order_by('-created_date')
    signatures_local = Signature.objects.filter(petition=primary_key,city=petition.region_city)
    paginator = Paginator(signatures, 25) # Show 25 signatures per page

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
    sign_event = False
    if request.method == "POST":
        if not signed:
            signform = SignatureForm(request.POST)
            if signform.is_valid():
                signature = signform.save(commit=False)
                signature.petition = petition
                signature.save()
                request.session['has_signed'] = True
                request.session['signer_name'] = signature.first_name
                signed = True
                sign_event = True
                signer_name = signature.first_name

    # Either way render the petition details
    else:
        signform = SignatureForm()
    goal_progress = len(signatures) * (100/petition.goal)
    return render(
        request,
        'petition/petition_detail.html',
        {
            'petition': petition,
            'signatures': signatures,
            'signatures_local': signatures_local,
            'signform': signform,
            'signed': signed,
            'signer_name': signer_name,
            'goal_progress': goal_progress,
            'sign_event': sign_event,
        },
    )

def petition_csv(request, slug):
    petition = get_object_or_404(Petition, slug=slug)
    primary_key = petition.pk
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
