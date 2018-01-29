# coding=utf-8
from __future__ import unicode_literals
import re

class EventParser:
    """
    Parser class for fb events.
    """
    def __init__(self, event, parse_speakers=False):
        self.event = event
        self.parse_speakers = parse_speakers

    def parse(self):
        """
        parse event data loaded in the class
        """
        self.description = self.parseDescription(self.event['description']).strip()
        self.start_time = self.event['start_time'].strip()
        self.eid = self.event['id']
        self.title = self.parseName(self.event['name']).strip()
        self.programme = self.parseProgram(self.event['description']).strip()

        if self.parse_speakers:
            self.speakers = self.parseSpeakers(self.programme)

        try:
            self.place = self.event['place']['name'].strip()
            self.addr = self.event['place']['location']['street'].strip()
        except KeyError:
            self.place = ""
            self.addr = ""


        try:
            self.end_time = self.event['end_time']
        except KeyError:
            self.end_time = self.start_time
        
    def parseDescription(self, descr):
        """
        Parse description of event from its main components
        :param descr: event description string
        :return: the description of the event, without program
        """
        try:
            ret = descr.split('PROGRAM:')[0]
        except KeyError:
            ret = descr

        #get the punchline
        lines = descr.split('\n')
        for line in lines:
            if line == '':
                continue
            else:
                if line.isupper():
                    self.punchline = line.strip()
                    ret=ret.replace(self.punchline, "", 1)
                    break                
                else:
                    self.punchline = ""
                    break

        return ret


    def parseName(self, descr):
        """
        Event name parser
        :param descr: event description string
        :return: the name parsed
        """
        name = descr.split('-')  ## todo: always in the same format?
        if len(name) != 2:
            return name[0].strip()
        else:
            return name[1].strip()
        
    def parseProgram(self, descr):
        """
        Parse program from event string
        :param descr: the description string
        :return: the program that was parsed
        """
        try:
            ret = descr.split('PROGRAM:')[1].strip() 
        except KeyError:
            ret = "" # needs to be hand filled

        return ret


    def parseSpeakers(self, program):
        """
        Parse speakers from program string
        :param program: program to be parsed
        :return: dict of the speakers
        """
        speakers = []
        curr_role = ""
        lines = program.split('\n')
        for line in lines:
            if re.match(r'^[0-9][0-9].[0-9][0-9]', line):
                curr_role = line[line.index(" ")+1:]
            elif line != '':
                if re.search('keynote', curr_role, re.IGNORECASE): #person
                    person_line = line.split(',') #<name>,<title>,<org> for now!                   

                    if len(person_line) == 2:
                        if len(person_line[0]) < 30: #try to control the wild texts
                            speakers.append( {'role':'KN', 
                                              'name':person_line[0].strip(),
                                              'title':person_line[1].strip(),
                                              'org': ""} )
                    elif len(person_line) == 3:
                        speakers.append( {'role':'KN', 
                                          'name':person_line[0].strip(),
                                          'title':person_line[1].strip(),
                                          'org':person_line[2].strip() } )
                    elif (len(person_line)==1 and 
                          person_line[0].find('(') >= 0  and 
                          person_line[0].find(')') >= 0):   # notation for <person>(org)
                        person_line = line.split('(')
                        speakers.append( {'role':'KN', 
                                          'name':person_line[0].strip(),
                                          'org':person_line[1].strip().replace(')','',1) } )
                        

                elif re.search('panel', curr_role, re.IGNORECASE): #persons
                    person_line = line.split(',') #<name>,<title>,<org> for now!
                    if len(person_line) == 2:
                        if len(person_line[0]) < 30:  #try to control the wild texts
                            speakers.append( {'role':'PA', 
                                              'name':person_line[0].strip(),
                                              'title':person_line[1].strip(),
                                              'org': ""} )
                    elif len(person_line) == 3:
                        speakers.append( {'role':'PA', 
                                          'name':person_line[0].strip(),
                                          'title':person_line[1].strip(),
                                          'org':person_line[2].strip() } )
                    elif (len(person_line)==1 and 
                          person_line[0].find('(') >= 0  and 
                          person_line[0].find(')') >= 0):   # notation for <person>(org)
                        person_line = line.split('(')
                        speakers.append( {'role':'PA', 
                                          'name':person_line[0].strip(),
                                          'org':person_line[1].strip().replace(')','',1) } )



                elif (re.search('demo', curr_role, re.IGNORECASE) or 
                      re.search('pitch', curr_role, re.IGNORECASE)): #Organisations only
                    speakers.append( {'role':'DE',
                                      'name':"",
                                      'title':"",
                                      'org':line.strip() })

        return speakers
