import time
import sys
sys.path.insert(0,'/home/pi/git/Project_AIGB/DFRobot_ADS1115/python/raspberrypi')
sys.path.insert(0,'/home/pi/git/Project_AIGB/GreenPonik_EC_Python/src')
sys.path.insert(0,'/home/pi/git/Project_AIGB/GreenPonik_PH_Python/src')


ADS1115_REG_CONFIG_PGA_6_144V        = 0x00 # 6.144V range = Gain 2/3
ADS1115_REG_CONFIG_PGA_4_096V        = 0x02 # 4.096V range = Gain 1
ADS1115_REG_CONFIG_PGA_2_048V        = 0x04 # 2.048V range = Gain 2 (default)
ADS1115_REG_CONFIG_PGA_1_024V        = 0x06 # 1.024V range = Gain 4
ADS1115_REG_CONFIG_PGA_0_512V        = 0x08 # 0.512V range = Gain 8
ADS1115_REG_CONFIG_PGA_0_256V        = 0x0A # 0.256V range = Gain 16

from DFRobot_ADS1115 import ADS1115
from GreenPonik_EC import GreenPonik_EC
from GreenPonik_PH import GreenPonik_PH

ads1115 = ADS1115()
ec      = GreenPonik_EC()
ph      = GreenPonik_PH()

ec.begin()
ph.begin()

def read_ph_ec():
	global ads1115
	global ec
	global ph
	temperature = 25 # or make your own temperature read process
	#Set the IIC address
	ads1115.set_addr_ADS1115(0x48)
	#Sets the gain and input voltage range.
	ads1115.set_gain(ADS1115_REG_CONFIG_PGA_6_144V)
	#Get the Digital Value of Analog of selected channel
	adc0 = ads1115.read_voltage(0)
	adc1 = ads1115.read_voltage(1)
	#Convert voltage to EC with temperature compensation
	EC = ec.readEC(adc0['r'],temperature)
	PH = ph.readPH(adc1['r'])
	#print("Temperature:%.1f ^C EC:%.2f ms/cm PH:%.2f " %(temperature,EC,PH))
	return temperature, EC, PH

def reset_ec():
    ec.reset()

def reset_ph():
    ph.reset()

def calibration_ec():
	global ads1115
	global ec
	global ph
	temperature = 25 # or make your own temperature read process
	#Set the IIC address
	ads1115.set_addr_ADS1115(0x48)
	#Sets the gain and input voltage range.
	ads1115.set_gain(ADS1115_REG_CONFIG_PGA_6_144V)
	#Get the Digital Value of Analog of selected channel
	adc0 = ads1115.read_voltage(0)
	adc1 = ads1115.read_voltage(1)
	#Convert voltage to EC with temperature compensation
	EC = ec.readEC(adc0['r'], temperature)
	#print("Temperature:%.1f ^C EC:%.2f ms/cm PH:%.2f " %(temperature,EC,PH))
	print(adc0)
	#ph.calibration(number)
	ec.calibration(adc0['r'], temperature)
	
def calibration_ph():
	global ads1115
	global ec
	global ph
	temperature = 25 # or make your own temperature read process
	#Set the IIC address
	ads1115.set_addr_ADS1115(0x48)
	#Sets the gain and input voltage range.
	ads1115.set_gain(ADS1115_REG_CONFIG_PGA_6_144V)
	#Get the Digital Value of Analog of selected channel
	adc0 = ads1115.read_voltage(0)
	adc1 = ads1115.read_voltage(1)
	#Convert voltage to EC with temperature compensation
	PH = ph.readPH(adc1['r'])
	#print("Temperature:%.1f ^C EC:%.2f ms/cm PH:%.2f " %(temperature,EC,PH))
	print(adc1)
	#ph.calibration(number)
	ph.calibration(adc1['r'])

#while True:
#    read_ph_ec()
