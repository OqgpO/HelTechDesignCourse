# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Event, EventWorker, FBApplication

class EventAdmin(admin.ModelAdmin):
    fields = ['title', 'date_organised', 'description', 'speaker']
    list_display = ('title', 'date_organised')

class EventWorkerAdmin(admin.ModelAdmin):
    fields = ['name','page_name', 'page_id', 'page_token','user_token']
    list_display = ('name', 'page_name')
    

class FBApplicationAdmin(admin.ModelAdmin):
    fields = ['name','app_id','app_secret']
    list_display = ('name', 'app_id')



admin.site.register(Event, EventAdmin)
admin.site.register(EventWorker, EventWorkerAdmin)
admin.site.register(FBApplication, FBApplicationAdmin)
