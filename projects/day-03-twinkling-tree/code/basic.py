# Basic LED control for twinkling tree
# Simple button-activated LED pattern

import time
import board
import digitalio

# Set up the button
button = digitalio.DigitalInOut(board.BUTTON_A)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

# Set up the LED
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# Main loop
while True:
    if button.value:  # Button is pressed
        led.value = True
        time.sleep(0.5)
        led.value = False
        time.sleep(0.5)
    else:
        led.value = False