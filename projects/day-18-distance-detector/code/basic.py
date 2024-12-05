# Basic distance detector for Circuit Playground Express
# Designed for 9-year-old level

import time
import board
import digitalio
from adafruit_circuitplayground import cp

# Set up trigger pin on A2
trigger = digitalio.DigitalInOut(board.A2)
trigger.direction = digitalio.Direction.OUTPUT

# Set up echo pin on A1 (through voltage divider!)
echo = digitalio.DigitalInOut(board.A1)
echo.direction = digitalio.Direction.INPUT

def get_distance():
    """Measure distance safely with timeouts"""
    # Send trigger pulse
    trigger.value = True
    time.sleep(0.00001)    # 10 microseconds
    trigger.value = False
    
    # Wait for echo to start (with timeout)
    timeout = time.monotonic() + 0.1
    while not echo.value:
        if time.monotonic() > timeout:
            return None
    pulse_start = time.monotonic()
    
    # Wait for echo to end (with timeout)
    timeout = time.monotonic() + 0.1
    while echo.value:
        if time.monotonic() > timeout:
            return None
    pulse_end = time.monotonic()
    
    # Calculate distance
    distance = ((pulse_end - pulse_start) * 34300) / 2
    
    # Only return reasonable values
    if distance < 2 or distance > 400:
        return None
    return distance

# Main loop
while True:
    # Get distance measurement
    distance = get_distance()
    
    if distance is not None:
        # Light up pixels based on distance
        pixels_to_light = min(10, int(distance / 30))
        
        # Update Circuit Playground LEDs
        for i in range(10):
            if i < pixels_to_light:
                cp.pixels[i] = (0, 255, 0)  # Green
            else:
                cp.pixels[i] = (0, 0, 0)    # Off
    else:
        # Show error with red light
        cp.pixels.fill((10, 0, 0))  # Dim red
    
    time.sleep(0.1)