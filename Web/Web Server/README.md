# Steps to setup Raspberry Pi Pico W as a web server:

1. In the <b>web-server.py</b> program, specify the SSID/WiFi name and password.
2. Download the program to Raspberry Pi Pico W. 
3. Once the program is downloaded, there would be a notification printed in the Thonny shell that the board is now connected to the internet. The IP address assigned to the Raspberry Pi Pico W will be printed. Copy the IP address and paste it in the address bar of the web browser of your choice.

![Web server program with IP address printed in the Shell](https://github.com/ajgquional/rpi-picow-micropython/blob/95c73ebee50110376830a726ae55c5995a6bc26e/Web/Web%20Server/RPi-Pico-W-web-server-address.PNG)

4. Once the IP address is pasted, buttons to control the onboard LED, LED status, and onboard temperature would be displayed as a webpage, per the HTML string included in the program. Congratulations! You have now setup the Raspberry Pi Pico W as a web server. The temperature displayed would be updated very 5 seconds as specified in the HTML string.

![LED status and onboard temperature displayed in the webpage](https://github.com/ajgquional/rpi-picow-micropython/blob/95c73ebee50110376830a726ae55c5995a6bc26e/Web/Web%20Server/RPi-Pico-W-as-web-server.PNG)

5. Should you want to change the functionality (that is, not display the LED status and onboard temperature to the webpage), the program must be edited as well as the HTML code stored in the html variable.

# Notes on the webpage served by Raspberry Pi Pico W:

* The webpage is very simple so if you wanted to add aesthetics to it, it would be recommended to design the page using another code editor suitable for webpage design (Visual Studio Code is one).
* Once the design is complete, copy the entire HTML code as a string in the <b>web-server.py</b> program. Replace the contents of the string stored in the html variable with the new HTML code you've designed.
* The contents of the HTML code would be in accordance to your own project.
* CSS/JavaScript might also be included to the HTML code. It is recommended to have them inline (rather than external) within the HTML code so that when the code is copied to the MicroPython program, it's just a single string.
