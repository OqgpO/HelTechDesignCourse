from django_cron import CronJobBase, Schedule
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from events.models import EventWorker, Event, Place
from contacts.models import Speaker, Organisation
from events.parsers import EventParser
import datetime, pytz
from dateutil import parser

import facebook

import logging
logger = logging.getLogger(__name__)

## class for the django-cron. do method is ran every two hours
class FB(CronJobBase):
    RUN_EVERY_MINS = 120 # every 2 hours
    DJANGO_CRON_DELETE_LOGS_OLDER_THAN = 30 #30 days of logs

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'events.tasks.FB'    # a unique code

    def do(self):
        logger.debug("cron job starting for: FB")

        #get the event worker for heltech
        try:
            ew = EventWorker.objects.get(page_name = "HEL Tech") #assume one worker for hel tech
            
        except ObjectDoesNotExist:
            logger.error("No event workers configured, cannot check events!")
            return
        except MultipleObjectsReturned:
            logger.error("Multiple workers found, do not know which one to run yet!")
            return
        
        graph = facebook.GraphAPI(access_token=ew.page_token, version="2.1")

        #get the page events and the database events
        fb_events = graph.get_connections(id=ew.page_id, connection_name="events")        
        db_events = Event.objects.all()

        for event in fb_events['data']:
            try:
                e = Event.objects.get(eid=event['id'])
            except ObjectDoesNotExist:
                e = Event()
                
            ep = EventParser(event, ew.parse_speakers)
            ep.parse()
                
            #exists, lets update the participant count
            ac = graph.get_object(id=event['id'], fields='attending_count')
            e.attending_count = ac['attending_count'] or 0
                    
            # fetch the cover photo
            cover = graph.get_object(id=event['id'], fields=['cover'])
                
            try:
                e.cover_uri = cover['cover']['source']
            except KeyError:
                e.cover_uri = ""

            # fill in the data
            e.eid=ep.eid
            e.title=ep.title
            e.start_time=ep.start_time
            e.end_time=ep.end_time
            e.programme=ep.programme
            e.description=ep.description 
            e.punchline=ep.punchline
            
            #add the place
            try:
                p = Place.objects.get(name=ep.place)
            except ObjectDoesNotExist:
                p = Place()
                
            p.name=ep.place
            p.streetaddr=ep.addr
            
            p.save()
            e.place=p

            e.save() #that's all for now

            # fill the speakers
            if ew.parse_speakers:
                edt = parser.parse(e.start_time)
                now = datetime.datetime.now(edt.tzinfo)
                
                if edt >= now or (not Speaker.objects.filter(event__eid=e.eid).exists()):
                    (count, thedict) = speakers = Speaker.objects.filter(event__eid=e.eid).delete()
                    logger.debug("deleted: " + str(count) + " speakers, details: " + str(thedict))
                    for speaker in ep.speakers:
                        org = None
                        sobj = Speaker()

                        if speaker['org']:
                            try:
                                org = Organisation.objects.get(name=speaker['org'])
                            except ObjectDoesNotExist:
                                org = Organisation()
                             

                            org.name=speaker['org']
                            org.save()
                    
                        speaker = Speaker(full_name=speaker['name'],
                                          title=speaker['title'],
                                          role=speaker['role'],
                                          organisation=org,
                                          event=e)
                        speaker.save()
                        
                   
            
                        
