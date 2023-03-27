# Project objective: Control the brightness of an LED using a potentiometer
# 
# Hardware and connections used:
#   LED to GPIO Pin 15
#   220 ohm resistor for the LED
#   Potentiometer SIG pin to GPIO Pin 28 (capable of ADC)
#
# Programmer: Adrian Josele G. Quional

# modules
from machine import Pin, PWM, ADC
from time import sleep

# creating PWM and ADC objects
pwm = PWM(Pin(15))
adc = ADC(Pin(28))

# setting frequency of PWM output
pwm.freq(1000)

# continuously control the brightness of the LED using the potentiometer
while True:
    # reading analog values from the potentiometer
    duty = adc.read_u16()
    # writing analog values to the LED
    pwm.duty_u16(duty)