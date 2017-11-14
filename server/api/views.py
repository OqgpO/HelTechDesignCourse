# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from events.models import Event
from contacts.models import Speaker, Organisation
from api.serializers import *
from rest_framework import viewsets


from django.shortcuts import render

# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
    
class OrganisationViewSet(viewsets.ModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer

class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Organisation.objects.filter(is_partner=True)
    serializer_class = OrganisationSerializer
