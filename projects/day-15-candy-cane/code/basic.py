# Basic NeoPixel strip control for Circuit Playground Express
# Designed for 9-year-old level (pre-loaded program)

import time
import board
import neopixel
from adafruit_circuitplayground import cp

# Set up NeoPixel strip
strip = neopixel.NeoPixel(board.A1, 10, brightness=0.3)

# Define colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

# Main loop
while True:
    if cp.button_a:  # Red and white stripes
        for i in range(10):
            if i % 2 == 0:
                strip[i] = RED
            else:
                strip[i] = WHITE
    elif cp.button_b:  # Spin pattern
        for offset in range(10):
            for i in range(10):
                if (i + offset) % 2 == 0:
                    strip[i] = RED
                else:
                    strip[i] = WHITE
            time.sleep(0.2)
    elif cp.button_a and cp.button_b:  # Twinkle
        for i in range(10):
            strip[i] = WHITE if i % 2 == 0 else RED
            time.sleep(0.1)
            strip[i] = OFF
    else:
        strip.fill(OFF)
    
    time.sleep(0.1)