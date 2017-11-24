# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from events.forms import TokenForm
from events.models import EventWorker, FBApplication
from events.parsers import EventParser
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
import logging

import urllib3.contrib.pyopenssl
import certifi, ssl
import facebook
import time, ast

urllib3.contrib.pyopenssl.inject_into_urllib3()


logger = logging.getLogger(__name__)

@login_required
def index(request):
    return HttpResponse('Maintenance section of the heltech site, currently: <a href="authorize">Authorizing the server</a> for facebook event access is all you can do. Site administration needs to remove the token, if needed.<br> Before authorization, a Facebook application details need to have inserted via the admin site by site admin.')

## page token elevation views
@login_required
def authorize(request):
    # get the app info
    try:
        app = FBApplication.objects.all()[0] # only one for now..
    except:
        return HttpResponse('Cannot authorize, a facebook application details need to be created through the admin site.')
    return render( request, "login.html", context={'app':app})


@login_required
def authorize_page(request):
    logger.info('authorize_page')
    form = TokenForm()
    return render(request, 'page_auth_form.html', {'form':form})

@login_required
def elevate_page_token(request):
    logger.info('elevate_page_token')
    if request.method == 'POST':
        try:
            app = FBApplication.objects.all()[0] # only one for now..
        except:
            return HttpResponse('You should not be here..')

        form = TokenForm(request.POST)
        if form.is_valid():
            user_token = form.cleaned_data['user_token']
        else:
            return render(request, 'page_auth_form.html', {'form':form})

        #maintenance: if there are other workers, delete them
        ews = EventWorker.objects.all().delete()
        
        # create the one we want
        ew = EventWorker(name='Heltech' + str(time.time()), user_token=user_token, page_name="heltech")
        
        #get the long-lived token
        https = urllib3.PoolManager(cert_reqs=str('CERT_REQUIRED'), ca_certs=certifi.where())
        params = "grant_type=fb_exchange_token&client_id=" + app.app_id
        params += "&client_secret=" + app.app_secret
        params += "&fb_exchange_token=" + user_token
        params += "&redirect_uri=https://shapemeal.cs.hut.fi/heltech/events/select/" + ew.name
        
        # need valid certs for this
        resp = https.request('GET', "https://graph.facebook.com/oauth/access_token?"+params)        
        
        respDict = ast.literal_eval(resp.data)
        ew.user_ll_token = respDict['access_token']
        ew.ll_expires = str(respDict['expires_in'])
        ew.save()

        return redirect('select_page', ew.name)

    else:
      	return HttpResponse('Invalid request, start from the events main page')


@login_required
def select_page(request, wname):
    if request.method == 'POST':
        page_id = request.POST['pageid']
        if page_id and wname:
            ew = EventWorker.objects.get(name=wname)
            ew.page_id = page_id
            https = urllib3.PoolManager(cert_reqs=str('CERT_REQUIRED'), ca_certs=certifi.where())
            resp = https.request('GET', "https://graph.facebook.com/me/accounts?access_token="+ew.user_ll_token)
            thedict = ast.literal_eval(resp.data)
            for page in thedict['data']:
                if page['id'] == page_id:
                    ew.page_name = page['name']
                    ew.page_token = page['access_token']
                    ew.user_token = ""
                    ew.save()

                    return HttpResponse("Worker successfully created.")
            return HttpResponse("Got empty list..")
            
    else:
        #get pages list
        if wname and wname != "":
            ew = EventWorker.objects.get(name=wname)
            https = urllib3.PoolManager(cert_reqs=str('CERT_REQUIRED'), ca_certs=certifi.where())
            resp = https.request('GET', "https://graph.facebook.com/me/accounts?access_token="+ew.user_ll_token)


            thedict = ast.literal_eval(resp.data)
        
            return render(request, "select_page.html", context={'data':thedict['data'],'name':ew.name})
        
## view for sending contact email.
