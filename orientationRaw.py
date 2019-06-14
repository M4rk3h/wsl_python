from sense_hat import SenseHat
sense = SenseHat()

while True:
    pitch, roll, yaw = sense.get_accelerometer_raw().values()
    print"pitch=%s, roll=%s, yaw=%s" % (round(pitch,1), round(yaw,1), round(roll,1))
