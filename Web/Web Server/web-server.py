# ================================================== 
""" 
Project objectives:
    Setup the Raspberry Pi Pico W as a web server
    Display onboard temperature in a webpage
    Display onboard LED status and control it via a webpage

Author: Adrian Josele G. Quional

Code reference: https://projects.raspberrypi.org/en/projects/get-started-pico-w/0
"""
# ==================================================

# modules
import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine

# connection details
ssid = "PUT HERE YOUR SSID/WIFI NAME"
password = "PUT HERE YOUR WIFI PASSWORD"

def connect():
    """This function facilitates connection of Raspberry Pi Pico W to the Internet using WiFi."""
    
    # connecting to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    # performing handshake
    # continuously wait for connection
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
        
    # displaying to the console the IP address that the Raspberry Pi Pico is assigned to
    ip = wlan.ifconfig()[0]
    print(f"Connected on {ip}")
    
    return ip

def open_socket(ip):
    """
    This function opens a socket in order for the server (Raspberry Pi Pico W)
    to be able to listen to a client (any web browser accessing the IP address
    of the Raspberry Pi Pico W).
    """
    
    # opening a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    
    return connection

def webpage(temperature, state):
    """
    This function contains the HTML string containing elements that would be displayed in the webpage.
    
    As a sample, this takes in temperature (from the onboard temperature sensor) and the onboard LED state (ON or OFF).
    According to the actual purpose of the project, the parameters can be changed.
    """
    
    # HTML template
    # can be varied according to what's needed to be displayed in the webpage
    # it is recommended to create the HTML document in a separate file to be edited in the editor of choice suitable for webpage design
    # after editing the HTML file in a separate browser, copy the code here as a string stored in the html variable
    html = f"""
            <!DOCTYPE html>
            <html>
                <body>
                    <form action="./lighton">
                        <input type="submit" value="Light on" />
                    </form>

                    <form action="./lightoff">
                        <input type="submit" value="Light off" />
                    </form>

                    <p>LED is {state}</p>
                    <p>Temperature is {temperature}</p>
                    
                    <meta http-equiv="refresh" content="5" />
                </body>
            </html>
            """
    
    return str(html)

def serve(connection):
    """This function starts the web server and serves the webpage."""
    
    # starting the web server
    
    # initially, LED should be OFF
    state = 'OFF'
    pico_led.off()
    
    # temperature is initially set to 0 (just for initialization purposes)
    temperature = 0
    
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        
        try:
            request = request.split()[1]
        except IndexError:
            pass
        
        # controls LED state depending on request
        if request == '/lighton?':
            pico_led.on()
            state = 'ON'
        elif request =='/lightoff?':
            pico_led.off()
            state = 'OFF'
        
        # gets onboard temperature via picozero module
        # stores onboard temperature in the temperature variable
        temperature = pico_temp_sensor.temp
        
        html = webpage(temperature, state)
        client.send(html)
        client.close()

try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)

except KeyboardInterrupt:
    machine.reset()