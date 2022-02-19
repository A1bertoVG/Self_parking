import time
import os
from tracemalloc import start

# os.system('clear')

def selfparking():
    print("Estacionando")

print("Escriba a para empezar cronometro y b para detener: ")
print
try:
    while True:
        cmd = input ("A para empezar: ")
        cmd = cmd.lower()

        if cmd == "a":
            
            start = time.time()
            #start = float(start)

        elif cmd == "b":
            
            finish = time.time()
            diftime = finish - start

            if diftime >= 6:
                print ("espacio encontrado")
                print (f'Tiempo = {diftime}s')

                selfparking()
                break
            else:
                print("no existe espacio")

            print (f'Tiempo = {diftime}s')
            

        else:
            print("error")


except KeyboardInterrupt:
    pwm_a.stop()
    pwm_b.stop()
    GPIO.cleanup()
    os.system("clear")
    print
    print("Programa terminado")
    print
    exit()


