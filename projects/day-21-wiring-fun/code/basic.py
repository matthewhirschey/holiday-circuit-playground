# Basic wiring test for Circuit Playground Express
# Designed for 9-year-old level

import time
import board
import digitalio

# Set up LED
led = digitalio.DigitalInOut(board.A1)
led.direction = digitalio.Direction.OUTPUT

# Set up button
button = digitalio.DigitalInOut(board.A2)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Main loop
while True:
    if not button.value:  # Button is pressed
        # Turn LED on
        led.value = True
    else:
        # Turn LED off
        led.value = False
    
    time.sleep(0.1)