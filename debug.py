import ipdb
from lib import *

# Test your code below...


r1 = Role("Programmer Kid")
r2 = Role("Bride")
r3 = Role("Joker")


a1 = Audition("Morgan", "NYC", True, r1)
a2 = Audition("Mike", "CO", False, r1)

a3 = Audition("Chandler", "NC", True, r2)
a4 = Audition("Raiza", "MT", True, r2)

a5 = Audition("Dan", "NC", False, r3)
a5 = Audition("Dan", "NC", False, r3)



# the below line allows us to stop & try stuff!
ipdb.set_trace()