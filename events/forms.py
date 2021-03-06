# -*- coding: utf-8 -*-
from django.forms import ModelForm, CharField, HiddenInput, PasswordInput, Form
from events.models import EventWorker

class TokenForm(ModelForm):
    user_token = CharField(max_length=400, widget = HiddenInput(attrs={'autocomplete': 'off',}))
    
    class Meta:
        model = EventWorker
        fields = ['user_token']


# form for contacting the heltech crew
