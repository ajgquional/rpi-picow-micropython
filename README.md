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
  <img src="https://www.raspberrypi.com/documentation/microcontrollers/images/picow-pinout.svg" alt="Raspberry Pi Pico W Pinout">
</p>

<b>Interactive Raspberry Pi Pico Pinout:</b> https://pico.pinout.xyz/

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

#### Via the Tools menu in Thonny:

1. Click on Tools in the Menu Bar on top of the Thonny IDE then click "Manage Packages." A window would then appear showing the instructions how to install a module.

<p align='center'>
  <img src="https://github.com/ajgquional/rpi-picow-micropython/blob/4ea81efc9646a1d7f4095579e5a0e62de02f18ca/Installing-picozero-via-Tools-Part1.png" alt="Installing picozero via Tools Part 1">
</p>

<p align='center'>
  <img src="https://github.com/ajgquional/rpi-picow-micropython/blob/4ea81efc9646a1d7f4095579e5a0e62de02f18ca/Installing-picozero-via-Tools-Part2.png" alt="Installing picozero via Tools Part 2">
</p>

2. In the search bar, type <b>picozero</b> then press enter or click "Search on PyPI."

<p align='center'>
  <img src="https://github.com/ajgquional/rpi-picow-micropython/blob/4ea81efc9646a1d7f4095579e5a0e62de02f18ca/Installing-picozero-via-Tools-Part3.png" alt="Installing picozero via Tools Part 3">
</p>

3. The module name that you have typed will appear in the selection. Click picozero. It would show the details of the module that you have selected. Once you have verified that it's the module that you wanted to install, click "Install" on the lower part of the window.

<p align='center'>
  <img src="https://github.com/ajgquional/rpi-picow-micropython/blob/4ea81efc9646a1d7f4095579e5a0e62de02f18ca/Installing-picozero-via-Tools-Part4.png" alt="Installing picozero via Tools Part 4">
</p>

4. A progress window would then appear showing the status of the installation. After installation, the progress window would disappear and you would see picozero in the left sidebar of the package manager window which shows the modules already installed. Furthermore, when picozero is selected, there are two options that will appear on the lower part of the window - "Upgrade" and "Uninstall" - rather than just "Install." This is another indication that picozero is already installed in Pico W.

<p align='center'>
  <img src="https://github.com/ajgquional/rpi-picow-micropython/blob/4ea81efc9646a1d7f4095579e5a0e62de02f18ca/Installing-picozero-via-Tools-Part5.png" alt="Installing picozero via Tools Part 5">
</p>

<p align='center'>
  <img src="https://github.com/ajgquional/rpi-picow-micropython/blob/4ea81efc9646a1d7f4095579e5a0e62de02f18ca/Installing-picozero-via-Tools-Part6.png" alt="Installing picozero via Tools Part 6">
</p>

5. As a last verification that picozero is already installed, show the files that are contained in Pico W (see Step 5 above to know how to enable the "Files" view) and you would see that inside the "lib" folder, there are picozero folders saved. Congratulations! You can now use the picozero module in your Pico W. (Note: Should you wish to install other modules, you can follow the same process.) 

<p align='center'>
  <img src="https://github.com/ajgquional/rpi-picow-micropython/blob/4ea81efc9646a1d7f4095579e5a0e62de02f18ca/Installing-picozero-via-Tools-Part7.png" alt="Installing picozero via Tools Part 7">
</p>

#### Via manual saving:

1. Look for the actual Python code of the module that you wanted to save in Pico W. For picozero, the code can be found here: https://raw.githubusercontent.com/RaspberryPiFoundation/picozero/master/picozero/picozero.py?token=GHSAT0AAAAAABRLTKWZDBSYBE54NJ7AIZ6MYSENI2A
2. Copy and paste the entire code as a new file in Thonny.

<p align='center'>
  <img src="https://github.com/ajgquional/rpi-picow-micropython/blob/c573783918e1939c8e655ad0c7c3f9f20beb1ad2/Installing-picozero-via-manual-saving-Part1.png" alt="Installing picozero via manual saving Part 1">
</p>

3. Save the file to Raspberry Pi Pico. Go inside the "lib" folder, and in there, save the file as "picozero.py."

<p align='center'>
  <img src="https://github.com/ajgquional/rpi-picow-micropython/blob/c573783918e1939c8e655ad0c7c3f9f20beb1ad2/Installing-picozero-via-manual-saving-Part2.png" alt="Installing picozero via manual saving Part 2">
</p>

4. As a verification, you would see, when the "Files" view is enabled, that "picozero.py" is saved under the lib folder.

