#This program demonstrates an argument being
#passed to a function.

#This is a definition
def main():
    #This is the value, which needs user input
    value = int(raw_input('Enter A Value '))
    #This runs show_double
    show_double(value)

#The show_double function accepts an argument
#And displays double its value.

#This is the second definition
def show_double(number):
    #This is the second
    result = number * 2
    print 'Result is', result

#Call The Main Function

print 'Hi'
main()
print ''
print 'That is how functions work :D'
