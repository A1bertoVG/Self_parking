import cmd
import RPi.GPIO as GPIO
import os 
import time

ena = 13
enb = 21
in1 = 26
in2 = 19 
in3 = 16
in4 = 20

GPIO.setmode(GPIO.BCM)

GPIO.setup(in1, GPIO.OUT) #motor derecho fordward    
GPIO.setup(in2, GPIO.OUT) #motor derecho backward    
GPIO.setup(in3, GPIO.OUT) #motor izquierdo backward  
GPIO.setup(in4, GPIO.OUT) #motor izquierdo backward  
GPIO.setup(ena, GPIO.OUT) #pwm derecho  
GPIO.setup(enb, GPIO.OUT) #pwm izquierdo   

pwm_a = GPIO.PWM(ena, 500)
pwm_b = GPIO.PWM(enb, 500)

pwm_a.start(0)
pwm_b.start(0)

vel = 65
sta = 40

def dir_foward():
							
    GPIO.output(in1, False)
    GPIO.output(in2, True)
    GPIO.output(in3, True)
    GPIO.output(in4, False)

def dir_backward():
    GPIO.output(in1, True)
    GPIO.output(in2, False)
    GPIO.output(in3, False)
    GPIO.output(in4, True)

def vel_foward():
    pwm_a.ChangeDutyCycle(vel)
    pwm_b.ChangeDutyCycle(vel)

def vel_backward():
    pwm_a.ChangeDutyCycle(sta)
    pwm_b.ChangeDutyCycle(sta)

def park():
    pwm_a.ChangeDutyCycle(80)
    pwm_b.ChangeDutyCycle(70)
    GPIO.output(in1, True)
    GPIO.output(in2, False)
    GPIO.output(in3, True)
    GPIO.output(in4, False)
    time.sleep(1.3)
    vel_backward()
    dir_backward()
    time.sleep(2.5)
    pwm_a.ChangeDutyCycle(70)
    pwm_b.ChangeDutyCycle(80)
    GPIO.output(in1, False)
    GPIO.output(in2, True)
    GPIO.output(in3, False)
    GPIO.output(in4, True)
    time.sleep(1)
    vel_backward()
    dir_foward()
    time.sleep(0.5)

'''
while True:


    cmd = input("Ingrese S").lower()

    if cmd == "f":
        dir_foward()
        vel_foward()
    elif cmd =="b":
        dir_backward()
        vel_backward()
    elif cmd == "p":
        pwm_a.ChangeDutyCycle(0)
        pwm_b.ChangeDutyCycle(0)
        time.sleep(3)
        park()
        print ("System running")
        break
    print
'''


'''
os.system('clear')

print("Escriba F o B para seleccionar la direccion del auto y su velocidad")
print("Ejemplo: F50")
print
try:
    while True:
        cmd = input("Inserte comando")
        cmd = cmd.lower()
        
        dir = cmd[0]
        vel = cmd[1:4]

        if dir == "f":
            dir_foward()
            print("Avance hacia delante a una velocidad de ")
	    pwm_a.ChangeDutyCycle(vel)
	    pwm_b.ChangeDutyCycle(vel)


        elif dir == "b":
            dir_backward()
            print("Avance hacia atras a una velocidad de ")
	    pwm_a.ChangeDutyCycle(vel)
	    pwm_b.ChangeDutyCycle(vel)

        else:
            print("Comando no reconocido")
        #pwm_a.ChangeDutyCycle(50)
        #pwm_b.ChangeDutyCycle(50)
        print

except KeyboardInterrupt:
    pwm_a.stop()
    pwm_b.stop()
    GPIO.cleanup()
    os.system("clear")
    print
    print("Programa terminado")
    print
    exit()

'''


