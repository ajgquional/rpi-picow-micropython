# Project objective: Blink four external LEDs connected to the Raspberry Pi Pico W using for loop
#
# Hardware and connections used:
#   Anode of four LEDs to GPIO pins 6-9 of Raspberry Pi Pico W
#   220 ohm resistor connected in series to each LED
#
# Programmer: Adrian Josele G. Quional

# modules
from machine import Pin
from time import sleep

# empty list to hold the LED objects
LEDS = []

# storing each LED object (set as OUT) in the LEDS list using append method
for LED in range(6, 10):
    LEDS.append(Pin(LED, Pin.OUT))

# continuously blink all 4 LEDs at the same time while the board has power
while True:
    # turning on all 4 LEDs at the same time then a 1 sec delay before turning them off
    for LED in LEDS:
        LED.on()
    sleep(1)

    # turning off all 4 LEDs at the same time then a 1 sec delay before turning them on
    for LED in LEDS:
        LED.off()
    sleep(1)
