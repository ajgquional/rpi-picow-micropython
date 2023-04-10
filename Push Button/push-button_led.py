# ================================================== 
""" 
Project objective: Light up an external LED when a push button is pressed

Hardware and connections used:
    Push button to GPIO Pin 16
    10k ohm pull-down resistor for the push button
    LED anode to GPIO Pin 15
    220 ohm resistor for LED
    
Author: Adrian Josele G. Quional
"""
# ==================================================

# modules
from machine import Pin
from time import sleep

LED = Pin(9, Pin.OUT)		# creating LED object, setting it as OUT
BUTTON = Pin(16, Pin.IN)	# creating Push Button object, setting it as IN

# continuously read the signal from the push button while the board has power
while True:
    # if the signal from the button is HIGH (button is pressed), turn LED on
    if BUTTON.value() == 1:
        LED.on()
        sleep(0.1)
        
    # otherwise, turn the LED off
    else:
        LED.off()