<p align='center'>
  <img src="https://github.com/ajgquional/rpi-picow-micropython/blob/c573783918e1939c8e655ad0c7c3f9f20beb1ad2/Installing-picozero-via-manual-saving-Part3.png" alt="Installing picozero via manual saving Part 3">
</p>

5. As a final verification, open <a href="https://github.com/ajgquional/rpi-picow-micropython/blob/fbb70b24b01a84577c0d2e0c3a9aa24f74f51ccb/Blink/blink_picozero.py">blink_picozero.py</a> then run it. You should see that the onboard LED of Pico W blinking. (Note: Should you wish to install other modules not available via the Thonny Package Manager, you can follow the same process, outlined here, to install the necessary module/s.)

#### Final notes about the installation of modules:
* The first method (via the Thonny Package Manager) is the most convenient; however, if the modules you're looking for aren't available in the package manager, then you can't use this method.
* The second method (manual saving) is more flexible but is more tedious. You should use this method only if the modules that you wanted to install aren't available in the Thonny Package Manager (such as some LCD modules). 

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
* Programs would work for both Raspberry Pi Pico and Pico W, except for programs blinking the onboard LED which is accessed differently for Pico and Pico W if purely using the machine library (check comments on  <a href="https://github.com/ajgquional/rpi-picow-micropython/blob/5d93332fbf7df72a722749734f5b3f13ae6fe678/Blink/blink.py">blink.py</a>) and for web-related projects which are obviously only for Pico W (having a WiFi module).
* Only Raspberry Pi Pico is used in Wokwi simulations since Pico W is not yet available in Wokwi. Should it become available in Wokwi, simulations would be updated to use Raspberry Pi Pico W.  
* Contents of this repository would definitely be updated as more devices are interfaced and verified to work with the Raspberry Pi Pico W. 
* Disregard the images (detailing the steps to get started with Pico W) uploaded in the main directory. They are only uploaded to be used for this README file.

