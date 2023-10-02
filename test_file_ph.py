import logging
from gpiozero import Button, PWMLED, OutputDevice
import time
import RPi.GPIO as GPIO            # import RPi.GPIO module
import csv

import time
import board
import cond_ph as cond

GPIO.setmode(GPIO.BCM)		# choose BCM or BOARD  
GPIO.setup(17, GPIO.OUT)	# set GPIO17 as an output; Fans
GPIO.setup(7, GPIO.OUT)		# Motor
GPIO.setup(16, GPIO.OUT)		# Motor
GPIO.setup(19, GPIO.OUT)		# Motor
GPIO.setup(24, GPIO.OUT)		# Motor
GPIO.setup(13, GPIO.OUT)		# Koeling
GPIO.output(13, 0)

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
        temperature, EC, PH = cond.read_ph_ec()
        t = time.time()
        if (t > timeLast + 1.0):
            timeLast = t;
            print("Timestamp (since program start): ", round(t-timeStart, 2), "s")
            print("Temperature: ", round(temperature, 2), "degrees Celsius")
            print("EC: ", round(EC, 1), "mS/cm")
            print("pH: ", round(PH, 2), "pH")
            print("")
            csv_writer.writerow([round(t-timeStart, 2), round(temp, 2)])
            
            
        