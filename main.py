#Main code

import cmd
#from turtle import distance
import rasp_motors

print("Empezando programa")

print(f'The name is: {__name__}')

while True:

    cmd = input("Ingrese S").lower()

    if cmd == "s":
        rasp_motors.dir_foward()
        rasp_motors.vel_foward()
    elif cmd =="r":
        rasp_motors.dir_backward()
        rasp_motors.vel_backward()
    elif cmd == "b":
        rasp_motors.pwm_a.stop()
        rasp_motors.pwm_b.stop()
        print ("System stoped")
        break
    print


