# ==================================================
"""
Project objective: Blink four external LEDs connected to the Raspberry Pi Pico W

Hardware and connections used:
    Anode of four LEDs to GPIO pins 6-9 of Raspberry Pi Pico W
    220 ohm resistor connected in series to each LED

Author: Adrian Josele G. Quional
"""
# ==================================================

# modules
from machine import Pin
from time import sleep

# setting GPIO Pins 6-9 as OUT
# note: any GPIO pin can be used
LED1 = Pin(6, Pin.OUT)
LED2 = Pin(7, Pin.OUT)
LED3 = Pin(8, Pin.OUT)
LED4 = Pin(9, Pin.OUT)

# continuously blink all 4 LEDs at the same time while the board has power
while True:
    LED1.on()
    LED2.on()
    LED3.on()
    LED4.on()
    sleep(1)

    LED1.off()
    LED2.off()
    LED3.off()
    LED4.off()
    sleep(1)
