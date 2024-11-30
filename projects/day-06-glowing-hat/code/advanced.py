# Advanced NeoPixel control for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import neopixel
from adafruit_circuitplayground import cp

# Set up NeoPixels
pixel1 = neopixel.NeoPixel(board.A1, 1, brightness=0.3)
pixel2 = neopixel.NeoPixel(board.A2, 1, brightness=0.3)
pixel3 = neopixel.NeoPixel(board.A3, 1, brightness=0.3)

# Define colors
COLORS = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Purple
    (0, 255, 255),  # Cyan
    (255, 255, 255) # White
]

def color_chase(wait=0.5):
    """Move through colors one at a time"""
    for color in COLORS:
        pixel1.fill(color)
        time.sleep(wait)
        pixel2.fill(color)
        time.sleep(wait)
        pixel3.fill(color)
        time.sleep(wait)

def rainbow_fade(speed=0.02):
    """Create smooth rainbow fade effect"""
    for i in range(255):
        r = (i * 3) % 255
        g = (i * 7) % 255
        b = (i * 11) % 255
        pixel1.fill((r, g, b))
        pixel2.fill((g, b, r))
        pixel3.fill((b, r, g))
        time.sleep(speed)

def sparkle(wait=0.1, iterations=20):
    """Create random sparkle effect"""
    import random
    pixels = [pixel1, pixel2, pixel3]
    for _ in range(iterations):
        pixel = random.choice(pixels)
        color = random.choice(COLORS)
        pixel.fill(color)
        time.sleep(wait)
        pixel.fill((0, 0, 0))

# Main loop
while True:
    if cp.button_a:
        color_chase()
    elif cp.button_b:
        rainbow_fade()
    elif cp.button_a and cp.button_b:
        sparkle()
    else:
        # Gentle twinkling when no buttons pressed
        sparkle(0.2, 5)
    
    time.sleep(0.1)