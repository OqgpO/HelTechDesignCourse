class EventParser:
    def __init__(self, event):
        self.event = event

    def parse(self):
        self.description = self.parseDescription(self.event['description'])
        self.start_time = self.event['start_time']
        self.end_time = self.event['end_time']
        self.eid = self.event['id']
        self.title = self.parseName(self.event['name'])
        self.program = self.parseProgram(self.event['description'])
        
    def parseDescription(self, descr):
        return descr.split('PROGRAM:')[0]

    def parseName(self, descr):
        return descr.split(' - ')[1]  ## todo: always in the same format?

    def parseProgram(self, descr):
        return descr.split('PROGRAM:')[1] ## todo, not finished, there are some final words usually


    
