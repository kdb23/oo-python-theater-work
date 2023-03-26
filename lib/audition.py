
class Audition:
    
  
    def __init__(self, actor, location):
        self.actor = actor
        self.location = location
        # self.hired = hired
        # self.role = role
        # role.auditions.append(self)
    
    def call_back(self):
        self.hired = True
    
# keeps throwing attribute error, eliminated hired in order to see if that 
# would solve this error issue but it does not. In addition states that 
# character_name must be a string as an attribute error as well