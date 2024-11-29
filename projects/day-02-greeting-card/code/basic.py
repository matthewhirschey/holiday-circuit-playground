# Basic LED control for holiday card
# Makes a single LED blink in a simple pattern

import time
import board
import digitalio

# Set up the LED
led = digitalio.DigitalInOut(board.D1)
led.direction = digitalio.Direction.OUTPUT

# Create a simple blinking pattern
while True:
    # Turn LED on
    led.value = True
    time.sleep(1)  # Stay on for 1 second
    
    # Turn LED off
    led.value = False
    time.sleep(1)  # Stay off for 1 second