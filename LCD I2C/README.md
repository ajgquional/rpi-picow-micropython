# Wokwi Raspberry Pi Pico Simulation Link

* <b> LCD I2C Hello World Display </b> https://wokwi.com/projects/357957814062447617

# Circuit diagram: LCD Screen (I2C) to Raspberry Pi Pico W

<p align="center">
  <img src="https://github.com/ajgquional/rpi-picow-micropython/blob/95661b0e89008af8ca759816827d58919eba89a5/LCD%20I2C/LCD-I2C-to-RPi-Pico-W_bb.png" alt="Circuit diagram - LCD Screen (I2C) conencted to Raspberry Pi Pico W">
</p>

# Notes on working with the LCD screen (using I2C)
* To provide power to the LCD screen, use VBUS Pin of the Raspberry Pi Pico/Pico W. This is directly connected to the micro-USB and is 5 V. Based on experiments, 3.3 V from the board itself cannot provide sufficient power to the screen (although in the simulaiton, it's possible). Note however that VBUS should only be strictly used to power the LCD screen, not to the whole circuit if there are other components interfaced to the board as the board can't take in 5 V.
* In terms of software, make sure to save first the two modules inside of Raspberry Pi Pico/Pico W. Specifically, the modules used in this implementation are lcd_api.py and pico_i2c_lcd.py. These are not available in Thonny; thus, these modules need to be manually saved in the board (see README file in the main directory for guidance).
* Other modules can be used to be able to work with the LCD screen. In this case, you have to know the specific methods to use to be display text on the screen.
* In terms of connections, other SDA and SCL pins of the Raspberry Pi Pico/Pico W can be used (refer to Raspberry Pi Pico/Pico W documentation for GPIO pins that are also SDA and SCL pins).
