# Basic NeoPixel control for Circuit Playground Express
# Designed for 9-year-old level (pre-loaded program)

import time
import board
import neopixel
from adafruit_circuitplayground import cp

# Set up the NeoPixels
pixel1 = neopixel.NeoPixel(board.A1, 1, brightness=0.3)
pixel2 = neopixel.NeoPixel(board.A2, 1, brightness=0.3)
pixel3 = neopixel.NeoPixel(board.A3, 1, brightness=0.3)

# Define simple colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
OFF = (0, 0, 0)

# Main loop
while True:
    if cp.button_a:  # Change colors
        pixel1.fill(RED)
        pixel2.fill(GREEN)
        pixel3.fill(BLUE)
        time.sleep(1)
        pixel1.fill(GREEN)
        pixel2.fill(BLUE)
        pixel3.fill(RED)
        time.sleep(1)
    elif cp.button_b:  # Simple twinkle
        pixel1.fill(YELLOW)
        pixel2.fill(OFF)
        pixel3.fill(YELLOW)
        time.sleep(0.5)
        pixel1.fill(OFF)
        pixel2.fill(YELLOW)
        pixel3.fill(OFF)
        time.sleep(0.5)
    else:
        pixel1.fill(OFF)
        pixel2.fill(OFF)
        pixel3.fill(OFF)
    
    time.sleep(0.1)