
class Audition:
    
    all = []
  
    def __init__(self, actor, location, hired, role):
        self.actor = actor
        self.location = location
        self.hired = hired
        self.role = role
        Audition.all.append(self)
    
    def call_back(self):
        self.hired = True
    
