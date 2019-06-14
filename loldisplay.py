from sense_hat import SenseHat
import random
import time
random.seed()
sense = SenseHat()
while True:
    num1 = raw_input ('Enter a message')
    sense.show_message(num1)
    time.sleep (.5)
