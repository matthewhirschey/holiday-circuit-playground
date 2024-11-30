# Basic NeoPixel Jewel control for Circuit Playground Express
# Designed for 9-year-old level - works with alligator clips

import time
import board
import neopixel
from adafruit_circuitplayground import cp

# Set up NeoPixel Jewel on pin A1
jewel = neopixel.NeoPixel(board.A1, 7, brightness=0.3)

# Define colors
RED = (255, 0, 0)          # Regular red
BRIGHT_RED = (255, 50, 50)  # Brighter, warmer red
OFF = (0, 0, 0)            # LEDs off

# Main loop
while True:
    if cp.button_a:  # Steady glow
        jewel.fill(RED)
        
    elif cp.button_b:  # Simple twinkle
        jewel.fill(BRIGHT_RED)
        time.sleep(0.5)
        jewel.fill(RED)
        time.sleep(0.5)
        
    elif cp.button_a and cp.button_b:  # Special pattern
        # Spin around the circle
        for i in range(7):
            jewel.fill(OFF)
            jewel[i] = RED
            time.sleep(0.2)
        # Then all on
        jewel.fill(RED)
        time.sleep(0.5)
    
    time.sleep(0.1)  # Small delay between checks