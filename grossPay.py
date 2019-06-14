#Grosspay calc
valid = False

while valid != True:
    try:
        hours = int(raw_input('How many hours did you work? '))
        payrate = float(raw_input('What is your pay rate? '))
        grosspay = hours * payrate
        print 'Gross pay: $',format(grosspay, ',.2f')
        valid = True

    except ValueError:
        print 'Your pay must be an integer'
