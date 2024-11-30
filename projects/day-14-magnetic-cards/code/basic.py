# Basic magnetic card control for Circuit Playground Express
# Designed for 9-year-old level (pre-loaded program)

import time
import board
import digitalio
import neopixel
from adafruit_circuitplayground import cp

# Set up reed switch
reed = digitalio.DigitalInOut(board.A1)
reed.direction = digitalio.Direction.INPUT
reed.pull = digitalio.Pull.UP

# Set up NeoPixels
pixels = neopixel.NeoPixel(board.A2, 8, brightness=0.3)

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
OFF = (0, 0, 0)

# Main loop
while True:
    if not reed.value:  # Card is open
        # Simple color cycle
        pixels.fill(RED)
        time.sleep(0.5)
        pixels.fill(GREEN)
        time.sleep(0.5)
        pixels.fill(BLUE)
        time.sleep(0.5)
    else:  # Card is closed
        pixels.fill(OFF)
    
    time.sleep(0.1)