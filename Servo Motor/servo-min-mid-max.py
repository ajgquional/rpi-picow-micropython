# Project objective: Swing the servo arm from min, mid, to max positions
#
# Hardware and connections used:
#   Servo GND to Raspberry Pi Pico GND
#   Servo V+ to Raspberry Pi Pico 3.3 V
#   Servo PWM pin to GPIO Pin 15
# 
# Programmer: Adrian Josele G. Quional

# modules
from picozero import Servo	# importing Servo class to easily control the servo motor
from time import sleep

# creating a Servo object
servo = Servo(15)

# continuously swing the servo arm to min, mid, and max positions (for a duration of 1 sec each)
while True:
    # swinging the servo arm to its min position
    servo.min()
    sleep(1)

    # swinging the servo arm to its mid position
    servo.mid()
    sleep(1)

    # swinging the servo arm to its max position
    servo.max()
    sleep(1)