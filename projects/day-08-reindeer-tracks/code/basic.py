# Basic motion detection for Circuit Playground Express
# Designed for 9-year-old level (pre-loaded program)

import time
import board
import digitalio
import neopixel
from adafruit_circuitplayground import cp

# Set up the motion sensor
pir = digitalio.DigitalInOut(board.A1)
pir.direction = digitalio.Direction.INPUT

# Set up the NeoPixel Jewel
jewel = neopixel.NeoPixel(board.A2, 7, brightness=0.3)

# Define colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
OFF = (0, 0, 0)

# Main loop
while True:
    if pir.value:  # Motion detected
        # Simple color change pattern
        jewel.fill(RED)
        time.sleep(0.5)
        jewel.fill(GREEN)
        time.sleep(0.5)
        jewel.fill(BLUE)
        time.sleep(0.5)
    else:
        jewel.fill(OFF)
    
    time.sleep(0.1)