from Interfaces import Actuator
from gpiozero import Button, PWMLED, OutputDevice
import RPi.GPIO as GPIO            # import RPi.GPIO module

class SimpleActuator(Actuator):
    pin = 13
    
    def __init__(this, givenName):
        this.setup(givenName)
        
    def __init__(this, givenName, pinNew):
        this.pin = pinNew
        this.setup(givenName)
        
    def setup(this, givenName):
        this.name = givenName
        GPIO.setup(this.pin, GPIO.OUT)
        
    def turnOn(this):
        GPIO.output(this.pin, 1)
        
    def turnOff(this):
        GPIO.output(this.pin, 0)