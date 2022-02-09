import cmd
import RPi.GPIO as GPIO
import os 
from time import sleep

ena = 18
enb = 19
md1 = 23
md2 = 24 
mi1 = 6
mi2 = 5

GPIO.setmode(GPIO.BCM)

GPIO.setup(md1, GPIO.OUT) #motor derecho fordward    
GPIO.setup(md2, GPIO.OUT) #motor derecho backward    
GPIO.setup(mi1, GPIO.OUT) #motor izquierdo backward  
GPIO.setup(mi2, GPIO.OUT) #motor izquierdo backward  
GPIO.setup(ena, GPIO.OUT) #pwm derecho  
GPIO.setup(enb, GPIO.OUT) #pwm izquierdo   

pwm_a = GPIO.PWM(ena, 500)
pwm_b = GPIO.PWM(enb, 500)

pwm_a.start(0)
pwm_b.start(0)

def dir_foward():
    GPIO.output(md1, True)
    GPIO.output(md2, False)
    GPIO.output(mi1, True)
    GPIO.output(mi2, False)

def dir_backward():
    GPIO.output(md1, False)
    GPIO.output(md2, True)
    GPIO.output(mi1, False)
    GPIO.output(mi2, True)

os.system('clear')

print("Escriba F o B para seleccionar la direccion del auto y su velocidad")
print("Ejemplo: F50")
print
try:
    while True:
        cmd = raw_input("Inserte comando")
        cmd = cmd.lower()
        
        dir = cmd[0]
        vel = cmd[1:4]

        if dir == "f":
            dir_foward()
            print("Avance hacia delante a una velocidad de "+ vel)

        elif dir == "b":
            dir_backward()
            print("Avance hacia atras a una velocidad de "+ vel)

        else:
            print("Comando no reconocido")
        pwm_a.ChangeDutyCycle(int(vel))
        pwm_b.ChangeDutyCycle(int(vel))
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




