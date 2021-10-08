from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Meetup, Location, Participant
from .forms import RegistrationForm
# Create your views here.


def confirmation_page(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/confirmation-page.html', {
        'organizer_email': meetup.organizer_email
    })

def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {
        'meetups': meetups
    })

def meetup_details(request, meetup_slug):
    print("*******************************************************************")
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)

        if request.method == 'GET':
            registration_form = RegistrationForm()
            
            
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirmation-page', meetup_slug=meetup_slug)

        return render(request, 'meetups/meetup-details.html', {
                'meetup': selected_meetup,
                'meetup_found': True,
                'form': registration_form
                })
        

    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        })

