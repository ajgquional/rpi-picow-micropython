# Project objective: Blink the onboard LED of the Raspberry Pi Pico W using the Picozero module
# Programmer: Adrian Josele G. Quional

# modules
from picozero import pico_led
from time import sleep

# continuously blink the onboard LED for an interval of 1 sec while the board has power
while True:
    pico_led.on()	# turn on LED
    sleep(1)		# wait for 1 sec
    pico_led.off()	# turn off LED
    sleep(1)		# wait for 1 sec