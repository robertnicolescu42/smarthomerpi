#programul asta de python o sa afiseze si temperatura/presiunea/etc si lumina. trebuie sa fac un meniu cu switch

#importuri pentu temperatura/presiune
import board
import busio
import adafruit_bme280
import time
#importuri pentru senzorul de lumina
import smbus

def bme280():
    i2c = busio.I2C(board.SCL, board.SDA)
    #while True:
    #    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
    #    print("\nTemperature: %0.1f C" % bme280.temperature)
    #    print("Humidity: %0.1f %%" % bme280.humidity)
    #    print("Pressure: %0.1f hPa" % bme280.pressure)
    #    time.sleep(1)
    
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
    print("\nTemperature: %0.1f C" % bme280.temperature)
    print("Humidity: %0.1f %%" % bme280.humidity)
    print("Pressure: %0.1f hPa" % bme280.pressure)
        
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
    print("Light Level : " + format(lightLevel,'.2f') + " lx")

def main():
    answer = input("What do you want to measure?\n1.Temperature/humidity/pressure\n2.The light level\n")
    if (answer == "1"):
        bme280()
    else:
        bh1750()
        
        
main()