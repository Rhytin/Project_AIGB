from Interfaces import Sensor
import cond_ph

class CondPHSensor(Sensor):

    conductivity = 0
    ph = 0
    temperature = 0
    
    def __init__(this, givenName):
        this.name = givenName
        
    def getValues():
        return cond_ph.read_ph_ec()
    
    def updateValues():
        temperature, conductivity, ph = cond_ph.read_ph_ec()
        temperature = round(temperature, 1)
        conductivity = round(conductivity, 2)
        ph = round(ph, 2)

    def printData():
        print("Conductivity/Ph data:")
        print("Conductivity: ", conductivity, " ms/cm")
        print("pH value: ", ph)