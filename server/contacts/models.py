
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from heltech import settings
from django.db import models
from events.models import Event

default_portrait = settings.STATIC_ROOT + "/img/man-235.png"

class Organisation(models.Model):
    name = models.CharField(max_length=200)
    site_address = models.URLField(max_length=400, blank=True)
    logo = models.ImageField(upload_to='organisation_logos/', blank=True)
    is_partner = models.BooleanField(default=False)

class Speaker(models.Model):
    full_name = models.CharField(max_length=200)
    title = models.CharField(max_length=400, blank=True);
    introduction = models.TextField(max_length=2000, blank=True)
    portrait = models.ImageField(upload_to='speaker_portraits/', default=default_portrait)
    organisation = models.ForeignKey(Organisation, null=True)
    event = models.ForeignKey(Event, null=True, blank=True)

    ROLE_CHOICES = (
    ('KN', 'Keynote speaker'),
    ('PA', 'Panelist'),
    ('DM', 'Demo presenter'),
    )
    role = models.CharField(max_length=2, blank=True, choices=ROLE_CHOICES)


