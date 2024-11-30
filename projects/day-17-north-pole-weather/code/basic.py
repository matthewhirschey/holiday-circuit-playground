# Basic weather station for Circuit Playground Express
# Designed for 9-year-old level (pre-loaded program)

import time
import board
import adafruit_dht
import neopixel

# Set up temperature sensor
dht = adafruit_dht.DHT22(board.A1)

# Set up NeoPixel strip
pixels = neopixel.NeoPixel(board.A2, 10, brightness=0.3)

# Define colors
BLUE = (0, 0, 255)    # Cold
GREEN = (0, 255, 0)   # Comfortable
RED = (255, 0, 0)     # Warm
OFF = (0, 0, 0)

# Main loop
while True:
    try:
        # Read sensor
        temperature = dht.temperature
        humidity = dht.humidity
        
        # Set color based on temperature
        if temperature < 0:
            color = BLUE
        elif temperature < 20:
            color = GREEN
        else:
            color = RED
        
        # Fill strip with color
        pixels.fill(color)
        
        # Turn off pixels based on humidity
        pixels_on = int(humidity / 10)
        for i in range(pixels_on, 10):
            pixels[i] = OFF
            
    except RuntimeError:
        # Flash red if error
        pixels.fill(RED)
        time.sleep(0.1)
        pixels.fill(OFF)
    
    time.sleep(2)  # Wait between readings