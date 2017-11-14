class EventParser:
    def __init__(self, event):
        self.event = event

    def parse(self):
        self.description = self.parseDescription(self.event['description'])
        self.start_time = self.event['start_time']
        self.eid = self.event['id']
        self.title = self.parseName(self.event['name'])
        self.programme = self.parseProgram(self.event['description'])

        try:
            self.end_time = self.event['end_time']
        except KeyError:
            self.end_time = self.start_time
        
    def parseDescription(self, descr):
        return descr.split('PROGRAM:')[0]

    def parseName(self, descr):
        name = descr.split('-')  ## todo: always in the same format?
        if len(name) != 2:
            return name[0]
        else:
            return name[1]
        
    def parseProgram(self, descr):
        return descr.split('PROGRAM:')[1] ## todo, not finished, there are some final words usually


    
