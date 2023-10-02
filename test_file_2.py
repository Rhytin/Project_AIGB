import logging
from gpiozero import Button, PWMLED, OutputDevice
import time
import RPi.GPIO as GPIO            # import RPi.GPIO module
from rpi_ws281x import *
import csv

import time
import board
import bme280 as bme
import cond_ph as cond

GPIO.setmode(GPIO.BCM)		# choose BCM or BOARD  
GPIO.setup(17, GPIO.OUT)	# set GPIO17 as an output; Fans
GPIO.setup(7, GPIO.OUT)		# Motor
GPIO.setup(16, GPIO.OUT)		# Motor
GPIO.setup(19, GPIO.OUT)		# Motor
GPIO.setup(24, GPIO.OUT)		# Motor
GPIO.setup(13, GPIO.OUT)		# Koeling
GPIO.output(13, 0)
# pwm = GPIO.PWM(13, 1)

def colorWipe(strip, color, wait_ms=25):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
    
def temp_hum_run():	# Sensor variables 
    temperature,pressure,humidity = bme.readBME280All()       
    return temperature, humidity, pressure

LED_COUNT      = 192      # Number of LED pixels.
LED_PIN        = 21      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Default; Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP      = ws.SK6812_STRIP_GRBW
#LED_STRIP      = ws.SK6812W_STRIP
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
strip.begin()

colorWipe(strip, Color(255, 255, 255))  # Red wipe with GRB --> aigb green with rgb

timeStart = time.time()
timeLast = time.time()
t = time.time()


cond.reset_ec()
#cond.reset_ph()

cond.calibration_ec()
#cond.calibration_ph()


# colorWipe(strip, Color(0,0,0))
with open('test.csv', mode= 'w', newline='' ) as csv_file:
    csv_writer = csv.writer(csv_file, dialect='excel')

    while True:
        temp, hum, press = temp_hum_run()
        temperature, EC, PH = cond.read_ph_ec()
        t = time.time()
        if (t > timeLast + 1.0):
            timeLast = t;
            print("Timestamp (since program start): ", round(t-timeStart, 2), "s")
            print("Temperature: ", round(temp, 2), "degrees Celsius")
            print("Humidity: ", round(hum, 1), "%RH")
            print("Pressure: ", round(press, 2), "Pa")
            print("Temperature: ", round(temperature, 2), "degrees Celsius")
            print("EC: ", round(EC, 1), "mS/cm")
            print("pH: ", round(PH, 2), "pH")
            print("")
            csv_writer.writerow([round(t-timeStart, 2), round(temp, 2)])
            
            
        