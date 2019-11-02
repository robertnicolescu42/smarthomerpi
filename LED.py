import RPi.GPIO as GPIO
import time

#GPIO 16 - YELLOW LED
#GPIO 18 - GREEN LED
#GPIO 15 - RED LED
#GPIO 22 - WHITE LED

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def turnLEDon(GPno):
    GPIO.setup(GPno,GPIO.OUT)
    print("LED on")
    GPIO.output(GPno,GPIO.HIGH)
    time.sleep(1)
    print("LED off")
    GPIO.output(GPno,GPIO.LOW)

def yellowLED():
    turnLEDon(16) #yellow led

def greenLED():
    turnLEDon(18) #green led

def redLED():
    turnLEDon(15) #red led

def whiteLED():
    turnLEDon(22) #white led