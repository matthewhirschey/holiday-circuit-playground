# Basic LED control for snowman using Circuit Playground Express
# Designed for 9-year-old level

import time
import board
import digitalio
from adafruit_circuitplayground import cp

# Set up the LEDs
led1 = digitalio.DigitalInOut(board.A1)
led1.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.A2)
led2.direction = digitalio.Direction.OUTPUT

# Main loop
while True:
    if cp.button_a:  # Button A is pressed
        # Turn on both LEDs
        led1.value = True
        led2.value = True
    else:
        # Turn off both LEDs
        led1.value = False
        led2.value = False
    
    time.sleep(0.1)  # Small delay to prevent button bounce