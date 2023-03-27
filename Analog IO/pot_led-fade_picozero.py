# Project objective: Control the brightness of an LED using a potentiometer and picozero module
# 
# Hardware and connections used:
#   LED to GPIO Pin 15
#   220 ohm resistor for the LED
#   Potentiometer SIG pin to GPIO Pin 28 (capable of ADC)
#
# Programmer: Adrian Josele G. Quional

# importing Pot and LED class from the picozero module
from picozero import Pot, LED

# creating potentiometer and LED objects
pot = Pot(28)
led = LED(15)

# continuously control the brightness of the LED using the potentiometer
while True:
    # directly convert potentiometer values to brightness values
    led.value = pot.value