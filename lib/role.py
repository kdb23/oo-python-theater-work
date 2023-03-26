from .audition import Audition

class Role:


    def __init__(self, character_name:str):
        self.character_name = character_name
    

#  returns all of the auditions associated with this role.
    @property
    def auditions(self):
        return [a for a in Audition.all if a.role == self]
    
# #     returns a list of names from the actors associated with this role.
    @property
    def actors(self):
        return [a.actor for a in self.auditions if a.role == self]
    
#     # returns a list of locations from the auditions associated with this role.
    @property
    def locations(self):
        return [l.location for l in self.auditions if l.role == self]
    
#     # returns the first instance of the audition that was hired for this role or 
#     # returns a string 'no actor has been hired for this role'.