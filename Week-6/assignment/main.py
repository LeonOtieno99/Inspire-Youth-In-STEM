from machine import Pin
import time
while True:
    led = Pin(13, Pin.OUT)
    led.value(1)
    time.sleep(10)
    led.value(0)
    time.sleep(0)

    led = Pin(12, Pin.OUT)
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(0)

    led = Pin(15, Pin.OUT)
    led.value(1)
    time.sleep(10)
    led.value(0)
    time.sleep(0)

