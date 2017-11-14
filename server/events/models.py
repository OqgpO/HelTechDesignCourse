# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from contacts.models import Speaker

class Event(models.Model):
    title = models.CharField(max_length=1000)
    start_time = models.DateTimeField('date organised')
    end_time = models.DateTimeField('date organised', blank=True)
    eid = models.CharField(max_length=400)
    description = models.TextField(max_length=2000)
    speaker = models.ForeignKey(Speaker, null=True, blank=True)
    programme = models.TextField(max_length=2000, blank=True)
    attending_count = models.IntegerField(blank=True)
    cover_uri = models.URLField(max_length=1000, blank=True)
    
class EventWorker(models.Model):
    user_token = models.CharField(max_length=400, blank=True)
    user_ll_token =  models.CharField(max_length=400, blank=True)
    ll_expires = models.CharField(max_length=400, blank=True)
    page_token = models.CharField(max_length=400, blank=True)
    name = models.CharField(max_length=200)
    page_name = models.CharField(max_length=200)
    page_id = models.CharField(max_length=200)

    
class FBApplication(models.Model):
    name = models.CharField(max_length=400)
    app_id = models.CharField(max_length=400)
    app_secret = models.CharField(max_length=400)

    
