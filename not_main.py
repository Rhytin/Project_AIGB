import logging
from gpiozero import Button, PWMLED, OutputDevice
import time
import RPi.GPIO as GPIO            # import RPi.GPIO module
import csv

import time
import board
import Interfaces
import testModule

GPIO.setmode(GPIO.BCM)		# choose BCM or BOARD, relates to pin numbers  
#GPIO.setup(17, GPIO.OUT)	# set GPIO17 as an output; Fans
#GPIO.setup(7, GPIO.OUT)		# Motor
#GPIO.setup(16, GPIO.OUT)		# Motor
#GPIO.setup(19, GPIO.OUT)		# Motor
#GPIO.setup(24, GPIO.OUT)		# Motor

leds = Interfaces.LedStrip("Main Ledstrip", 21)                    # Create a 'LedStrip' object, giving it a name and a pin
pPump1 = Interfaces.PeristalticPump("Peri pump 1", 7)              # ...
pPump2 = Interfaces.PeristalticPump("Peri pump 2", 16)             # ...
pPump3 = Interfaces.PeristalticPump("Peri pump 3", 19)             # ...
waterPumps = Interfaces.SimpleActuator("Water pumps", 24)          # ...
fans = Interfaces.SimpleActuator("Fans", 17)                       # ...
cooling = Interfaces.SimpleActuator("Cooling", 13)                 # ...

tempHumSensor = Interfaces.BME280Sensor("Temperature/Humidity/Pressure sensor")    # Data: Object.temperature, Object.humidity, Object.pressure
condPHSensor = Interfaces.CondPHSensor("Conductivity/pH sensor")                   # Data: Object.temperature, Object.humidity, Object.pressure
co2Sensor = Interfaces.CO2Sensor("CO2 sensor")                                     # Data: Object.co2

# ________________________________________________________ Create a test __________________________________________________________
# Create a test wrapper
exampleTest = testModule.newTest("Example_test")    # Create a test and give it a name, test output will be "testName_output.csv"

#________________________________________ Used parts !!! ________________________________________________
# Link used parts, syntax: (Name, Object)

exampleTest.linkPart("Lights", leds)
exampleTest.linkPart("Base pump", pPump1)
exampleTest.linkPart("Water pumps", waterPumps)
exampleTest.linkPart("THPSensor", tempHumSensor)
exampleTest.linkPart("CpHSensor", condPHSensor)
exampleTest.linkPart("CO2Sensor", co2Sensor)

#________________________________________ End conditions !!! ____________________________________________
# Times are given in [Seconds, Minutes, Hours, Days], you can leave later ones out
# Combine conditions and actions to create and events here

testCondition1 = testModule.duration([0, 0, 3])             # After 3 hours ...
testAction1 = testModule.stopTest                           # Stop the test
exampleTest.createEvent(testCondition1, testAction1)        # Link condition and action to create an event for given test

testCondition2 = testModule.valueMax(["pH", 6])             # If value is larger than this number
testAction2 = testModule.set("Base pump", False)             # Set *device* to: True (on), False (off), [r,g,b] (led color), *number* (pwm)                          
exampleTest.createEvent(testCondition2, testAction2)        # If the pH goes above 6 pH, turn the base pump off

testCondition3 = testModule.valueMin(["Air Temperature", 30])   # If temperature is lower than 30 degrees
testAction3 = testModule.set("Lights", [255,0,255])         # Turn the lights on with a purple colour
testAction4 = testModule.set("Fans", False)                 # And also turn the fans off
exampleTest.createEvent(testCondition3, testAction3)        # Link both actions to the same condition
exampleTest.createEvent(testCondition3, testAction4)        # .....

# Stop the test if given value hasn't changed, within a deadband, over a given amount of time
# Syntax: 
testCondition4 = testModule.valuesUnchanged()


timeStart = time.time()
timeLast = time.time()
t = time.time()

with open('test.csv', mode= 'w', newline='' ) as csv_file:
    csv_writer = csv.writer(csv_file, dialect='excel')

    while True:
        temp, hum, press, alt = temp_hum_run()
        t = time.time()
        if (t > timeLast + 1.0):
            timeLast = t;
            print("Timestamp (since program start): ", round(t-timeStart, 2), "s")
            print("Temperature: ", round(temp, 2), "degrees Celsius")
            print("Humidity: ", round(hum, 1), "%RH")
            print("Pressure: ", round(press, 2), "Pa")
            print("")
            csv_writer.writerow([round(t-timeStart, 2), round(temp, 2)])
        