from Interfaces import Actuator
from gpiozero import Button, PWMLED, OutputDevice
import RPi.GPIO as GPIO            # import RPi.GPIO module

class PeristalticPump(Actuator):
    pin = 16
    pwmBoolean = False
    pi_pwm = None
    
    def __init__(this, givenName):
        this.setup()
        
    def __init__(this, givenName, pinNew):
        this.pin = pinNew
        this.setup(givenName)
        
    def __init__(this, givenName, pinNew, pwmBool):
        this.pin = pinNew
        this.pwmBoolean = pwmBool
        this.setup(givenName)
       
    def setup(this, givenName):
        this.name = givenName
        GPIO.setup(this.pin, GPIO.OUT)
        if (this.pwmBoolean):
            pi_pwm = GPIO.PWM(this.pin, 1000)
            pi_pwm.start(0)
        
    def set(this):
        GPIO.output(this.pin, 1)
        
    def set(this, pwm):
        GPIO.PWM(this.pin, pwm)