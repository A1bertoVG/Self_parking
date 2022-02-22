#Main code

import cmd
import Schallsensor
import rasp_motors
import time


print("Empezando programa")

print(f'The name is: {__name__}')

def park_run():
    rasp_motors.dir_foward()
    rasp_motors.vel_foward()

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

            
    
while True:

    cmd = input("Ingrese S: ").lower()

    if cmd == "s":
        print("Running")
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
    print()
    



    


