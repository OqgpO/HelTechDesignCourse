# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from contacts.models import Speaker

class Event(models.Model):
    title = models.CharField(max_length=1000)
    date_organised = models.DateTimeField('date organised')
    description = models.TextField(max_length=2000)
    speaker = models.ForeignKey(Speaker, null=True)

class EventWorker(models.Model):
    user_token = models.CharField(max_length=400, blank=True)
    page_token = models.CharField(max_length=400, blank=True)
    name = models.CharField(max_length=200)
    page_name = models.CharField(max_length=200)
    page_id = models.CharField(max_length=200)
    
class FBApplication(models.Model):
    name = models.CharField(max_length=400)
    app_id = models.CharField(max_length=400)
    app_secret = models.CharField(max_length=400)

    
