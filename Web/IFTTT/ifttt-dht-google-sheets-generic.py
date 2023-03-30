# ================================================== 
"""
Project objectives:
    Connect Raspberry Pi Pico W to Google Sheets via IFTTT
    Send temperature and humidity data (gathered using DHT22) to Google Sheets

Author: Adrian Josele G. Quional
"""
# ================================================== 

# modules
import network
from time import sleep
from machine import reset
import urequests
from picozero import pico_led
from dht import DHT22

# connection details
ssid = "PUT HERE YOUR SSID/WIFI NAME"
password = "PUT HERE YOUR WIFI PASSWORD"
key = "PUT HERE YOUR API KEY FROM IFTTT"
event_name = "PUT HERE THE EVENT NAME THAT YOU'VE CREATED IN IFTTT"

# creating a DHT object
dht = DHT22(Pin(15)) 

def connect():
    """This function facilitates connection of Raspberry Pi Pico W to the Internet using WiFi."""

    # connecting to wlan
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print(".", end="")
        sleep(0.5)

    print("Connected to WiFi")
    print("My IP address is:", wlan.ifconfig()[0])

try:
    # connecting first via WiFi
    connect()
    print("==================== \n")
    
    # then continuously read temperature and humidity and send the data to Google Sheets 
    while True:
        # LED on as status indicator that the device is working
        pico_led.on()
        
        # getting sensor readings
        dht.measure()
        temp = dht.temperature()
        hum = dht.humidity()
        
        # displaying values to the console
        print(f"Temperature: {temp}°C   Humidity: {hum}% ")
        
        # url from webhook integrations documentation
        url = f"https://maker.ifttt.com/trigger/{event_name}/with/key/{key}?value1={temp}&value2={hum}"
        # url for multiple values to be sent:
        # https://maker.ifttt.com/trigger/{event}/with/key/{webhooks_key}?value1=value1&value2=value2&value3=value3
        # replace value1 and value2 with the variable containing the data that you want to send
        # note: up until 3 values can be sent via IFTTT

        # sending data
        response = urequests.post(url)
        response.close()
        print("Event sent")
        # turning off LED, signaling that sending of data is done
        pico_led.off()
        
        # device reads temperature and humidity and sends data to Google Sheets every 5 secs
        sleep(5)
        
except KeyboardInterrupt:
    reset()