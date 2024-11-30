# Basic light-responsive star for Circuit Playground Express
# Designed for 9-year-old level

import time
import board
import analogio
import neopixel

# Set up the light sensor
light_sensor = analogio.AnalogIn(board.A1)

# Set up NeoPixel Jewel
jewel = neopixel.NeoPixel(board.A2, 7, brightness=0.3)

# Define colors
WARM_WHITE = (255, 200, 50)   # Cozy, warm color
COLD_WHITE = (200, 200, 255)  # Cooler, blueish white

# Main loop
while True:
    # Get light level (0-100)
    light = (light_sensor.value / 65535) * 100
    
    # Make star brighter when darker
    if light < 30:  # Dark room
        jewel.brightness = 0.8
        jewel.fill(WARM_WHITE)
    elif light < 70:  # Normal room
        jewel.brightness = 0.5
        jewel.fill(WARM_WHITE)
    else:  # Bright room
        jewel.brightness = 0.2
        jewel.fill(COLD_WHITE)
    
    time.sleep(0.1)  # Small delay between readings