from interfaces import Actuator
from rpi_ws281x import *
from gpiozero import Button, PWMLED, OutputDevice
import RPi.GPIO as GPIO            # import RPi.GPIO module

class LedStrip(Actuator):
    
    LED_COUNT      = 192      # Number of LED pixels.
    LED_PIN        = 21      # GPIO pin connected to the pixels (must support PWM!).
    LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
    LED_BRIGHTNESS = 255     # Default; Set to 0 for darkest and 255 for brightest
    LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
    LED_CHANNEL    = 0
    LED_STRIP      = ws.SK6812_STRIP_GRBW
    #LED_STRIP      = ws.SK6812W_STRIP
    strip = None
    
    def __init__(this, givenName):
        this.setup(givenName)
        
    def __init__(this, givenName, pin):
        this.LED_PIN = pin
        this.setup(givenName)
        
    def setup(this, givenName):
        this.name = givenName
        this.LED_STRIP = ws.SK6812_STRIP_GRBW
        
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        strip.begin()
        
    def set():
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(255,255,255))
        strip.show()
    
    def set(r,g,b):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(r,g,b))
        strip.show()
        
    def fancySet(r,g,b,delay):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(r,g,b))
            strip.show()
            time.sleep(delay/1000.0)