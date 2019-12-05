import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def turnLEDon(GPno):
    GPIO.setup(GPno,GPIO.OUT)
    #print("LED on")
    GPIO.output(GPno,GPIO.HIGH)
    time.sleep(0.5)
    #print("LED off")
    GPIO.output(GPno,GPIO.LOW)
    
turnLEDon(22)