#print("Hello, Pi Pico!")

#from machine import Pin
#led = Pin(13, Pin.OUT)
#led.value(1)
#led.value(0)

import time
from machine import Pin
led=Pin(13,Pin.OUT)

while True:
    led.value(1)        #set led turn on
    time.sleep(0.5)
    led.value(0)        #set led turn off
    time.sleep(0.5)