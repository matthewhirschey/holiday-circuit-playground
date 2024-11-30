# Basic rotary encoder control for Circuit Playground Express
# Designed for 9-year-old level (pre-loaded program)

import time
import board
import digitalio
import neopixel

# Set up encoder pins
clk = digitalio.DigitalInOut(board.A1)
dt = digitalio.DigitalInOut(board.A2)
sw = digitalio.DigitalInOut(board.A3)

clk.direction = digitalio.Direction.INPUT
dt.direction = digitalio.Direction.INPUT
sw.direction = digitalio.Direction.INPUT
sw.pull = digitalio.Pull.UP

# Set up NeoPixel Jewel
jewel = neopixel.NeoPixel(board.A0, 7, brightness=0.3)

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

# Track position and settings
color_index = 0
brightness = 0.3
last_clk = clk.value

# Main loop
while True:
    # Read encoder
    current_clk = clk.value
    if current_clk != last_clk:
        if dt.value != current_clk:
            color_index = (color_index + 1) % len(COLORS)
            jewel.fill(COLORS[color_index])
        else:
            brightness = max(0.1, min(1.0, brightness - 0.1))
            jewel.brightness = brightness
    
    # Check button press
    if not sw.value:
        # Toggle all pixels
        jewel.fill((0, 0, 0))
        time.sleep(0.2)
        jewel.fill(COLORS[color_index])
        time.sleep(0.2)
    
    last_clk = current_clk
    time.sleep(0.01)