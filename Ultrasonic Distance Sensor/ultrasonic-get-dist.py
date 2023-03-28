# Project object: Acquire distance measurements and print the values to the console
#
# Hardware and connections used:
#   Ultrasonic Distance Sensor VCC to 3.3 V
#   Ultrasonic Distance Sensor to GND
#   Ultrasonic Distance Sensor TRIG Pin to GPIO Pin 15
#   Ultrasonic Distance Sensor ECHO Pin to GPIO Pin 14
#
# Programmer: Adrian Josele G. Quional

# modules
from picozero import DistanceSensor     # importing the DistanceSensor class to easily handle distance calculations
from time import sleep

# creating a DistanceSensor object and specifying ECHO and TRIG pins
# any GPIO pin can be used for echo and trigger
ds = DistanceSensor(echo=14, trigger=15)

# continuously acquire distance measurements while the board has power
while True:
    # printing the values to the console
    # values are converted to cm because distance method returns values in m
    # conversion factor used is 100 cm = 1 m
    distance_cm = ds.distance * 100
    print(f"Distance: {distance_cm} cm")
    sleep(0.1)