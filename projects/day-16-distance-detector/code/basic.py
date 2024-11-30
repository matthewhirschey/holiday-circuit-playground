# Basic distance sensor control for Circuit Playground Express
# Designed for 9-year-old level (pre-loaded program)

import time
import board
import digitalio
import neopixel

# Set up the distance sensor
trigger = digitalio.DigitalInOut(board.A1)
trigger.direction = digitalio.Direction.OUTPUT

echo = digitalio.DigitalInOut(board.A2)
echo.direction = digitalio.Direction.INPUT

# Set up NeoPixel strip
pixels = neopixel.NeoPixel(board.A3, 10, brightness=0.3)

# Define colors
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
OFF = (0, 0, 0)

def measure_distance():
    """Simple distance measurement"""
    trigger.value = True
    time.sleep(0.00001)
    trigger.value = False
    
    # Wait for echo
    while not echo.value:
        pass
    start = time.monotonic()
    
    while echo.value:
        pass
    end = time.monotonic()
    
    return (end - start) * 17150

# Main loop
while True:
    try:
        distance = measure_distance()
        
        # Clear strip
        pixels.fill(OFF)
        
        if distance < 30:  # Close
            pixels.fill(RED)
        elif distance < 100:  # Medium
            pixels.fill(YELLOW)
        else:  # Far
            pixels.fill(GREEN)
    except:
        pixels.fill(OFF)
    
    time.sleep(0.1)