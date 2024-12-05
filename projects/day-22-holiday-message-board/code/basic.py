# Basic tree upgrade and train control for Circuit Playground Express
# Designed for 9-year-old level

import time
import board
import digitalio
import neopixel
from adafruit_circuitplayground import cp
from random import random

# Set up tree LEDs
tree_leds = []
for pin in [board.A1, board.A2, board.A3]:
    led = digitalio.DigitalInOut(pin)
    led.direction = digitalio.Direction.OUTPUT
    tree_leds.append(led)

# Set up train (NeoPixel Ring)
train = neopixel.NeoPixel(board.A4, 16, brightness=0.3)

# Define colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

# Train position
position = 0

# Main loop
while True:
    # Update tree lights
    for led in tree_leds:
        # Random twinkling
        led.value = random() > 0.7
    
    # Update train
    train.fill(OFF)  # Clear previous position
    
    # Add train (3 red pixels and headlight)
    train[position] = RED
    train[(position + 1) % 16] = RED
    train[(position + 2) % 16] = RED
    train[(position + 3) % 16] = WHITE
    
    # Move train
    position = (position + 1) % 16
    
    time.sleep(0.2)