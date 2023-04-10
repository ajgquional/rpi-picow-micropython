# ==================================================
"""
Project objectives: 
    Read inputs from the potentiometer and display values to the console
    Convert analog values to voltage then display it to the console

Hardware and connections used:
    Potentiometer SIG pin to GPIO Pin 28 (capable of ADC)

Author: Adrian Josele G. Quional
"""
# ==================================================

# modules
from machine import Pin, ADC    # ADC class is needed to create an ADC object
from time import sleep

# creating an ADC object, specifying GPIO Pin 28 as the INPUT pin
adc = ADC(Pin(28))
# Note: GPIO Pins capable of ADC are GPIO Pin 26-28 only

# continuously read data from the potentiometer and display the values to the console
while True:
    # reading analog values from the potentiometer
    analog_value = adc.read_u16()
    print(f"Analog value: {analog_value}")

    # converting analog values to voltage
    voltage = analog_value * (3.3 / 65535)
    print(f"Voltage: {voltage}")

    print("==========")
    sleep(1)
