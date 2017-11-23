from django_cron import CronJobBase, Schedule
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from events.models import EventWorker, Event, Place
from contacts.models import Speaker, Organisation
from events.parsers import EventParser
import datetime


import facebook

import logging
logger = logging.getLogger(__name__)

class FB(CronJobBase):
    RUN_EVERY_MINS = 120 # every 2 hours

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

        #get the page events
        
        fb_events = graph.get_connections(id=ew.page_id, connection_name="events")
        logger.debug("All events fetched, result:\n" + str(fb_events))
        
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
            cover = graph.get_object(id=e.eid, fields=['cover'])
                
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
            if ep.place and ep.addr:
                try:
                    p = Place.objects.get(name=ep.place)
                except ObjectDoesNotExist:
                    p = Place()
                    
                p.name=ep.place
                p.streetaddr=ep.place
                
                p.save()
                e.place=p

            e.save() #that's all for now

            # fill the speakers
            if ew.parse_speakers:
                now = datetime.datetime.now()
                if e.start_time >= now:
                    (count, dict) = speakers = Speaker.objects.filter(event__eid=e.eid).delete()
                    logger.debug("deleted: " + str(count), " speakers, details: " + str(dict))
                    for speaker in ep.speakers:
                        sobj = None
                        org = None
                    sobj = Speaker()

                    if speaker['org']:
                        try:
                            org = Organisation.objects.get(name=speaker['org'])
                        except ObjectDoesNotExist:
                            org = Organisation()
                             
                    if speaker['org']:
                        org.name=speaker['org']
                        org.save()
                    
                    speaker = Speaker(full_name=speaker['name'],
                                      title=speaker['title'],
                                      role=speaker['role'],
                                      organisation=org,
                                      event=e)
                    speaker.save()
                        
                   
            
                        
