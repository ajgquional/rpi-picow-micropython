# ================================================== 
""" 
Project objective: Pulse the servo from its min to max position and vice-versa

Hardware and connections used:
    Servo GND to Raspberry Pi Pico W GND
    Servo V+ to Raspberry Pi Pico W 3.3 V
    Servo PWM pin to GPIO Pin 15
 
Author: Adrian Josele G. Quional
"""
# ==================================================

# modules
from picozero import Servo  # importing Servo class to easily control the servo motor
from time import sleep

# creating a Servo object
servo = Servo(15)

# continuously pulse the servo arm from min to max position (and vice-versa) for a duration of 1 sec
while True:
    servo.pulse()
    sleep(1)
