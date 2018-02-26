
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from heltech import settings
from django.db import models
from events.models import Event

default_portrait = settings.STATIC_URL + "img/man-235.png"

class Organisation(models.Model):
    name = models.CharField(max_length=200)
    site_address = models.URLField(max_length=400, blank=True)
    logo = models.ImageField(upload_to='organisation_logos/', blank=True)
    is_partner = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    
class Speaker(models.Model):
    full_name = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=400, blank=True);
    introduction = models.TextField(max_length=2000, blank=True)
    portrait = models.ImageField(upload_to='speaker_portraits/', default=default_portrait)
    organisation = models.ForeignKey(Organisation, null=True)
    event = models.ForeignKey(Event, related_name='speakers', null=True, blank=True)

    ROLE_CHOICES = (
    ('KN', 'Keynote speaker'),
    ('PA', 'Panelist'),
    ('DM', 'Demo presenter'),
    )
    role = models.CharField(max_length=2, blank=True, choices=ROLE_CHOICES)

    def get_organisation_name(self, obj):
        return obj.organisation.name or ""
    get_organisation_name.admin_order_field  = 'organisation'  #Allows column order sorting
    get_organisation_name.short_description = 'Organisation Name'  #Renames column head

    def __unicode__(self):
        if not self.full_name:
            return self.organisation.name;
        else:
            return self.full_name

    def __str__(self):
        if not self.full_name:
            return self.organisation.name;
        else:
            return self.full_name
