from .audition import Audition

class Role:


    def __init__(self, character_name):
        self.character_name = character_name
    
#  returns all of the auditions associated with this role.
    @property
    def auditions(self):
        return [a for a in Audition.all if a.role == self]
    
# #     returns a list of names from the actors associated with this role.
    @property
    def actors(self):
        return [a.actor for a in self.auditions]
    
#     # returns a list of locations from the auditions associated with this role.
    @property
    def locations(self):
        return [l.location for l in self.auditions]
    
#     # returns the first instance of the audition that was hired for this role or 
#     # returns a string 'no actor has been hired for this role'.
    @property
    def lead(self):
        role_lead = "no actor has been hired for this role"
        for role in self.auditions:
           if role.hired == True:
               role_lead = role.actor
               return role_lead
        else:
            return role_lead
        

#   returns the second instance of the audition that was hired for this role or 
#   returns a string 'no actor has been hired for understudy for this role'.

    @property
    def understudy(self):
        support = [a.actor for a in self.auditions if a.hired]
        wish_me_luck = "no actor has been hired for understudy for this role"
        if len(support) > 1:
            return support[1]
        else:
            return wish_me_luck
