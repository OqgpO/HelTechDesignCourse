# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=1000)
    streetaddr = models.CharField(max_length=1000, blank=True)

class Event(models.Model):
    title = models.CharField(max_length=1000)
    start_time = models.DateTimeField('date organised')
    end_time = models.DateTimeField('date organised')
    eid = models.CharField(max_length=400)
    punchline = models.CharField(max_length=400, blank=True)
    description = models.TextField(max_length=2000)
    programme = models.TextField(max_length=2000, blank=True)
    attending_count = models.IntegerField(blank=True, null=True)
    cover_uri = models.URLField(max_length=1000, blank=True)
    place = models.ForeignKey(Place, null=True, blank=True)

    def __unicode__(self):
        return self.title
    
class EventWorker(models.Model):
    user_token = models.CharField(max_length=400, blank=True)
    user_ll_token =  models.CharField(max_length=400, blank=True)
    ll_expires = models.CharField(max_length=400, blank=True)
    page_token = models.CharField(max_length=400, blank=True)
    name = models.CharField(max_length=200)
    page_name = models.CharField(max_length=200)
    page_id = models.CharField(max_length=200)
    parse_speakers = models.BooleanField(default=False)

    
class FBApplication(models.Model):
    name = models.CharField(max_length=400)
    app_id = models.CharField(max_length=400)
    app_secret = models.CharField(max_length=400)

    
