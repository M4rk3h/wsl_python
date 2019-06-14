# Using python2, create a script
# which simulates dice rolls.

import random
import time
random.seed()

for x in range(1,11):
    result1 = random.randint(1,6)
    result2 = random.randint(1,6)
    
    print 'You rolled a ' + str(result1) + ' and a ' + str(result2)
    
    time.sleep(.5)
