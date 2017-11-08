# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from events.forms import TokenForm
from events.models import EventWorker, FBApplication
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
import logging

import urllib3.contrib.pyopenssl
import certifi, ssl
import facebook
import time, ast

urllib3.contrib.pyopenssl.inject_into_urllib3()


logger = logging.getLogger(__name__)

@login_required
def index(request):
    return HttpResponse("Maintenance section of the heltech site")

def login(request):
    logger.info('login')
    # get the app info
    app = FBApplication.objects.all()[0] # only one for now..
    
    
    return render( request, "login.html", context={'app':app})

#HttpResponse("Hello, world. You're at the events index.")

@login_required
def authorize_page(request):
    logger.info('authorize_page')
    form = TokenForm()
    return render(request, 'page_auth_form.html', {'form':form})

@login_required
def elevate_page_token(request):
    logger.info('elevate_page_token')
    if request.method == 'POST':
        app = FBApplication.objects.all()[0] # only one for now..

        form = TokenForm(request.POST)
        if form.is_valid():
            user_token = form.cleaned_data['user_token']
        else:
            return render(request, 'page_auth_form.html', {'form':form})

        
        #get the long-lived token
        https = urllib3.PoolManager(cert_reqs=str('CERT_REQUIRED'), ca_certs=certifi.where())
        params = "grant_type=fb_exchenge_token&client_id=" + app.app_id
        params += "&client_secret=" + app.app_secret
        params += "&fb_exchange_token=" + user_token
        resp = https.request('GET', "https://graph.facebook.com/oauth/access_token?"+params)
        
        logger.info( "params: " + params )
        logger.info( "status: " + resp.status)
        logger.info( "response" + resp.data )
        
        
        
        #construct the call for elevation
        resp = https.request('GET', "https://graph.facebook.com/me/accounts?access_token="+user_token)
        #graph = facebook.GraphAPI(access_token=ew.user_token, version="2.10")

        #events = graph.search(type='event')

        ew = EventWorker(name='Heltech' + str(time.time()), user_token=user_token, page_name="heltech")
        ew.save()

        thedict = ast.literal_eval(resp.data)
        
        return render(request, "select_page.html", context={'data':thedict['data'],'name':ew.name})

    return HttpResponse("Not a post!! should not get here")

@login_required
def select_page(request):
    logger.info('select_page')
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
        