# Collection of web articles/references on Raspberry Pi Pico/Pico W:
* <a href="https://www.hackster.io/news/pi-pico-sdk-1-5-0-release-adds-bluetooth-support-7fe4d09da432?f8e8b1feff822753a39b21de69259fd6">Pi Pico SDK 1.5.0 Release Adds Bluetooth Support</a>
* <a href="https://www.hackster.io/news/vlad-tomoiaga-s-fakepga-turns-a-raspberry-pi-pico-or-other-rp2040-board-into-a-slow-cheap-fpga-91f3cc98072c">Vlad Tomoiagă's FakePGA Turns a Raspberry Pi Pico or Other RP2040 Board Into a Slow, Cheap "FPGA"</a>
* <a href="https://www.hackster.io/news/the-raspberry-pi-pico-installer-is-a-one-shot-way-to-set-up-an-rp2040-toolchain-on-windows-a905eb5ce1ec">The Raspberry Pi Pico Installer Is a One-Shot Way to Set Up an RP2040 Toolchain on Windows</a>
* <a href="https://www.raspberrypi.com/news/did-i-close-the-garage-door-let-raspberry-pi-check-for-you/">Did I close the garage door? Let Raspberry Pi check for you</a>
* <a href="https://www.arm.com/resources/education/schools/content/raspberry-pi-pico-for-schools?fbclid=IwAR3bsCCkbVTrXIwRZH2imGxXU_SvYRvnNDKMAsK5frxmR6vZxRfoZDUv6f8">Raspberry Pi Pico Projects for Schools</a>
* <a href="https://www.hackster.io/news/adafruit-s-picowbell-adalogger-turns-a-raspberry-pi-pico-or-pico-w-into-a-compact-datalogger-a59654f13ce5">Adafruit's PiCowbell Adalogger Turns a Raspberry Pi Pico or Pico W Into a Compact Datalogger</a>
* <a href="https://www.raspberrypi.com/news/theremin-like-pico-h-musical-instrument/">Theremin-like Pico H musical instrument</a>
* <a href="https://resources.embeddedcomputing.com/Embedded-Computing-Design/Capacitive-Touch-Input-With-the-Raspberry-Pi-RP2040-Pico">Capacitive Touch Input With the Raspberry Pi RP2040 Pico</a>
* <a href="https://www.raspberrypi.com/news/scottoergo-ergonomic-hand-wired-keyboard/">ScottoErgo: ergonomic hand-wired keyboard</a>
* <a href="https://www.hackster.io/news/micropython-1-20-0-launches-with-mip-a-dedicated-package-manager-and-raspberry-pi-pico-w-support-258033aa9d45?a1255c9dbdcd635143d172dee1b8c0fe">MicroPython 1.20.0 Launches with Mip, a Dedicated Package Manager, and Raspberry Pi Pico W Support</a>
* <a href="https://www.hackster.io/news/philip-howard-s-raspberry-pi-pico-gpio-pinout-python-program-prints-pins-at-your-terminal-6bbd42792975">Philip Howard's Raspberry Pi Pico GPIO Pinout Python Program Prints Pins at Your Terminal</a>
* <a href="https://www.deeplearning.ai/the-batch/how-to-run-pilotnet-on-a-raspberry-pi-pico-microcontroller/?utm_campaign=The%20Batch&utm_content=250169984&utm_medium=social&utm_source=facebook&hss_channel=fbp-1027125564106325">Deep Learning at (Small) Scale: How to run PilotNet on a Raspberry Pi Pico microcontroller</a>
* <a href="https://www.digikey.com/en/articles/getting-started-raspberry-pi-pico-multicore-microcontroller-board?fbclid=IwAR1LiYSri3n3fgemzMgCNmJPHntmQ_a-XreTN4mENiztzaW8HGSkePLO0u0">Getting Started with the Raspberry Pi Pico Multicore Microcontroller Board Using C</a>
* <a href="https://www.hackster.io/news/milk-v-unveils-its-third-risc-v-board-in-a-month-the-9-dual-core-linux-capable-milk-v-duo-3fb5d9f978d1">Milk-V Unveils Its Third RISC-V Board in a Month: The $9 Dual-Core Linux-Capable Milk-V Duo [Raspberry Pi Pico-inspired]</a>
* <a href="https://www.raspberrypi.com/news/new-functionality-bluetooth-for-pico-w/">New functionality: Bluetooth for Pico W</a>
* <a href="https://www.hackster.io/news/raspberry-pi-gives-the-pico-w-a-bluetooth-boost-classic-and-ble-modes-now-available-in-micropython-5a988ae38c64">Raspberry Pi Gives the Pico W a Bluetooth Boost, Classic and BLE Modes Now Available in MicroPython</a>
* <a href="https://www.digikey.com/en/maker/projects/generating-text-with-chatgpt-pico-w-circuitpython/12dee4ec06a94877a2ca86a021d6df69?fbclid=IwAR3vKsLm2NfW9XlIxWfq4VTcPvCDgOLmKM29rq5GxXFIOCICvudNoUHyCVY">Generating Text with ChatGPT, Pico W, & CircuitPython</a>
* <a href="https://www.hackster.io/news/open-source-experiential-robotics-platform-xrp-kit-now-available-for-pre-order-c9cfebedc1ff?fbclid=IwAR3nUlEWlrHERHP4QWPVkX2-U0RWn7NOLJfhWLEWs_mS9ZnNOCuuJ-hPZ9Q">Open Source Experiential Robotics Platform (XRP) Kit Now Available for Pre-Order</a>
* <a href="https://www.hackster.io/news/gary-sims-piccolobasic-is-a-minimalist-programming-language-for-the-raspberry-pi-pico-rp2040-3a53ec2fc684">Gary Sims' PiccoloBASIC Is a Minimalist Programming Language for the Raspberry Pi Pico, RP2040</a>
* <a href="https://www.raspberrypi.com/news/gps-pothole-tracker/">GPS pothole tracker</a>
* <a href="https://www.raspberrypi.com/news/set-sail-in-the-pico-powered-roboat/">Set sail in the Pico-powered ‘Roboat’</a>
* <a href="https://www.hackster.io/news/set-sail-with-the-raspberry-pi-pico-w-5c581fbc4c62">Set Sail with the Raspberry Pi Pico W</a>
* <a href="https://www.raspberrypi.com/news/autoflash-multiple-raspberry-pi-picos-in-no-time-at-all/">Autoflash multiple Raspberry Pi Picos in no time at all</a>
* <a href="https://www.hackster.io/news/mark-stevens-picodebugger-aims-to-make-picoprobe-debugging-tidier-neater-and-more-flexible-6d6846368182">Mark Stevens' PicoDebugger Aims to Make PicoProbe Debugging Tidier, Neater, and More Flexible</a>
* <a href="https://www.raspberrypi.com/news/pico-powered-chess-robot-plays-dirty-using-chatgpt/">Pico-powered chess robot plays dirty using ChatGPT</a>
* <a href="https://www.hackster.io/news/phil-barrett-s-picocnc-aims-to-provide-professional-laser-lathe-and-router-control-at-a-low-cost-36ea251b5acc?fbclid=IwAR1XdQc_5O7vZpN8ByI3eEDiD4Ouecx1SNPdF0ElBGsyEpsQgYrW3Opntyg">Phil Barrett's PicoCNC Aims to Provide Professional Laser, Lathe, and Router Control at a Low Cost</a>
* <a href="https://www.raspberrypi.com/news/how-i-made-the-picocray-hackspace-69/">How I made the PicoCray | HackSpace #69</a>
* <a href="https://www.hackster.io/news/rishin-goswami-s-picosiggen-aims-to-turn-a-raspberry-pi-pico-into-a-100ms-s-waveform-generator-124dc23de761">Rishin Goswami's PicoSigGen Aims to Turn a Raspberry Pi Pico Into a 100MS/s Waveform Generator</a>
* <a href="https://www.hackster.io/news/dmitry-grinberg-s-romram-adds-8mb-of-external-ram-to-the-humble-raspberry-pi-rp2040-27f2d7363f10?fbclid=IwAR2xuEl2nvlsQ9qP1XzTKCAdIbYWFC5Od8lpKjbjVvmtw6DAj_kuJgcR8oI">Dmitry Grinberg's ROMRAM Adds 8MB of External RAM to the Humble Raspberry Pi RP2040</a>
* <a href="https://www.raspberrypi.com/news/getting-to-grips-with-bluetooth-on-pico-w/">Getting to grips with Bluetooth on Pico W</a>
* <a href="https://www.hackster.io/news/buckle-up-for-adventure-f520fdb14bbf">Buckle Up for Adventure</a>
* <a href="https://www.raspberrypi.com/news/track-your-run-to-the-moon-with-a-raspberry-pi-powered-ladder/">Track your run to the Moon with a Raspberry Pi-powered ladder</a>
* <a href="https://blog.tindie.com/2023/09/pico-qwiicreset-prototyping-assistant/?fbclid=IwAR3EmyavUN-uFPt85tlJhUjCDX55YGYsjA-8U5uhF6hvPxh4lyLF5zdVwPc">Pico QwiicReset Prototyping Assistant</a>
* <a href="https://www.raspberrypi.com/news/this-pico-powered-belt-pulls-you-north/">This Pico-powered belt pulls you north</a>
* <a href="https://hackaday.com/2023/09/30/a-1970s-mask-rom-mcu-spills-its-secrets/">A 1970S MASK ROM MCU SPILLS ITS SECRETS</a>
* <a href="https://www.hackster.io/news/andre-costa-s-pico-w-air-is-a-raspberry-pi-pico-w-carrier-board-for-air-quality-monitoring-0ffea3cc7e36?fbclid=IwAR14sd7f4LIOz0smMs7soz0HgACo4-goGAJdUTZlUGusXHqaTThIBZr7gAM">André Costa's Pico W Air Is a Raspberry Pi Pico W Carrier Board for Air Quality Monitoring</a>
* <a href="https://www.hackster.io/news/tim-hanewich-s-scout-flight-controller-pushes-micropython-on-the-raspberry-pi-pico-to-the-limit-e475db41959e">Tim Hanewich's Scout Flight Controller Pushes MicroPython on the Raspberry Pi Pico to the Limit</a>
* <a href="https://hackaday.io/project/192152-handheld-linux-terminal-haliterm">Handheld Linux Terminal [HaLiTerm]</a>
* <a href="https://www.hackster.io/christophe-favergeon/synthesize-music-with-animations-on-a-raspberry-pi-pico-9fcd3f">Synthesize music with animations on a Raspberry Pi Pico</a>
* <a href="https://www.hackster.io/news/michael-wessel-s-raspberry-pi-pico-powered-6116-sram-emulator-gives-vintage-sbcs-a-major-overhaul-2324810b773c?fbclid=IwAR0JCWsvTRej3jnfE3mLCowsHIorXRKLYulz1RZh813tv1pJ0HilOJKTzDg">Michael Wessel's Raspberry Pi Pico-Powered 6116 SRAM Emulator Gives Vintage SBCs a Major Overhaul</a>
* <a href="https://hackaday.io/project/175712-kamina-keyboard">Kamina Keyboard</a>
* <a href="https://hackaday.com/2024/01/14/saving-pic-microcontrollers-with-diy-programmer/">SAVING PIC MICROCONTROLLERS WITH DIY PROGRAMMER</a>
* <a href="https://tahmidmc.blogspot.com/2024/01/quick-and-dirty-pic16f72-programmer.html">Quick and dirty PIC16F72 programmer with the Pico</a>
* <a href="https://www.digikey.com/en/maker/projects/wirelessly-controlling-the-pico-arp-with-the-mini-controller-for-pico/e56edcce3a7f42f98386c6ef01e8114d">Wirelessly Controlling the Pico ARP with the Mini Controller for Pico</a>
* <a href="https://www.hackster.io/xpienet/dual-spiral-marble-clock-3aacf8">Dual Spiral Marble Clock</a>
