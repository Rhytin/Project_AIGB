from Interfaces import Sensor
import mh_z19

class CO2Sensor(Sensor):

    co2 = 0
    
    def __init__(this, givenName):
        this.name = givenName
        
    def getValues():
        return mh_z19.read_co2valueonly()
    
    def updateValues():
        co2 = mh_z19.read_co2valueonly()
        
    def testReturnType():
        print(mh_z19.read_co2valueonly())

    def printData():
        print("CO2 sensor data:")
        print("CO2 concentration: ", co2, " ppm")