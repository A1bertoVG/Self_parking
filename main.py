#Main code

import cmd
from dis import dis
from time import time
from tracemalloc import start
from turtle import distance
#from turtle import distance
import rasp_motors
import Schallsensor


print("Empezando programa")

print(f'The name is: {__name__}')

def park_run():
    pass

def suchen():
    while True:
        distance = Schallsensor.get_distance()

        if distance >= 9:
            start = time.time()
        elif distance < 9:
            finish = time.time()
            dif_time = finish - start

            if dif_time >= 9:
                rasp_motors.pwm_a.stop()
                rasp_motors.pwm_b.stop()
                park_run()

            else:
                suchen()
    
'''
def calc():
    if distance == int(8):
        rasp_motors.pwm_a.stop()
        rasp_motors.pwm_b.stop()
'''
    

while True:


    cmd = input("Ingrese S").lower()

    if cmd == "s":
        rasp_motors.dir_foward()
        rasp_motors.vel_foward()
        suchen()
    elif cmd =="r":
        rasp_motors.dir_backward()
        rasp_motors.vel_backward()
    elif cmd == "b":
        rasp_motors.pwm_a.stop()
        rasp_motors.pwm_b.stop()
        print ("System stoped")
        break
    print


