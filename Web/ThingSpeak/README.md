# Steps to integrate Raspberry Pi Pico W to ThingSpeak:

1. Login to ThingSpeak using a MathWorks account. If you don't have a MathWorks account, you can create a free account.

![ThingSpeak login page](https://github.com/ajgquional/rpi-picow-micropython/blob/153df7b05e920592b7e6da4a7f30a20f338956fa/Web/ThingSpeak/ThingSpeak-login.png)

2. Once you've logged in, you can create a new channel and specify some details such as the name of the channel, description, and fields (data you will be sending from the Raspberry Pi Pico W). Once details are specified, click "Save Channel."
3. In the channel that you've created, click on the "API Keys" tab to find the Write API Key. Copy the Write API Key. 

![ThingSpeak Channel API Keys](https://github.com/ajgquional/rpi-picow-micropython/blob/153df7b05e920592b7e6da4a7f30a20f338956fa/Web/ThingSpeak/ThingSpeak-Write-API-Key.png)

4. Open the program <b>thingspeak.py</b>. As usual, specify the SSID/WiFi name and password. Aside from these, you also need to paste the Write API Key that you've copied from ThingSpeak. Once all details are specified, you can now download the program to the Raspberry Pi Pico W. There would be a notification in the Thonny shell if Raspberry Pi Pico W has already been connected to the internet and if data is already being written to the ThingSpeak dashboard.

![RPi Pico W successfully connected to ThingSpeak](https://github.com/ajgquional/rpi-picow-micropython/blob/153df7b05e920592b7e6da4a7f30a20f338956fa/Web/ThingSpeak/RPi-Pico-W-ThingSpeak-Code.png)

5. Check your ThingSpeak channel if data is now being visualized. Congratulations! You now have connected Raspberry Pi Pico W to ThingSpeak.

![Sample ThingSpeak dashboard](https://github.com/ajgquional/rpi-picow-micropython/blob/153df7b05e920592b7e6da4a7f30a20f338956fa/Web/ThingSpeak/Sample-ThingSpeak-Dashboard.png)

6. Should you need to modify the functionality of the device (say, not send and visualize the onboard temperature in a ThingSpeak dashboard), the program and the dashboard must be modified, but the steps to integrate the board to ThingSpeak is still the same.
