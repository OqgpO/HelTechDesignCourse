import re

class EventParser:
    def __init__(self, event, parse_speakers=False):
        self.event = event
        self.parse_speakers = parse_speakers

    def parse(self):
        self.description = self.parseDescription(self.event['description'])
        self.start_time = str(self.event['start_time'])
        self.eid = self.event['id']
        self.title = self.parseName(self.event['name'])
        self.programme = self.parseProgram(self.event['description'])

        if self.parse_speakers:
            self.speakers = self.parseSpeakers(self.programme)

        try:
            self.place = self.event['place']['name']
            self.addr = self.event['place']['location']['street']
        except KeyError:
            self.place = ""
            self.addr = ""


        try:
            self.end_time = str(self.event['end_time'])
        except KeyError:
            self.end_time = self.start_time
        
    def parseDescription(self, descr):
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
                    self.punchline = line
                    ret.replace(line, '', 1)
                    break

        return ret


    def parseName(self, descr):
        name = descr.split('-')  ## todo: always in the same format?
        if len(name) != 2:
            return name[0]
        else:
            return name[1]
        
    def parseProgram(self, descr):
        try:
            ret = descr.split('PROGRAM:')[1] 
        except KeyError:
            ret = "" # needs to be hand filled

        return ret


    def parseSpeakers(self, program):
        speakers = []
        curr_role = ""
        lines = program.split('\n')
        for line in lines:
            if re.match(r'^[0-9][0-9].[0-9][0-9]', line):
                curr_role = line[line.index(" ")+1:]
            elif line != '':
                if re.search('keynote', curr_role, re.IGNORECASE): #person
                    person_line = line.split(',') #<name>,<title>,<org> for now!
                    if len(person_line) != 3:
                        continue # do not even try special cases..
                    else:
                        speakers.append( {'role':'KN', 
                                          'name':person_line[0],
                                          'title':person_line[1],
                                          'org':person_line[2] } )
                elif re.search('panel', curr_role, re.IGNORECASE): #persons
                    person_line = line.split(',') #<name>,<title>,<org> for now!
                    if len(person_line) == 2:
                        speakers.append( {'role':'PA', 
                                          'name':person_line[0],
                                          'title':person_line[1],
                                          'org': ""} )
                    elif len(person_line) == 3:
                        speakers.append( {'role':'PA', 
                                          'name':person_line[0],
                                          'title':person_line[1],
                                          'org':person_line[2] } )
                elif (re.search('demo', curr_role, re.IGNORECASE) or 
                      re.search('pitch', curr_role, re.IGNORECASE)): #Organisations only
                    speakers.append( {'role':'DE',
                                      'name':"",
                                      'title':"",
                                      'org':line })

        return speakers
