# Basic NeoPixel nose control for Circuit Playground Express
# Designed for 9-year-old level (pre-loaded program)

import time
import board
import neopixel
from adafruit_circuitplayground import cp

# Set up NeoPixel Jewel
jewel = neopixel.NeoPixel(board.A1, 7, brightness=0.3)

# Define colors
RED = (255, 0, 0)
BRIGHT_RED = (255, 50, 50)
DIM_RED = (64, 0, 0)
OFF = (0, 0, 0)

# Main loop
while True:
    if cp.button_a:  # Steady glow
        jewel.fill(RED)
    elif cp.button_b:  # Simple twinkle
        jewel.fill(BRIGHT_RED)
        time.sleep(0.5)
        jewel.fill(DIM_RED)
        time.sleep(0.5)
    elif cp.button_a and cp.button_b:  # Special pattern
        for i in range(7):
            jewel[i] = BRIGHT_RED
            time.sleep(0.1)
            jewel[i] = DIM_RED
    else:
        jewel.fill(OFF)
    
    time.sleep(0.1)