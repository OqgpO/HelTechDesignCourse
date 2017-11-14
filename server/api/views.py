# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from events.models import Event
from contacts.models import Speaker, Organisation
from api.serializers import *
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import datetime
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import render

# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-start_time')
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

@csrf_exempt
@api_view(['GET'])
def pastEvents(request, limit=None):
    if request.method=='GET':
        if limit == None:
            events = event.objects.filter(start_time__lt=timezone.now()).order_by('-start_time')
        else:
            try:
                events = event.objects.filter(start_time__lt=timezone.now()).order_by('-start_time')[:limit]
            except IndexError:
                events = event.objects.filter(start_time__lt=timezone.now()).order_by('-start_time')
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

        
        serializer = EventSerializer(events, many=events.len()!=1)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(['GET'])
def futureEvents(request, limit=None):
    if request.method=='GET':
        if limit == None:
            events = event.objects.filter(start_time__gte=timezone.now()).order_by('+start_time')
        else:
            try:
                events = event.objects.filter(start_time__gte=timezone.now()).order_by('+start_time')[:limit]
            except IndexError:
                events = event.objects.filter(start_time__gte=timezone.now()).order_by('+start_time')
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

        
        serializer = EventSerializer(events, many=events.len()!=1)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@api_view(['GET'])
def currentEvent(request):
    if request.method=='GET':
        now = timezone.now()
        event = Event.objects.filter(start_time__gte=now).order_by('+start_time')
        if not event:
            event = Event.objects.filter(start_time__lte=now).order_by('-start_time')
            if not event:
                return Response(status=status.HTTP_404_NOT_FOUND)


        serializer = EventSerializer(event[0], many=False)
        return Response(serializer.data)

    return Response(status=status.HTTP_404_NOT_FOUND)
