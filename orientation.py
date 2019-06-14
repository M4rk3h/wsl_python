from sense_hat import SenseHat
sense = SenseHat()

while True:
    pitch, roll, yaw = sense.get_orientation().values()
    print"pitch=%s, roll=%s, yaw=%s" % (round(pitch,2), round(yaw,2), round(roll,2))
