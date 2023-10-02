from LedStrip import *
from PeristalticPump import *
from SimpleActuator import * 
from BME280Sensor import *
from CO2Sensor import *
from CondPHSensor import *

class Actuator:
    name = "undefined (Was a name given at creation?)"
    def turnOn():
        print("Function not overwritten properly (Was this object created properly?)")
    def turnOff():
        print("Function not overwritten properly (Was this object created properly?)")
    
class Sensor:
    name = "Undefined (Was a name given at creation?)"
    def getValues():
        print("Function not overwritten properly (Was this object created properly?)")
    def updateValues():
        print("Function not overwritten properly (Was this object created properly?)")
    def printData():
        print("Function not overwritten properly (Was this object created properly?)")