# Basic NeoPixel candy cane for Circuit Playground Express
# Designed for 9-year-old level

import time
import board
import neopixel
from adafruit_circuitplayground import cp

# Set up NeoPixel strip - 5 LEDs on pin A1
pixels = neopixel.NeoPixel(board.A1, 5, brightness=0.3)

# Define colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

# Main loop
while True:
    if cp.button_a:  # Classic candy cane pattern
        for i in range(5):
            if i % 2 == 0:
                pixels[i] = RED
            else:
                pixels[i] = WHITE
    
    elif cp.button_b:  # Moving light pattern
        for i in range(5):
            pixels.fill(OFF)  # All off
            pixels[i] = RED   # One light on
            time.sleep(0.2)
    
    elif cp.button_a and cp.button_b:  # Sparkle pattern
        from random import randint
        for _ in range(10):
            i = randint(0, 4)  # Random LED
            pixels[i] = WHITE
            time.sleep(0.1)
            pixels[i] = RED
            time.sleep(0.1)
    
    time.sleep(0.1)