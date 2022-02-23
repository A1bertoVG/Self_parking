import RPi.GPIO as GPIO 
import time


#GPIO.setwarnings(False)
#GPIO.cleanup()

GPIO.setmode (GPIO.BCM)

trig2 = 2
echo2 = 3

GPIO.setup(trig2, GPIO.OUT)
GPIO.setup(echo2, GPIO.IN)


    
def get_distance2():
    GPIO.output(trig2, False)
    time.sleep(0.000002)
    GPIO.output(trig2, True)
    time.sleep(0.0000010)
    GPIO.output(trig2, False)

    while GPIO.input(echo2) == False:
        start = time.time()

    while GPIO.input(echo2) == True:
        end = time.time()

    sig_time = end - start

    distance2 = 10*( sig_time/0.00058)
    #distance = (sig_time*0.034)/2
    #distance=sig_time*17150
    distance2=round(distance2,3)

    #print ('Distance: {} cm'.format(distance))
    return distance2


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