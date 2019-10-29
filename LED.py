import RPi.GPIO as GPIO
import time

#GPIO 16 - YELLOW LED
#

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def turnLEDon(GPno):
    GPIO.setup(GPno,GPIO.OUT)
    print("LED on")
    GPIO.output(GPno,GPIO.HIGH)
    time.sleep(1)
    print("LED off")
    GPIO.output(GPno,GPIO.LOW)


turnLEDon(16) #yellow led

turnLEDon(18) #green led

turnLEDon(15) #red led

turnLEDon(22) #white led