import RPi.GPIO as GPIO 
import time


GPIO.setwarnings(False)
GPIO.cleanup()

GPIO.setmode (GPIO.BCM)

trig1 = 14
echo1 = 4

trig2 = 2
echo2 = 3

trig3 = 18
echo3 = 15

trig4 = 24
echo4 = 23

#trig5
#echo5


GPIO.setup(trig1, GPIO.OUT)
GPIO.setup(echo1, GPIO.IN)
GPIO.setup(trig2, GPIO.OUT)
GPIO.setup(echo2, GPIO.IN)
GPIO.setup(trig3, GPIO.OUT)
GPIO.setup(echo3, GPIO.IN)
GPIO.setup(trig4, GPIO.OUT)
GPIO.setup(echo4, GPIO.IN)


    
def get_distanceF():
    GPIO.output(trig1, False)
    time.sleep(0.000002)
    GPIO.output(trig1, True)
    time.sleep(0.0000010)
    GPIO.output(trig1, False)

    while GPIO.input(echo1) == False:
        start1 = time.time()

    while GPIO.input(echo1) == True:
        end1 = time.time()

    sig_time1 = end1 - start1

    distanceF = 10*( sig_time1/0.00058)
    #distance = (sig_time*0.034)/2
    #distance=sig_time*17150
    distanceF=round(distanceF,3)

    print ('Distance: {} cm'.format(distanceF))
    return distanceF

'''
while True:

    distanceF = get_distanceF()
    time.sleep(0.5)
'''
'''
def dis_continua():
    while True:

        distanceF = get_distanceF()
        time.sleep(0.05)


def main():
    get_distanceF()
    dis_continua()


if __name__ == "__main__":
    main()


'''