# Project objectives: 
#   Read temperature and humidity values from the DHT22 sensor
#   Display the sensor readings in the console
#
# Hardware connections used:
#   DHT22 VCC Pin to 3.3V
#   DHT22 SDA Pin to GPIO Pin 15
#   10k ohm pull-up resistor from DHT22 SDA Pin to 3.3V (diregard if DHT22 is 3-pin)
#   DHT22 GND Pin to GND
#
# Programmer: Adrian Josele G. Quional

# modules
from machine import Pin
from time import sleep
from dht import DHT22	# if the sensor is DHT11, import DHT11 instead of DHT22

# creating a DHT object
# change DHT22 to DHT11 if DHT11 is used
dht = DHT22(Pin(15)) 

# continuously get sensor readings while the board has power
while True:
    # getting sensor readings
    dht.measure()
    temp = dht.temperature()
    hum = dht.humidity()

    # displaying values to the console
    print(f"Temperature: {temp}°C   Humidity: {hum}% ")
    
    # format method or string concatenation may also be used
    #print("Temperature: {}°C   Humidity: {:.0f}% ".format(temp, hum))
    #print("Temperature: " + str(temp) + "°C" + "   Humidity: " + str(hum) + "%")
    #print("Temperature: {}°C   Humidity: {:.0f}% ".format(temp, hum))
    
    # delay of 2 secs because DHT22 takes a reading once every 2 secs
    sleep(2)