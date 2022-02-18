# from ast import While
# from curses import echo
import RPi.GPIO as GPIO 
import time
import os
import cmd



GPIO.setwarnings(False)
GPIO.cleanup()

GPIO.setmode (GPIO.BCM)

trig = 4
echo = 17

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

def get_distance():
    GPIO.output(trig, True)
    time.sleep(0.0001)
    GPIO.output(trig, False)

    while GPIO.input(echo) == False:
        start = time.time()

    while GPIO.input(echo) == True:
        end = time.time()

    sig_time = end - start

    distance = 10*( sig_time/0.00058)
    #distance = sig_time/2

    print ('Distance: {} cm'.format(distance))
    return distance
try:

    while True:
        distance = get_distance()
        time.sleep(0.05)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    os.system("clear")
    print
    print("Programa terminado")
    print
    exit()

