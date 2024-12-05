# Basic magnetic card control for Circuit Playground Express
# Designed for 9-year-old level - works with alligator clips

import time
import board
import digitalio
from adafruit_circuitplayground import cp

# Set up the magnetic switch on pin A1
switch = digitalio.DigitalInOut(board.A1)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

# Main loop
while True:
    if not switch.value:  # Card is open
        # Light up built-in LEDs
        cp.pixels.fill((255, 0, 0))  # Red
        # Play a tone
        cp.play_tone(440, 0.1)
    else:  # Card is closed
        # Turn off LEDs
        cp.pixels.fill((0, 0, 0))
    
    time.sleep(0.1)  # Small delay