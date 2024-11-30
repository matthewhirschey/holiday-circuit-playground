# Advanced LED control for snowman using Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import digitalio
from adafruit_circuitplayground import cp

# Set up external LEDs
led1 = digitalio.DigitalInOut(board.A1)
led1.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.A2)
led2.direction = digitalio.Direction.OUTPUT

# Clear all NeoPixels
cp.pixels.fill((0, 0, 0))

def twinkle_eyes():
    """Make the LEDs twinkle alternately"""
    led1.value = True
    led2.value = False
    time.sleep(0.2)
    led1.value = False
    led2.value = True
    time.sleep(0.2)

def fade_effect():
    """Create a fading effect with the NeoPixels"""
    for i in range(10):
        cp.pixels.fill((i * 5, i * 5, i * 5))
        time.sleep(0.05)
    for i in range(10, 0, -1):
        cp.pixels.fill((i * 5, i * 5, i * 5))
        time.sleep(0.05)
    cp.pixels.fill((0, 0, 0))

# Main loop
while True:
    if cp.button_a:  # Button A controls eye twinkle
        twinkle_eyes()
    elif cp.button_b:  # Button B controls NeoPixel fade
        fade_effect()
    else:
        # Everything off when no buttons are pressed
        led1.value = False
        led2.value = False
        cp.pixels.fill((0, 0, 0))
    
    time.sleep(0.1)  # Small delay to prevent button bounce