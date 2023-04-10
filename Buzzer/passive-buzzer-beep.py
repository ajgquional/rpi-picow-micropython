# ================================================== 
""" 
Project objective: To test a passive buzzer to play an alarm sound at one second interval

Hardware and connections used:
    Passive buzzer GND to Raspberry Pi Pico GND
    Passive buzzer + Pin to GPIO Pin 15

Author: Adrian Josele G. Quional
"""
# ==================================================

# if passive buzzer is used, import the Speaker class from picozero
from picozero import Speaker
from time import sleep

# creating a Speaker object
speaker = Speaker(15)

# continuously beep at 1 sec interval while the board has power
# note: a passive buzzer can also be used to play different tones
while True:
    speaker.on()
    sleep(1)
    speaker.off()
    sleep(1)
