import RPi.GPIO as GPIO 
import time


#GPIO.setwarnings(False)
#GPIO.cleanup()

GPIO.setmode (GPIO.BCM)

trig3 = 18
echo3 = 15

GPIO.setup(trig3, GPIO.OUT)
GPIO.setup(echo3, GPIO.IN)


    
def get_distance3():
    GPIO.output(trig3, False)
    time.sleep(0.000002)
    GPIO.output(trig3, True)
    time.sleep(0.0000010)
    GPIO.output(trig3, False)

    while GPIO.input(echo3) == False:
        start = time.time()

    while GPIO.input(echo3) == True:
        end = time.time()

    sig_time = end - start

    distance3 = 10*( sig_time/0.00058)
    #distance = (sig_time*0.034)/2
    #distance=sig_time*17150
    distance3=round(distance3,3)

    #print ('Distance: {} cm'.format(distance))
    return distance3


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