#Main code

import cmd
from turtle import distance
#from turtle import distance
import rasp_motors
import Schallsensor


print("Empezando programa")

print(f'The name is: {__name__}')


def busqueda():
    rasp_motors.dir_foward()
    rasp_motors.vel_foward()
    Schallsensor.main()

def calc():
    if distance == int(8):
        rasp_motors.pwm_a.stop()
        rasp_motors.pwm_b.stop()

    

while True:


    cmd = input("Ingrese S").lower()

    if cmd == "s":
        busqueda()
        calc()
    elif cmd =="r":
        rasp_motors.dir_backward()
        rasp_motors.vel_backward()
    elif cmd == "b":
        rasp_motors.pwm_a.stop()
        rasp_motors.pwm_b.stop()
        print ("System stoped")
        break
    print


