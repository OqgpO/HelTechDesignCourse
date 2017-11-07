# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from events.forms import TokenForm
from events.models import EventWorker, FBApplication
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

import urllib3.contrib.pyopenssl
import certifi, ssl
import facebook
import time, ast

urllib3.contrib.pyopenssl.inject_into_urllib3()

@login_required
def index(request):
    return HttpResponse("Maintenance section of the heltech site")

def login(request):
    # get the app info
    app = FBApplication.objects.all()[0] # only one for now..
    
    
    return render( request, "login.html", context={'app':app})

#HttpResponse("Hello, world. You're at the events index.")

@login_required
def authorize_page(request):
    form = TokenForm()
    return render(request, 'page_auth_form.html', {'form':form})

@login_required
def elevate_page_token(request):
    if request.method == 'POST':
        form = TokenForm(request.POST)
        if form.is_valid():
            user_token = form.cleaned_data['user_token']
        else:
            return render(request, 'page_auth_form.html', {'form':form})

        
        #construct the call for elevation
        https = urllib3.PoolManager(cert_reqs=str('CERT_REQUIRED'), ca_certs=certifi.where())
        resp = https.request('GET', "https://graph.facebook.com/me/accounts?access_token="+user_token)
        print(resp.status)
        print(resp.data) 
        #graph = facebook.GraphAPI(access_token=ew.user_token, version="2.10")

        #events = graph.search(type='event')

        test_data = {
  "data": [
    {
      "category": "Product/service",
      "name": "Sample Page",
      "access_token": "{page-access-token}",
      "id": "1234567890",
      "perms": [
        "ADMINISTER",
        "EDIT_PROFILE",
        "CREATE_CONTENT",
        "MODERATE_CONTENT",
        "CREATE_ADS",
        "BASIC_ADMIN"
      ]
    },
      ]
}
        ew = EventWorker(name='Heltech' + str(time.time()), user_token=user_token, page_name="heltech")
        ew.save()

        thedict = ast.literal_eval(resp.data)
        
        return render(request, "select_page.html", context={'data':thedict['data'],'name':ew.name})

    return HttpResponse("Not a post!! should not get here")

@login_required
def select_page(request):
    if request.method == 'POST':
        page_id = request.POST['pageid']
        wname = request.POST['pagename']
        if page_id and wname:
            ew = EventWorker.objects.get(name=wname)
            ew.page_id = page_id
            https = urllib3.PoolManager(cert_reqs=str('CERT_REQUIRED'), ca_certs=certifi.where())
            resp = https.request('GET', "https://graph.facebook.com/me/accounts?access_token="+ew.user_token)
            print resp.data
            thedict = ast.literal_eval(resp.data)
            print thedict
            for page in thedict['data']:
                if page['id'] == page_id:
                    ew.page_name = page['name']
                    ew.page_token = page['access_token']
                    ew.user_token = ""
                    ew.save()

                    return HttpResponse("Worker successfully created.")
            return HttpResponse("Got empty list..")
            
    else:
        return HttpResponse("Not a post!! should not get here")
        
