import cmd
from turtle import distance
import Schallsensor
import rasp_motors
import time

#Evolution measrurement
length = 22.3
width = 5  #real es 1315 mm

print("Empezando programa")

print(f'The name is: {__name__}')

def measurement():
    while True:
        dist=Schallsensor.get_distance()

        if dist > width:
            start = time.time()
            print('State: Longer than width')
            print(f'distance {dist} cm')
            #print(start)
        else:
            print('State: Shorter tham width')
            print(f'distance {dist} cm')
            finish = time.time()
            diftime = finish - start
        print(start)
        print(finish)
        print(diftime)

        time.sleep(0.5)

while True:

    cmd = input("Ingrese S: ").lower()

    if cmd == "s":
        rasp_motors.vel_foward()
        rasp_motors.dir_foward()
        measurement()

    elif cmd =="r":
        rasp_motors.dir_backward()
        rasp_motors.vel_backward()
    elif cmd == "b":
        rasp_motors.pwm_a.stop()
        rasp_motors.pwm_b.stop()
        print ("System stoped")
        break
    print()