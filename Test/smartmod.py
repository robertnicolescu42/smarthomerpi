#imports for temperature/humidity/pressure sensor
import board
import busio
import adafruit_bme280
import time
#imports for light sensor
import smbus
#imports for LEDs
import RPi.GPIO as GPIO

def bme280():
    i2c = busio.I2C(board.SCL, board.SDA)
    #while True:
    #    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
    #    print("\nTemperature: %0.1f C" % bme280.temperature)
    #    print("Humidity: %0.1f %%" % bme280.humidity)
    #    print("Pressure: %0.1f hPa" % bme280.pressure)
    #    time.sleep(1)
    
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
    #print("\nTemperature: %0.1f C" % bme280.temperature)
    #print("Humidity: %0.1f %%" % bme280.humidity)
    #print("Pressure: %0.1f hPa" % bme280.pressure)
    list = [bme280.temperature, bme280.humidity, bme280.pressure]
    return list

        
def bh1750():
    # Define some constants from the datasheet

    DEVICE     = 0x23 # Default device I2C address

    POWER_DOWN = 0x00 # No active state
    POWER_ON   = 0x01 # Power on
    RESET      = 0x07 # Reset data register value

    # Start measurement at 4lx resolution. Time typically 16ms.
    CONTINUOUS_LOW_RES_MODE = 0x13
    # Start measurement at 1lx resolution. Time typically 120ms
    CONTINUOUS_HIGH_RES_MODE_1 = 0x10
    # Start measurement at 0.5lx resolution. Time typically 120ms
    CONTINUOUS_HIGH_RES_MODE_2 = 0x11
    # Start measurement at 1lx resolution. Time typically 120ms
    # Device is automatically set to Power Down after measurement.
    ONE_TIME_HIGH_RES_MODE_1 = 0x20
    # Start measurement at 0.5lx resolution. Time typically 120ms
    # Device is automatically set to Power Down after measurement.
    ONE_TIME_HIGH_RES_MODE_2 = 0x21
    # Start measurement at 1lx resolution. Time typically 120ms
    # Device is automatically set to Power Down after measurement.
    ONE_TIME_LOW_RES_MODE = 0x23

    #bus = smbus.SMBus(0) # Rev 1 Pi uses 0
    bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

    def convertToNumber(data):
      # Simple function to convert 2 bytes of data
      # into a decimal number. Optional parameter 'decimals'
      # will round to specified number of decimal places.
      result=(data[1] + (256 * data[0])) / 1.2
      return (result)

    def readLight(addr=DEVICE):
      # Read data from I2C interface2
      data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)
      return convertToNumber(data)
    
    #while True:
    #    lightLevel=readLight()
    #    print("Light Level : " + format(lightLevel,'.2f') + " lx")
    #    time.sleep(0.5)
    lightLevel = readLight()
    #return("Light Level : " + format(lightLevel,'.2f') + " lx")
    return format(lightLevel, '.2f')

def sensors():
    answer = input("What do you want to measure?\n1.Temperature/humidity/pressure\n2.The light level\n")
    if (answer == "1"):
        list = bme280()
        print("\nTemperature: %0.1f C" % list[0])
        print("Humidity: %0.1f %%" % list[1])
        print("Pressure: %0.1f hPa" % list[2])
    else:
        print("Light level : " + bh1750() + " lx")
        

#############################LEDs code
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def turnLEDon(GPno):
    GPIO.setup(GPno,GPIO.OUT)
    #print("LED on")
    GPIO.output(GPno,GPIO.HIGH)
    time.sleep(0.5)
    #print("LED off")
    GPIO.output(GPno,GPIO.LOW)

def yellowLED():
    turnLEDon(16) #yellow led

def greenLED():
    turnLEDon(18) #green led

def redLED():
    turnLEDon(15) #red led

def whiteLED():
    turnLEDon(22) #white led
#####################################
def SensCheck():
    list = bme280()
    lightLV = bh1750()
    
    #if (lightLV < '1.00'):
    #    whiteLED()
    #if (list[0] > 20):
    #    redLED()
    #if (list[1] > 98):
    #    greenLED()
    #if (list[2] > 700):
    #    yellowLED()
    
    lightLevel = lightLV + " lx"
    tempLevel = "Temperature: %0.1f C" % list[0]
    humidLevel = "Humidity: %0.1f %%" % list[1]
    presLevel = "Pressure: %0.1f hPa" % list[2]

    #print(lightLevel)
    #print(humidLevel)
    #print(presLevel)
    #print (tempLevel)
    
    strlist = []
    strlist.append(lightLV)
    strlist.append("%0.1f" % list[0])
    strlist.append("%0.1f" % list[1])
    strlist.append("%0.1f" % list[2])
    return strlist
        
#SensCheck()
#sensors()

def solution():
    list = SensCheck()
    my_string = ','.join(map(str, list))
    return(my_string)
    
#print(solution())
#print(solution())

def fisier():
    f=open('date.txt',"w+")
    lista = solution()
    #print(lista)
    f.write(lista)
    f.close()
   
#print("merge")
while (True):
    fisier()
    time.sleep(10)