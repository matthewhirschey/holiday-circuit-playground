# Basic light sensor control for Circuit Playground Express
# Designed for 9-year-old level (pre-loaded program)

import time
import board
import analogio
import neopixel

# Set up the light sensor
light_sensor = analogio.AnalogIn(board.A1)

# Set up NeoPixel Jewel
jewel = neopixel.NeoPixel(board.A2, 7, brightness=0.3)

# Define colors
WHITE = (255, 255, 255)
WARM_WHITE = (255, 200, 100)

# Main loop
while True:
    # Get light level (0-100)
    light = (light_sensor.value / 65535) * 100
    
    # Make star brighter when darker
    brightness = 1.0 - (light / 100)
    jewel.brightness = max(0.1, min(1.0, brightness))
    
    # Use warmer color when dimmer
    if brightness > 0.7:
        jewel.fill(WARM_WHITE)
    else:
        jewel.fill(WHITE)
    
    time.sleep(0.1)