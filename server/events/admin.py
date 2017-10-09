# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Event, EventWorker

class EventAdmin(admin.ModelAdmin):
    fields = ['title', 'date_organised', 'description', 'speaker']
    list_display = ('title', 'date_organised')

class EventWorkerAdmin(admin.ModelAdmin):
    fields = ['name', 'update_freq']
    list_display = ('name', 'update_freq')
    
admin.site.register(Event, EventAdmin)
admin.site.register(EventWorker, EventWorkerAdmin)
