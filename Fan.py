from Interfaces import Actuator
from gpiozero import Button, PWMLED, OutputDevice
import RPi.GPIO as GPIO            # import RPi.GPIO module

class Fans(Actuator):
    pin = 17
    
    def __init__(this):
        this.setup()
        
    def __init__(this, pinNew):
        this.pin = pinNew
        this.setup()
        
    def setup(this):
        GPIO.setup(this.pin, GPIO.OUT)
        
    def turnOn(this):
        GPIO.output(this.pin, 1)
        
    def turnOff(this):
        GPIO.output(this.pin, 0)