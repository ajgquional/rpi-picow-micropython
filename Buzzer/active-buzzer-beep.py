# ================================================== 
""" 
Project objective: To test an active buzzer to play an alarm sound at one second interval

Hardware and connections used:
    Active buzzer GND to Raspberry Pi Pico GND
    Active buzzer + Pin to GPIO Pin 15

Author: Adrian Josele G. Quional
"""
# ==================================================

# if active buzzer is used, import the Buzzer class from picozero
from picozero import Buzzer
from time import sleep

# creating a Buzzer object
buzzer = Buzzer(15)

# continuously beep at 1 sec interval while the board has power
while True:
    buzzer.on()
    sleep(1)
    buzzer.off()
    sleep(1)
