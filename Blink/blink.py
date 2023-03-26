# Project objective: Blink the onboard LED of the Raspberry Pi Pico W
# Programmer: Adrian Josele G. Quional

# modules
from machine import Pin # to be able to work with the hardware
from time import sleep	# to add delays in the program

# Setting the pin mode to OUT
# Pin 25 (GP25) is the onboard LED in Raspberry Pi Pico W
# for Raspberry Pi Pico
# LED_PIN = Pin(25, Pin.OUT)

# for Raspberry Pi Pico W
LED = Pin("LED", Pin.OUT)

# continuously blink the onboard LED for an interval of 1 sec while the board has power
while True:
    LED.on()	# turn on LED
    sleep(1)	# wait for 1 sec
    LED.off()	# turn off LED
    sleep(1)	# wait for 1 sec