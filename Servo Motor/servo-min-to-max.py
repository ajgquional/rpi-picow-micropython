# ================================================== 
""" 
Project objective: Gradually move the servo arm to its min to max position (at 100 increments) and vice-versa

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

# continuously and gradually move the servo arm from min to max position (and vice-versa) at 100 increments (for a duration of 0.01 sec each increment)
while True:
    # moving from min to max
    for i in range(0, 100):
        servo.value = i / 100
        sleep(0.01)

    # moving from max to min
    for i in range(100, 0, -1):
        servo.value = i / 100
        sleep(0.01)
