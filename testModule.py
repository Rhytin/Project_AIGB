import Interfaces

import csv
import time
import board
import bisect

class TestModule:

    testName = "undefined"
    objects = {}
    events = {}

    timeDict = {"startTime": time.time()}
    timeDict["currentTime"] = time.time() - timeDict["startTime"]

    dataLocationDict = {}                       # {key(dataSubject): variable, key(dataSubject): variable}
                                                # For example dataLocationDict[pH] => pHdata variable

    dataLogDict = {}                            # {key(dataSubject): {timestamp(t): data}, {timestamp(t1): data1}, {timestamp(t2): data2} }
                                                # For example dataLogDict[pH][timestamp] => pHdata at timestamp


    def newTest(this, str):
        this.testName = str   
#exampleTest = testModule.newTest("Example_test")    # Create a test and give it a name, test output will be "testName_output.csv"

    def linkPart(this, str, object):
        this.objects[str] = object                                          # Add the given object to the dictionary with the given name
        if isinstance(object, Interfaces.Sensor):                           # If the given object is a Sensor 
            this.dataLocationDict |= object.dataDict                        # Add the data output name and where to find it

    def createEvent(this, condition, action):                       
        eventname = "Event" + str(len(this.events))                         # Create event name
        temp = Event.createEvent(condition, action, this.timeDict, this.dataLogDict)       # Create the actual event 'Object'
        this.events[eventname] = temp                                       # Add the event to the dictionary
    
    def runEvents(this):
        for key in this.events:                                             # Iterating will give the keys
            event = this.events[key]                                        # Get the 'actual' event object, using the key 
            event.checkCondition()                                          # Check the condition


class Condition:

    definition = {}

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
        this.definition["type"] = "duration"
        this.definition["startTime"] = time.time()
        this.definition["duration"] = this.convertTime(lst)
        this.definition["endTime"] = this.definition["startTime"] + this.definition["duration"]
    
    def valueMax(this, lst):
        this.definition["type"] = "max"
        this.definition["dataKey"] = lst[0]
        this.definition["max"] = lst[1]
    
    def valueMin(this, lst):
        this.definition["type"] = "min"
        this.definition["dataKey"] = lst[0]
        this.definition["max"] = lst[1]

    def valueUnchanged(this, lst):
        this.definition["type"] = "delta"
        this.definition["dataKey"] = lst[0]
        this.definition["deadband"] = lst[1]
        this.definition["startTime"] = time.time()
        this.definition["deltaTime"] = this.convertTime(lst[2])
        this.definition["firstCheckTime"] = this.definition["startTime"] + this.definition["deltaTime"]


class Action:

    definition = {}

    def stopTest(this, object):
        this.definition["type"] = "stop"
        this.definition["object"] = object

    def set(this, object, argument):
        this.definition["type"] = "set"
        this.definition["actuator"] = object
        this.definition["argument"] = argument


class Event:

    lastCheckResult = False
    definition = {}
    timeDict = {}
    dataLog = {}

    def createEvent(this, condition, action, timeDict, dataLog):
        this.definition["condition"] = condition
        this.definition["action"] = action
        this.timeDict = timeDict
        this.dataLog = dataLog

        match condition.definition["type"]:
            case "duration":
                condition.definition["startTime"] = condition.definition["startTime"]-this.timeDict["startTime"]
                condition.definition["endTime"] = condition.definition["endTime"]-this.timeDict["startTime"]

            case "delta":
                condition.definition["startTime"] = condition.definition["startTime"]-this.timeDict["startTime"]
                condition.definition["firstCheckTime"] = condition.definition["firstCheckTime"]-this.timeDict["startTime"]

    def checkCondition(this):
        condition = this.definition["condition"]
        passed = this.lastCheckResult

        match condition.definition["type"]:

            case "duration":
                if (this.timeDict["CurrentTime"] > condition.definition["endTime"]):
                    passed = True

            case "min":
                dataKey = condition.definition["dataKey"]                   # For example, dataKey "Temperature"      
                specificDataDict = this.dataLog[dataKey]                    # this.dataLog["Temperature"] gives the temperature dict
                lastKey = list(specificDataDict.keys())[-1]                 # get the last key of the temperature dict
                lastEntry = specificDataDict[lastKey]                       # get the corresponding value from the last key

                if (lastEntry < condition.definition["min"]):
                    passed = True

            case "max":
                dataKey = condition.definition["dataKey"]                   # For example, dataKey "Temperature"      
                specificDataDict = this.dataLog[dataKey]                    # this.dataLog["Temperature"] gives the temperature dict
                lastKey = list(specificDataDict.keys())[-1]                 # get the last key of the temperature dict
                lastEntry = specificDataDict[lastKey]                       # get the corresponding value from the last key

                if (lastEntry > condition.definition["max"]):
                    passed = True

            case "delta":
                if (this.timeDict["currentTime"] > condition.definition["firstCheckTime"]):                  # First check if the deltaTime has passed
                    dataKey = condition.definition["dataKey"]
                    specificDataDict = this.dataLog[dataKey]                    # this.dataLog["Temperature"] gives the temperature dict
                    lastKey = list(specificDataDict.keys())[-1]                 # get the last key of the temperature dict
                    lastEntry = specificDataDict[lastKey]                       # get the corresponding value from the last key
                    deltaEntry = bisect.bisect_left(specificDataDict, int(lastKey)-int(condition.definition["deltaTime"]))
                    #get closest datapoint


                    passed = True



        if (passed and (passed is not this.lastCheckResult)):
            this.doAction()
            this.lastCheckResult = passed
        else:
            this.lastCheckResult = passed
    
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