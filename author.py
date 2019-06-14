# Using python2, create a script
# which gets user input as text
# and ints, to calculate their age
# in days and hours.

name = raw_input('What is your name? ')
age = raw_input('How old are you? ')
place = raw_input('Where do you live? ')
int (age)
AgeInDays = int(age) * 365
AgeInHours = AgeInDays * 24
print 'The author of this programme is',name, 'who is',age, 'years old,',AgeInDays,'days old and,',AgeInHours, 'hours old and lives in', place
