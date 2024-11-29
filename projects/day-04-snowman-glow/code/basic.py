# Basic LED control for snowman
# Makes the snowman's eyes twinkle when the nose (button) is pressed

import board
import digitalio
import time

# Set up the button
button = digitalio.DigitalInOut(board.A1)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

# Set up the LEDs (eyes)
led1 = digitalio.DigitalInOut(board.D1)
led1.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.D2)
led2.direction = digitalio.Direction.OUTPUT

# Main loop
while True:
    if button.value:  # Button is pressed
        # Light up both LEDs
        led1.value = True
        led2.value = True
        time.sleep(0.5)
        # Turn off both LEDs
        led1.value = False
        led2.value = False
        time.sleep(0.5)
    else:
        # When button is not pressed, LEDs are off
        led1.value = False
        led2.value = False