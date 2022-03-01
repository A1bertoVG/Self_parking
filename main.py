#Main code

import cmd
import Schallsensor
import Schallsensor2
import Schallsensor3
import rasp_motors
import time 


def place_found():
    rasp_motors.dir_foward()
    rasp_motors.vel_foward()

    time.sleep(5)

    rasp_motors.pwm_a.ChangeDutyCycle(0)
    rasp_motors.pwm_b.ChangeDutyCycle(0)
    time.sleep(3)
    rasp_motors.park()
    print("Parked")

def place_found2():
    rasp_motors.dir_foward()
    rasp_motors.vel_foward()
    if (distance2 <= 10):
        rasp_motors.pwm_a.ChangeDutyCycle(0)
        rasp_motors.pwm_b.ChangeDutyCycle(0)
        time.sleep(2)
        rasp_motors.park()
        return 




print("Empezando programa")
time.sleep(3)


        

while True:
    rasp_motors.dir_foward()
    rasp_motors.vel_foward()
    distance = Schallsensor.get_distance()
    distance2 = Schallsensor2.get_distance2()
    distance3 = Schallsensor3.get_distance3()

    print(f'Distance 1 = {distance}')
    print(f'Distance 2 = {distance2}')
    print(f'Distance 3 = {distance3}')

    time.sleep(0.15)

    
#    if (distance2 > 5 < distance <= distance3) :
    if (distance > 40 < distance3):
        rasp_motors.pwm_a.ChangeDutyCycle(0)
        rasp_motors.pwm_b.ChangeDutyCycle(0)
        time.sleep(2)
        place_found2()
        #break

