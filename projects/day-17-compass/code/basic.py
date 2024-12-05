# Basic compass for Circuit Playground Express
# Designed for 9-year-old level

import time
import board
import math
import adafruit_lsm303agr_mag
from adafruit_circuitplayground import cp

# Set up the magnetometer
i2c = board.I2C()
mag = adafruit_lsm303agr_mag.LSM303AGR_Mag(i2c)

# Define colors
NORTH = (255, 0, 0)    # Red for north
OTHER = (0, 0, 255)    # Blue for other directions
OFF = (0, 0, 0)        # LEDs off

# Main loop
while True:
    try:
        # Read magnetic values
        mag_x, mag_y, mag_z = mag.magnetic
        
        # Calculate heading (0-360 degrees)
        heading = (math.atan2(mag_y, mag_x) * 180) / math.pi
        heading = (heading + 360) % 360
        
        # Convert heading to pixel position (0-9)
        pixel = int((heading / 360.0) * 10)
        
        # Update display
        cp.pixels.fill(OFF)
        if 350 <= heading or heading <= 10:  # North ±10 degrees
            cp.pixels[pixel] = NORTH
        else:
            cp.pixels[pixel] = OTHER
        
        # Optional: Play tone when pointing north
        if cp.button_a and (350 <= heading or heading <= 10):
            cp.play_tone(880, 0.1)
        
    except Exception as e:
        # Flash red if there's an error
        cp.pixels.fill((50, 0, 0))
        time.sleep(0.2)
        cp.pixels.fill(OFF)
        time.sleep(0.2)
    
    time.sleep(0.1)