import Interfaces

import csv
import time
import board

class TestModule:

    eventsInitialised = False

    def newTest(this, str):
        this.testName = str   
#exampleTest = testModule.newTest("Example_test")    # Create a test and give it a name, test output will be "testName_output.csv"

    def linkPart(object, str):
        Objects.append(objects)
        if isinstance(object, Interfaces.LedStrip):
            lights = object

    def createEvent(this, condition, action):
        if not eventsInitialised:
            this.eventsList = [Event.createEvent(condition, action)]
            eventsInitialised = True
        else:
            this.eventsList.append(Event.createEvent(condition, action))
    
    def runEvents(this):
        if eventsInitialised == True:
            for i in range(eventsList):
                if i.checkCondition() is not i.lastCheckResult:
                    i.doAction
        if 


class Condition:

    type = "undefined"

    def convertTime(lst):
        match (len(lst)):
            case 1:
                return lst[0]
            case 2:
                return (lst[0] + 60 * lst[1])
            case 3:
                return (lst[0] + 60*(lst[1] + 60*lst[2]))
            case 4:
                return (lst[0] + 60*(lst[1] + 60*(lst[2] + 24*lst[3])))

    def duration(this, lst):
        this.type = "duration"
        this.duration = this.convertTime(lst)
    
    def valueMax(this, lst):
        this.type = "max"
        this.value = lst[0]
        this.max = lst[1]
    
    def valueMin(this, lst):
        this.type = "min"
        this.value = lst[0]
        this.min = lst[1]

    def valueUnchanged(this, lst):
        this.type = "delta"
        this.value = lst[0]
        this.deadband = lst[1]
        this.dTime = this.convertTime(lst[2])

class Action:

    type = "undefined"

    def stopTest(this, object):
        this.type = "stop"
        this.object = object

    def set(this, object, argument):
        this.type = "set"
        this.object = object
        this.argument = argument

class Event:

    lastCheckResult = False

    def createEvent(this, condition, action):
        this.condition=condition
        this.action=action

        match condition.type:
            case "duration":

    def checkCondition():
        return #Succeeded?

    def doAction(this):
        match this.action.type:
            case "stop":
                # Zet alles uit, schrijf data weg
                
            case "set":
                this.action.object.set(this.action.arguments)

                

    def stop()
        
    def start()


class duration:
    def __init__(this, lst):
        this.seconds = 0
        for i in lst:
            this.seconds = this.seconds + i

class stopTest:


        


    

#________________________________________ Used parts !!! ________________________________________________
# Link used parts, syntax: (Object, optional arguments)

exampleTest.linkPart(leds, "Lights")         # Optional argument for leds is: [r,g,b]
exampleTest.linkPart(pPump1, "pPump1")                    # Optional argument for peristaltic pumps is a PWM value (0-100)
exampleTest.linkPart(waterPumps)                    # Waterpumps, fans and the cooling dont have optional arguments, they'll just be turned on 

exampleTest.linkPart(tempHumSensor, "THSensor",                 # Optional arguments are what values you want to use: (Still optional, will use everything without arguments)
                    [True,                           # Temperature
                    True,                           # Humidity
                    True])                           # Pressure

exampleTest.linkPart(condPHSensor,                  # Optional arguments are what values you want to use: (Still optional, will use everything without arguments)
                    [True,                           # Conductivity
                    True,                           # pH
                    False])                          # Temperature

exampleTest.linkPart(co2Sensor)                     # Has no optional arguments

#________________________________________ End conditions !!! ____________________________________________
# Times are given in [Seconds, Minutes, Hours, Days], you can leave later ones out
# Combine conditions and actions to create and events here

testCondition1 = Condition.duration([0, 0, 3])                                              # After 3 hours ...
testAction1 = Action.stopTest(exampleTest)                                                  # Stop the test
durationEvent = testModule.createEvent(testCondition1, testAction1)                         # Link condition and action to create an event for given test

testCondition2 = testModule.valueMax([exampleTest.pH, 6])                                   # If value is larger than this number
testAction2 = testModule.set(exampleTest.basePump, False)                                   # Set *device* to: True (on), False (off), [r,g,b] (led color), *number* (pwm)                          
phLowEvent = testModule.createEvent(testCondition2, testAction2)                                         # If the pH goes above 6 pH, turn the base pump off

testCondition3 = testModule.valueMin([exampleTest.temperature, 30])                         # If temperature is lower than 30 degrees
testAction3 = testModule.set(exampleTest.lights, [255,0,255])                               # Turn the lights on with a purple colour
testAction4 = testModule.set(exampleTest.fans, False)                                       # And also turn the fans off
tempLowLights = testModule.createEvent(testCondition3, testAction3)                                         # Link both actions to the same condition
tempLowFans = testModule.createEvent(testCondition3, testAction4)                                         # .....

# If given values are within a given deadband when compared to a value a given amount of time of time ago
testCondition4 = testModule.valueUnchanged([exampleTest.temperature, 5.0, [30, 5]])        # Syntax: [value, deadband, [Time]]
testAction5 = testModule.set(exampleTest.lights, [255,255,255])                             # 
tempUnchangedLights = testModule.createEvent(testCondition4, testAction5)

phLowEvent.stop()                                                                           # Stop triggering on the given event    (Enable by default at creation)
phLowEvent.start()                                                                          # Resume triggering on the given event

exampleTest.stopLog(exampleTest.temperature)                                                # Stop logging given value              (Enabled by default at creation)
exampleTest.startLog(exampleTest.temperature)                                               # Resume logging of given value

while True:
    exampleTest.run()                                                                       # Run the system untill stopTest() is called, export logs when this happens