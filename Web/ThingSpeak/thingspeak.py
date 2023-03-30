# ================================================== 
""" 
Project objectives:
    Setup the Raspberry Pi Pico W as an end device sending temperature data to a dashboard
    Connect Raspberry Pi Pico W to ThingSpeak
    Visualize onboard temperature data in an IoT dashboard

Authors: Adrian Josele G. Quional and Renz Carlo A. Cabual
"""
# ==================================================

# modules
import urequests 
from machine import Pin, Timer, reset
from time import sleep
import network
from picozero import pico_temp_sensor, pico_led

HTTP_HEADERS = {'Content-Type': 'application/json'}

# connection details
ssid = "PUT HERE YOUR SSID/WIFI NAME"
password = "PUT HERE YOUR WIFI PASSWORD"
THINGSPEAK_WRITE_API_KEY = "PUT HERE YOUR API KEY FROM THINGSPEAK"

def connect():
    """
    This function facilitates connection of Raspberry Pi Pico W to the Internet using WiFi.
    
    Thus, this configures the Raspberry Pi Pico W as an end device.
    """
    
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(ssid, password)

    # continuously wait for connection
    while sta_if.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
        
    # displaying to the console the IP address that the Raspberry Pi Pico is assigned to
    ip = sta_if.ifconfig()[0]
    print(f"Connected on {ip}")

try:
    # connecting first via WiFi
    connect()
    print("==================== \n")
    
    # then continuously read temperature and send the data to a ThingSpeak dashboard 
    while True:
        # LED on as status indicator that the device is working
        pico_led.on()
        
        temperature = pico_temp_sensor.temp
        print(f"Onboard temperature: {temperature}")
        readings = {'field1': temperature}
        
        request = urequests.get('http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY, json=readings, headers=HTTP_HEADERS)  
        request.close()
        # turning off LED, signaling that sending of data is done
        pico_led.off()
        
        print("writing data to ThingSpeak...")
        print("==================== \n")
        # device reads temperature and sends data to the dashboard every 10 secs
        sleep(10)
             
except KeyboardInterrupt:
    reset()