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
    page_token = models.CharField(max_length=200)
    update_freq = models.BigIntegerField()
    name = models.CharField(max_length=200)
