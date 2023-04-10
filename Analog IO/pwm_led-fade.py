# ================================================== 
"""
Project objective: Fade the light of an external LED using PWM
 
Hardware and connections used:
    LED to GPIO Pin 15
    220 ohm resistor for the LED

Author: Adrian Josele G. Quional
"""
# ================================================== 

# modules
from machine import Pin, PWM	# PWM class is needed to create a PWM object
from time import sleep

# creating a PWM object, specifying GPIO Pin 15 as OUT
pwm = PWM(Pin(15))
# Note: pins that support PWM are 
#   GPIO0, GPIO2, GPIO4, GPIO5, GPIO10, GPIO12-19, GPIO21, GPIO22, GPIO23, GPIO25-27

# setting frequency of PWM output at 1000 Hz
pwm.freq(1000)

# continuously fade the brightness of the LED
while True:
    # gradually turns the LED on
    # 65535 is the maximum analog value (max voltage)
    # 65025 would also worked, as per Raspberry Pi Projects website
    for duty in range(65535):
        pwm.duty_u16(duty)
        sleep(0.0001)
    
    # gradually turns the LED off
    # 65535 slowly decrements to 0
    for duty in range(65535, 0, -1):
        pwm.duty_u16(duty)
        sleep(0.0001)
