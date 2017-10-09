
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Organisation(models.Model):
    name = models.CharField(max_length=200)
    site_address = models.URLField(max_length=400)
    logo = models.ImageField(upload_to='organisation_logos/')
    is_partner = models.BooleanField(default=False)

class Speaker(models.Model):
    full_name = models.CharField(max_length=200)
    introduction = models.TextField(max_length=2000)
    portrait = models.ImageField(upload_to='speaker_portraits/')
    organisation = models.ForeignKey(Organisation, null=True)
    


