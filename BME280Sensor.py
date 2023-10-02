from Interfaces import Sensor
import bme280

class BME280(Sensor):

    temperature = 0
    humidity = 0 
    pressure = 0

    def __init__(this, givenName):
        this.name = givenName
        
    def getValues():
        return bme280.readBME280All()
    
    def updateValues():
        temperature, humidity, pressure = bme280.readBME280All
        temperature = round(temperature, 1)
        humidity = round(humidity, 1)
        pressure = round(pressure, 1)

    def printData():
        print("BME data:")
        print("Temperature: ", temperature, " degrees Celsius")
        print("Humidity: ", humidity, " %RH")
        print("Pressure: ", pressure, " hPa")