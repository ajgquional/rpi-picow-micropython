# ================================================== 
""" 
Project objectives:
    Read voltage from an LDR circuit
    Convert readings from LDR to voltage
    Print readings to the console

Hardware and connections used:
    LDR and a 10k ohm resistor in series (specifically a voltage divider network)
    LDR connected to 3.3 V (reference voltage)
    10k ohm resistor connected to GND
    Overlap of LDR and 10k ohm resistor connected to GPIO Pin 28 (capable of ADC)

Author: Adrian Josele G. Quional
"""
# ==================================================

# modules
from machine import ADC, Pin
from time import sleep

# creating an ADC object named LDR
# LDR can be connected to any GPIO pins capable of analog inputs (GPIO 26-28)
ldr = ADC(Pin(28))

# continuously read voltage from the LDR
while True:
    # store LDR readings in a variable
    ldr_val = ldr.read_u16()
    
    # convert LDR readings (analog values) to voltage
    # conversion factor: 3.3 V = 65535
    voltage = ldr_val * (3.3 / 65535)
    
    # print analog values and equivalent voltage
    print(f"Analog values: {ldr_val}	Voltage: {voltage}")
    sleep(1)
