# Basic LED control for Circuit Playground Express
# This code makes a single LED blink

import time
import board
import digitalio

# Set up the LED pin
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# Create a simple blinking pattern
while True:
    led.value = True    # Turn LED on
    time.sleep(0.5)     # Wait for half second
    led.value = False   # Turn LED off
    time.sleep(0.5)     # Wait for half second
