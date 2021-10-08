from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='all-meetups'),  # our-domain.com/meetups
    path('<slug:meetup_slug>/confirmation', views.confirmation_page, name='confirmation-page'),
    path('<slug:meetup_slug>', views.meetup_details, name='meetup-detail') # our-domain.com/meetups/<dinamic-path-segment>
    
]