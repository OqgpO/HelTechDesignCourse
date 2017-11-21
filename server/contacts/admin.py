# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Speaker, Organisation

class SpeakerAdmin(admin.ModelAdmin):
    #fields = ['full_name', 'introduction', 'portrait', 'organisation']
    list_display = ['full_name']

class OrganisationAdmin(admin.ModelAdmin):
    #fields = ['name', 'site_address', 'logo']
    list_display = ('name', 'site_address')
    
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Organisation, OrganisationAdmin)
