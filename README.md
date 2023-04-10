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

#### Installing the MicroPython firmware:

1. Download the MicroPython firmware for Raspberry Pi Pico W (link: https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2).
2. Push and hold the BOOTSEL button and plug your Pico W into the USB port of your computer. Release the BOOTSEL button after your Pico W is connected. It will mount as a Mass Storage Device called RPI-RP2.
3. Drag and drop (or copy and paste) the MicroPython UF2 file onto the RPI-RP2 volume. Your Pico W will reboot. It is now running MicroPython.

#### Installing the Thonny IDE:

4. Install Thonny IDE (link: https://thonny.org/).
5. Once Thonny is installed, open it. If Pico W is still plugged in into the computer, you should see on the lower right corner of the Thonny IDE that the Pico W is detected. Also, you would see that the Thonny shell is active and it says which MicroPython version is installed in your Pico W.

<p align='center'>
  <img src="https://github.com/ajgquional/rpi-picow-micropython/blob/4c4db31205459c176ff2e62cea10394aa111f15a/RPi-Pico-W-Detected.png" alt="RPi Pico W Detected">
</p>

6. To test if the MicroPython is really detected, type the command `print("Hello world!")` in the Thonny shell then press enter. If the text is printed after you've entered the command, it means that you have successfully installed MicroPython to Raspberry Pi Pico W. Congratulations! You can now program your Pico W!

<p align='center'>
  <img src="https://github.com/ajgquional/rpi-picow-micropython/blob/4c4db31205459c176ff2e62cea10394aa111f15a/MicroPython-Hello-World-Test.png" alt="MicroPython Hello World Test">
</p>

### Running scripts/programs in the Raspberry Pi Pico W:

1. Open a script that you wanted Raspberry Pi Pico W to run (for instance, you may open the standard <a href="https://github.com/ajgquional/rpi-picow-micropython/blob/5d93332fbf7df72a722749734f5b3f13ae6fe678/Blink/blink.py">blink.py</a>).
2. To run a script, click the green play button in the toolbar on top. You should see a notification in the Thonny shell below that the script is running and (if you have used the Blink program) you should see the onboard LED of the Raspberry Pi Pico W blinking.
3. To stop the script, click the red stop button in the toolbar on top.

<p align='center'>
  <img src="https://github.com/ajgquional/rpi-picow-micropython/blob/4c4db31205459c176ff2e62cea10394aa111f15a/RPi-Pico-W-Run-Script.png" alt="Running and stopping scripts in RPi Pico W">
</p>

### Downloading a program and running it by default when power is given to Raspberry Pi Pico W:

Once a script is run by the board, it doesn't automatically mean that it would run by default when power is given to the board. This is in contrast with downloading a sketch in an Arduino board where the sketch would automatically run when the Arduino board is given power (via the DC jack) disconnected from the computer. To enable the board to run a script by default when power is given to it, the script must be saved to the Raspberry Pi Pico W itself. The steps are as follows:

1. If a script is running, stop the script.
2. Click "File" on the upper left corner of the Menu Bar of the Thonny IDE then click "Save as."
3. A new window would appear asking where the script must be saved. Choose "Raspberry Pi Pico."

<p align='center'>
  <img src="https://github.com/ajgquional/rpi-picow-micropython/blob/4c4db31205459c176ff2e62cea10394aa111f15a/Saving-to-RPi-Pico-W-Part1.png" alt="Saving to RPi Pico W Part 1">
</p>

4. Afterwards, a new window would appear allowing you to type the file name for the script. Type <b>main.py</b> as the file name (this is the required file name to enable the Pico W to automatically run the script). Press OK. (Additional note: There is a "lib" folder when you save the script to Raspberry Pi Pico W. This is just the folder where the modules, installed in Pico W, would be located.)

<p align='center'>
  <img src="https://github.com/ajgquional/rpi-picow-micropython/blob/4c4db31205459c176ff2e62cea10394aa111f15a/Saving-to-RPi-Pico-W-Part2.png" alt="Saving to RPi Pico W Part 2">
</p>

5. To verify that the script is already saved (as main.py) in Pico W, the file name displayed on the script tab above the actual script would change to `[main.py]` (emphasis on the square brackets). Also, if you enable the "Files" view to see the files (to be displayed as a sidebar to the left) in both the computer and Raspberry Pi Pico, you would see the file "main.py." (Note: To enable "Files" view, click "View" in the Menu Bar on top then click "Files.")

<p align='center'>
  <img src="https://github.com/ajgquional/rpi-picow-micropython/blob/4c4db31205459c176ff2e62cea10394aa111f15a/Saving-to-RPi-Pico-W-Part3.png" alt="Saving to RPi Pico W Part 3">
</p>

6. As a final verification, disconnect the Pico W from your computer then plug it again. At the instance that power is applied to the board, Pico W will run the saved script. If the standard blink.py is saved as main.py, you would that the onboard LED of the Pico W blinking every second. Congratulations! You now know how to save a script to the Pico W!

### Installing modules to the Raspberry Pi Pico W (feat. picozero module):

To install modules to the Raspberry Pi Pico W, first make sure that the board is plugged in to your computer. Then, you may follow any of the steps below.

#### Via Tools menu in Thonny:

1. Click on Tools in the Menu Bar on top of the Thonny IDE then click "Manage Packages." A window would then appear showing the instructions how to install a module.
2. In the search bar, type picozero then press enter or click "Search on PyPI."
3. The module name that you have typed will appear in the selection. Click picozero. It would show the details of the module that you have selected. Once you have verified that it's the module that you wanted to install, click "Install" on the lower part of the window.
4. A progress window would then appear showing the status of the installation. After installation, the progress window would disappear and you would see picozero in the left sidebar of the package manager window which shows the modules already installed. Furthermore, when picozero is selected, there are two options that appeared on the lower part of the window - "Upgrade" and "Uninstall" - rather than just "Install." This indicates that picozero is already installed in Pico W.
5. As a last verification that picozero is already installed, show the files that are contained in Pico W (see Step 5 above to know how to enable the "Files" view) and you would see that inside the "lib" folder, there are picozero folders saved. Congratulations! You can now use the picozero module in your Pico W. (Note: Should you wish to install other modules, you can follow the same process.) 

#### Via manual saving:

1. Look for the actual Python code of the module that you wanted to save in Pico W. For picozero, the code can be found here: https://raw.githubusercontent.com/RaspberryPiFoundation/picozero/master/picozero/picozero.py?token=GHSAT0AAAAAABRLTKWZDBSYBE54NJ7AIZ6MYSENI2A
2. Copy and paste the entire code as a new file in Thonny.
3. Save the file to Raspberry Pi Pico. Go inside the "lib" folder, and in there, save the file as "picozero.py."
4. As a verification, you would see, when the "Files" view is enabled, that "picozero.py" is saved under the lib folder.
5. As a final verification, open <a href="https://github.com/ajgquional/rpi-picow-micropython/blob/fbb70b24b01a84577c0d2e0c3a9aa24f74f51ccb/Blink/blink_picozero.py">blink_picozero.py</a> then run it. You should see that the onboard LED of Pico W blinking. (Note: Should you wish to install other modules not available via the Thonny Package Manager, you can follow the same process, outlined here, to install the necessary module/s.) 

### Useful links:
* <b>Raspberry Pi Pico/Pico W Documentation:</b> https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html
* <b>MicroPython Documentation:</b> https://docs.micropython.org/en/latest/index.html
* <b>picozero Documentation:</b> https://picozero.readthedocs.io/en/latest/index.html
* <b>Arduino Labs for MicroPython (should you wish to use "Arduino" for MicroPython):</b> https://labs.arduino.cc/en/labs/micropython

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
