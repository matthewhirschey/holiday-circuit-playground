# Basic rotary encoder control for Circuit Playground Express
# Designed for 9-year-old level

import time
import board
import digitalio
import neopixel
from adafruit_circuitplayground import cp

# Set up encoder pins
clk = digitalio.DigitalInOut(board.A1)
dt = digitalio.DigitalInOut(board.A2)
sw = digitalio.DigitalInOut(board.A3)

clk.direction = digitalio.Direction.INPUT
dt.direction = digitalio.Direction.INPUT
sw.direction = digitalio.Direction.INPUT
sw.pull = digitalio.Pull.UP

# Set up NeoPixel display (optional)
display = neopixel.NeoPixel(board.A4, 30, brightness=0.3)

# Track encoder position and state
position = 0
last_clk = clk.value
brightness = 0.3

# Define some colors
COLORS = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Purple
    (0, 255, 255),  # Cyan
    (255, 255, 255) # White
]

# Main loop
while True:
    # Read encoder
    current_clk = clk.value
    if current_clk != last_clk:
        if dt.value != current_clk:
            position = (position + 1) % len(COLORS)
        else:
            position = (position - 1) % len(COLORS)
        
        # Update display color
        display.fill(COLORS[position])
        
    # Check button
    if not sw.value:
        # Flash current color
        current_color = COLORS[position]
        display.fill((0, 0, 0))
        time.sleep(0.2)
        display.fill(current_color)
        time.sleep(0.2)
    
    last_clk = current_clk
    time.sleep(0.01)