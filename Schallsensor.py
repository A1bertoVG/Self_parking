import RPi.GPIO as GPIO 
import time


GPIO.setwarnings(False)
GPIO.cleanup()

GPIO.setmode (GPIO.BCM)

trig = 14
echo = 4

#trig = 18
#echo = 15

#trig = 2
#echo = 3

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)


    
def get_distance():
    GPIO.output(trig, False)
    time.sleep(0.000002)
    GPIO.output(trig, True)
    time.sleep(0.0000010)
    GPIO.output(trig, False)

    while GPIO.input(echo) == False:
        start = time.time()

    while GPIO.input(echo) == True:
        end = time.time()

    sig_time = end - start

    distance = 10*( sig_time/0.00058)
    #distance = (sig_time*0.034)/2
    #distance=sig_time*17150
    distance=round(distance,3)

#    print ('Distance: {} cm'.format(distance))
    return distance


'''
while True:
    distance = get_distance()
    time.sleep(0.05)
'''



'''
def dis_continua():
    while True:
        distance = get_distance()
        time.sleep(0.05)


def main():
    get_distance()
    dis_continua()


if __name__ == "__main__":
    main()


'''
