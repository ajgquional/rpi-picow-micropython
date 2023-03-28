# Project objective: Read voltage from the liquid level sensor as it is being submerged to different liquid depths
#
# Hardware and connections used:
#	Liquid level sensor + Pin to 3.3 V
#	Liquid level sensor - Pin to GND
#	Liquid level sensor S Pin to GPIO 28
#
# Programmer: Adrian Josele G. Quional

# modules
from machine import Pin, ADC
from time import sleep

# creating an ADC object
h2o = ADC(Pin(28))

# continuously read voltage from the sensor as it is being submerged to different liquid depths
while True:
    # print varying voltage read from the sensor
    print(h2o.read_u16())
    # readings can also be converted to voltage or calibrated to liquid depth
    
    # take readings every 1 sec
    sleep(1)