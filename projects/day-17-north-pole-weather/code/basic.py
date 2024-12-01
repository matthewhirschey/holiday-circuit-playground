# Basic weather station for Circuit Playground Express
# Designed for 9-year-old level

import time
import board
import adafruit_ahtx0
from adafruit_circuitplayground import cp

# Set up the AHT20 sensor
i2c = board.I2C()
sensor = adafruit_ahtx0.AHTx0(i2c)

# Define colors
BLUE = (0, 0, 255)    # Cold
GREEN = (0, 255, 0)   # Comfortable
RED = (255, 0, 0)     # Warm

# Main loop
while True:
    try:
        # Get temperature in Celsius
        temperature = sensor.temperature
        humidity = sensor.relative_humidity
        
        # Show temperature with colors
        if temperature < 18:  # Cold
            cp.pixels.fill(BLUE)
        elif temperature < 25:  # Comfortable
            cp.pixels.fill(GREEN)
        else:  # Warm
            cp.pixels.fill(RED)
            
        # Optional: Show humidity with brightness
        brightness = max(0.1, min(1.0, humidity / 100))
        cp.pixels.brightness = brightness
        
        # Play tone based on temperature (if button A pressed)
        if cp.button_a:
            tone_freq = 500 + (temperature * 50)
            cp.play_tone(tone_freq, 0.1)
        
    except Exception as e:
        # Flash red if there's an error
        cp.pixels.fill((50, 0, 0))
        time.sleep(0.2)
        cp.pixels.fill((0, 0, 0))
        time.sleep(0.2)
    
    time.sleep(0.5)