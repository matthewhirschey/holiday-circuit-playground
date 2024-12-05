# Basic NeoPixel Ring light show for Circuit Playground Express
# Designed for 9-year-old level

import time
import board
import neopixel
from adafruit_circuitplayground import cp

# Set up NeoPixel Ring
ring = neopixel.NeoPixel(board.A1, 24, brightness=0.3)

# Define some colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

# Holiday colors
HOLIDAY_COLORS = [RED, GREEN, WHITE]

def spin_pattern():
    """Spin holiday colors around the ring"""
    for offset in range(24):
        for i in range(24):
            color_index = ((i + offset) // 8) % len(HOLIDAY_COLORS)
            ring[i] = HOLIDAY_COLORS[color_index]
        time.sleep(0.1)

def twinkle_pattern():
    """Random holiday twinkle effect"""
    from random import randint
    # Start with all green
    ring.fill(GREEN)
    
    # Add random red and white twinkles
    for _ in range(10):
        i = randint(0, 23)  # Random pixel
        ring[i] = RED if randint(0, 1) else WHITE
        time.sleep(0.1)
        ring[i] = GREEN

def rainbow_pattern():
    """Simple rainbow effect"""
    for j in range(255):
        for i in range(24):
            pixel_index = (i * 256 // 24) + j
            ring[i] = color_wheel(pixel_index & 255)
        time.sleep(0.01)

def color_wheel(pos):
    """Generate rainbow colors"""
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

# Main loop
while True:
    if cp.button_a:
        spin_pattern()
    elif cp.button_b:
        twinkle_pattern()
    elif cp.button_a and cp.button_b:
        rainbow_pattern()
    else:
        ring.fill(OFF)
    
    time.sleep(0.1)