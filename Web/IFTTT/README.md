# Steps to integrate Raspberry Pi Pico W and Google Sheets via IFTTT:

### Creating the applet:

1. Login to your IFTTT account. If you don't have one, you can create a free account.
2. Once you've logged in, click the "Create" button in the upper right corner of the home page. This is to create a new Applet.

![Creating an IFTTT applet](https://github.com/ajgquional/rpi-picow-micropython/blob/d40a643011c3118987e2f358445a1a715e1eaafa/Web/IFTTT/IFTTT-Integration-Step1.png)

3. Specify the trigger and action. The "If This" is the trigger and the "Then That" is the action (thus, "IFTTT"). Note that you cannot click the "Then That" button (it's greyed out) if you haven't specified yet the "If This." Create the trigger by clicking the "If This" button.

![Creating a trigger](https://github.com/ajgquional/rpi-picow-micropython/blob/d40a643011c3118987e2f358445a1a715e1eaafa/Web/IFTTT/IFTTT-Integration-Step2.png)

4. Choose the trigger. In our case, since we need to connect Raspberry Pi Pico W to Google Sheets, we have to create a webhook. Type "webhook" in the search bar for the services and click the icon that appeared.

![Choosing webhook service](https://github.com/ajgquional/rpi-picow-micropython/blob/d40a643011c3118987e2f358445a1a715e1eaafa/Web/IFTTT/IFTTT-Integration-Step3.png)

5. After choosing Webhooks as our service, choose "receive a web request."

![Choosing receive a web request](https://github.com/ajgquional/rpi-picow-micropython/blob/d40a643011c3118987e2f358445a1a715e1eaafa/Web/IFTTT/IFTTT-Integration-Step4.png)

6. Specify the event name. You can create any event name as long as it's valid (containing only letters, numbers, and underscores). It would be recommended to create an event name that is descriptive of the project you're creating. In the example, the event name used is "temp_data" because the project involves sending onboard temperature data from the Raspberry Pi Pico W to Google Sheets. After typing the event name, remember it, as you need to specify this in the MicroPython code. Once the event name is finalized, click "Create trigger."

![Event name](https://github.com/ajgquional/rpi-picow-micropython/blob/d40a643011c3118987e2f358445a1a715e1eaafa/Web/IFTTT/IFTTT-Integration-Step5.png)

7. Now that you have created the "If This" (the trigger) part of the applet, you are now ready to create the "Then That" (action). In the page containing "If This" "Then That," click "Then That" to create the action.

![Creating the action](https://github.com/ajgquional/rpi-picow-micropython/blob/d40a643011c3118987e2f358445a1a715e1eaafa/Web/IFTTT/IFTTT-Integration-Step6.png)

8. Similar to Step 4, you to choose a service. This time, type "google sheets" since the project involves sending data to Google Sheets. Click the Google Sheets icon that appeared. Note that you need to allow the integration of IFTTT and your Google account. 

![Choosing Google Sheets service](https://github.com/ajgquional/rpi-picow-micropython/blob/d40a643011c3118987e2f358445a1a715e1eaafa/Web/IFTTT/IFTTT-Integration-Step7.png)

9. Choose "Add row to spreadsheet." This means every time the Raspberry Pi Pico W sends data, a new row in the spreadsheet would automatically be created containing the values that you are intending to send.

![Choosing add row to spreadsheet](https://github.com/ajgquional/rpi-picow-micropython/blob/d40a643011c3118987e2f358445a1a715e1eaafa/Web/IFTTT/IFTTT-Integration-Step8.png)

10. Specify details related to the action that you have chosen (add row to spreadsheet). There are already default names specified and you may choose to just use it. However, if you are meticulous, you can change some details: 

  * First, the spreadsheet name can be changed from the default "IFTTT_Maker_Webhooks_Events." 
  * Next, for the "Formatted row," it shows you how each row would look like. In every row, it would show you the date and time the event occurred (thus, OccrredAt). This is the first column. The second column is the event name specified in the trigger. The third to fifth columns are the values to be sent by Raspberry Pi Pico W. If you are only sending one value, it is recommended to delete "Value2" and "Value3" columns because if these are retained, you would see the text {{Value2}} and {{Value3}} in the fourth and fifth columns of the spreadsheet. Thus, retain only what you needed.
  * You can also change the Google Drive folder path. By the, the path is "IFTTT/MakerWebooks/EventName". What this means is that, ultimately, the created spreadsheet would live inside the event name folder (for example, if the event name is "temp_data," the spreadsheet would be created inside the folder of that name). For the default Drive folder path, IFTTT is the main folder then inside of that, there is a MakerWebooks folder, then finally, there is "temp_data" folder (if that's the name of the event). Again, the path can be edited if you think the path is confusing.

    After specifying the details, click "Create action" to finalize the action.

![Finalizing action](https://github.com/ajgquional/rpi-picow-micropython/blob/d40a643011c3118987e2f358445a1a715e1eaafa/Web/IFTTT/IFTTT-Integration-Step9.png)

11. You will then return to the applet creation page. Now that the trigger and action are decided, click "Continue" to finalize the applet.

![Finalizing the applet](https://github.com/ajgquional/rpi-picow-micropython/blob/ff33c5cfd6c726f24ac67a646255c73b7b50988f/Web/IFTTT/IFTTT-Integration-Step10-edited.png)

### Getting the API Key:

12. After finalizing the applet, you will be lead to a page containing the applet that you have created. There will be a default name assigned to you applet but it is recommended to change it to something more descriptive. In the example below, the applet's name is changed to "Pico W Onboard Temp to Google Sheets." However, more important than the title of the applet is to webhooks icon which you need to click to be able to proceed to the documentation containing the API key needed to be copied to the MicroPython program.

![Clicking webhooks icon](https://github.com/ajgquional/rpi-picow-micropython/blob/ff33c5cfd6c726f24ac67a646255c73b7b50988f/Web/IFTTT/IFTTT-Integration-Step11.png)

13. After clicking the webhooks icon, click "Documentation" in the page that appeared.

![Clicking Documentation](https://github.com/ajgquional/rpi-picow-micropython/blob/ff33c5cfd6c726f24ac67a646255c73b7b50988f/Web/IFTTT/IFTTT-Integration-Step12.png)

14. A new page would open containing the API key and some mechanism to test if the connectivity to Google Sheets is a success. First, copy your API key above. Should you want to proceed to the test, type the event name that you specified in the trigger and click "Test It." If you wanted to test if you can send two or three values because it is what you wanted to do in your project, scroll down the page and look for "To Trigger an Event with 3 JSON values." Again, specify the event name and put arbitrary test values then click "Test It" (see images below for a more specific guide). In either of the test methods, you should be able to see a new spreadsheet created in your Google Drive in the path you specified before. If you see a Google Sheet with the test values you specified (if you used the second method), then the Google Sheet integration is a success.

<p align="center">
  <b>Test Method 1</b>
</p>

![API key with test method 1](https://github.com/ajgquional/rpi-picow-micropython/blob/ff33c5cfd6c726f24ac67a646255c73b7b50988f/Web/IFTTT/IFTTT-Integration-Step13.png)

<p align="center">
  <b>Test Method 2</b>
</p>

![API key with test method 2](https://github.com/ajgquional/rpi-picow-micropython/blob/ff33c5cfd6c726f24ac67a646255c73b7b50988f/Web/IFTTT/IFTTT-Integration-Step14.png)

### Editing the MicroPython program:

15. Now that you've set up the integration, the last step to integrate Raspberry Pi Pico W to Google Sheets is to download a program enabling the connection between the two. In the MicroPython program, specify the SSID/WiFi name and password, as usual. Aside from this, you have to include the event name which you created before (in the trigger) and the API key you've recently copied. After including all necessary details in the program, download it to Raspberry Pi Pico W. There would be a notification in the Thonny shell telling you that the connection is a success. Check the values sent to the Google Sheet and the ones printed in the shell. They should match. Congratulations! You are successful in integrating Raspberry Pi Pico W and Google Sheets.

![Raspberry Pi Pico W and Google Sheets](https://github.com/ajgquional/rpi-picow-micropython/blob/ff33c5cfd6c726f24ac67a646255c73b7b50988f/Web/IFTTT/IFTTT-Integration-Step15.png)

16. Should you wish to send more than the onboard temperature data, create the circuit (if needed) and modify the program and applet accordingly. More so, you can change the action part of the applet. If you don't want to sent data to Google Sheets, you can choose other actions, such as sending an SMS message, posting a tweet, or sending an email. There are a lot of services to choose from in IFTTT. 
