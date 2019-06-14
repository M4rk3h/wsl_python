# Using python2, create a script
# which gets user input as raw_input
# and calculate their overall grade.

nbr1 = raw_input('Number 1 ')
nbr2 = raw_input('Number 2 ')
nbr3 = raw_input('Number 3 ')
avg = int (nbr1) + int (nbr2) + int (nbr3)
#print avg, (""),
dvd = avg / 3
#print dvd
if dvd >= 70:
    print 'Well Done, you have an A!!! Congrats!'
    
elif dvd >= 60:
    print 'Well Done, you have a B!!! Congrats!'

elif dvd >= 50:
    print 'Well Done, you have a C!'
    
elif dvd >= 40:
    print 'Well Done, passed!'

elif dvd >= 30:
    print 'You earned your self a resit'

else:
    print 'Go home, and study harder and longer ;)'
