# Guide to working with the Raspberry Pi Pico W

### Hardware specifications:
* RP2040 microcontroller chip designed by Raspberry Pi in the United Kingdom
* Dual-core Arm Cortex M0+ processor, flexible clock running up to 133 MHz
* 264kB of SRAM, and 2MB of on-board flash memory
* USB 1.1 with device and host support
* Low-power sleep and dormant modes
* Drag-and-drop programming using mass storage over USB
* 26 × multi-function GPIO pins
* 2 × SPI, 2 × I2C, 2 × UART, 3 × 12-bit ADC, 16 × controllable PWM channels
* Accurate clock and timer on-chip
* Temperature sensor
* Accelerated floating-point libraries on-chip
* 8 × Programmable I/O (PIO) state machines for custom peripheral support
* On-board single-band 2.4GHz wireless interfaces (802.11n) using the Infineon CYW43439

### Pinout:

<p align='center'>
  <img src="https://www.raspberrypi.com/documentation/microcontrollers/images/pico-pinout.svg" alt="Raspberry Pi Pico W Pinout">
</p>

### Getting started with programming the Raspberry Pi Pico W:

1. Download the MicroPython firmware for Raspberry Pi Pico W (link: https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2).
2. Push and hold the BOOTSEL button and plug your Pico W into the USB port of your computer. Release the BOOTSEL button after your Pico W is connected. It will mount as a Mass Storage Device called RPI-RP2.
3. Drag and drop (or copy and paste) the MicroPython UF2 file onto the RPI-RP2 volume. Your Pico W will reboot. You are now running MicroPython.
4. Install Thonny IDE (link: https://thonny.org/).
5. Once Thonny is installed, open it. If Pico W is still plugged in into the computer, you should see on the lower right corner of the Thonny IDE that the Pico W is detected. Also, you would see that the Thonny shell is active and it says which MicroPython version is installed in your Pico W.
6. To test if the MicroPython is really detected, type the command `print("Hello world!")` in the Thonny shell then press enter. If the text is printed after you entered the command, it means that you have successfully installed MicroPython to Raspberry Pi Pico W. Congratulations!

### Running scripts/programs in the Raspberry Pi Pico W:

1. Open a script that you wanted Raspberry Pi Pico W to run (for instance, you may open the standard <a href="https://github.com/ajgquional/rpi-picow-micropython/blob/5d93332fbf7df72a722749734f5b3f13ae6fe678/Blink/blink.py">blink.py</a>).
2. To run a script, click the green play button in the toolbar on top. You should see a notification in the Thonny shell below that the script is running and (if you have used the Blink program) you should see the onboard LED of the Raspberry Pi Pico W blinking.
3. To stop the script, click the red stop button in the toolbar on top.

### Downloading a program and running it by default when power is given to Raspberry Pi Pico W:

Once a script is run by the board, it doesn't automatically mean that it would run by default when power is given to the board. This is in contrast with downloading a sketch in an Arduino board. To enable the board run a script by default when power is given, the script must be saved to the Raspberry Pi Pico W itself. The steps are as follows:

1. If a script is running, stop the script.
2. Click "File" on the upper left corner of the Thonny IDE then click "Save as."

### Installing modules to the Raspberry Pi Pico W:

### Useful links:
* Raspberry Pi Pico and Pico W Documentation: https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html
* MicroPython Documentation: https://docs.micropython.org/en/latest/index.html
* picozero Documentation: https://picozero.readthedocs.io/en/latest/index.html

# Notes on this repository:
* Each directory contains MicroPython programs, README files (containing circuit diagrams, Wokwi simulation links, and other notes), Fritzing files, and/or steps to implement the project/program contained within the folder.
* Each directory is themed according to the device interfaced with the Raspberry Pi Pico W or on an overarching project theme. To specify, the directories are described as follows:
  * <b>Analog IO</b> - contains files related to the use of analog components, such as the potentiometer (analog input) and using PWM to control LED brightness (analog     output)
  * <b>Blink</b> - contains files related to the use of LEDs (and the programs contained in the directory would just make the LEDs simply turn on or off)
  * <b>Buzzer</b> - contains files related to the use of active and passive buzzers
  * <b>DHT</b> - contains files related to the use of DHT11/22 Sensor
  * <b>LCD I2C</b> - contains files related to the use of an LCD screen with I2C adaptor
  * <b>LDR</b> - contains files related to the use of a photoresistor/LDR
  * <b>Liquid Level Sensor</b> - contains files related to the use of an HW-038 Water/Liquid Level Sensor
  * <b>PIR</b> - contains files related to the use of a HC-SR501 Passive Infrared (thus, PIR) Sensor
  * <b>Push Button</b> - contains files related to the use of push buttons
  * <b>Servo Motor</b> - contains files related to the use of servo motors
  * <b>Ultrasonic Distance Sensor</b> - contains files related to the use of an HC-SR04 Ultrasonic Distance Sensor
  * <b>Web</b> - contains several directories containing files interfacing Raspberry Pi Pico W to the web (additional details are contained in the README file of that      directory)
* Programs would work for both Raspberry Pi Pico and Pico W, except for programs blinking the onboard LED which is accessed differently for Pico and Pico W (check comments on  <a href="https://github.com/ajgquional/rpi-picow-micropython/blob/5d93332fbf7df72a722749734f5b3f13ae6fe678/Blink/blink.py">blink.py</a>) and for web-related projects which are obviously only for Pico W (having a WiFi module).
* Only Raspberry Pi Pico is used in Wokwi simulations since Pico W is not yet available in Wokwi. Should it become available in Wokwi, simulations would be updated to use Raspberry Pi Pico W.  
* Contents of this repository would definitely be updated as more devices are interafaced and verified to work with Raspberry Pi Pico W. 
