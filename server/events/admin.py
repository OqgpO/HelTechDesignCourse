# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Event, EventWorker, FBApplication, Place

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'streetaddr')


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time')

class EventWorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'page_name')
    

class FBApplicationAdmin(admin.ModelAdmin):
    fields = ['name','app_id','app_secret']
    list_display = ('name', 'app_id')



admin.site.register(Event, EventAdmin)
admin.site.register(EventWorker, EventWorkerAdmin)
admin.site.register(FBApplication, FBApplicationAdmin)
admin.site.register(Place, PlaceAdmin)
