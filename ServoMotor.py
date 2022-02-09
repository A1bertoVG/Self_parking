import RPi.GPIO as GPIO 
import time

servo = 12

GPIO.setmode(GPIO.BCM)

GPIO.setup(servo, GPIO.OUT).PWM(50)

servo.start(0)
print("Inicializing")
time.sleep(2)

print("Roateting 180° in 10 steps")

duty = 2

#while duty <= 12:



print ("ALLES GUT")
