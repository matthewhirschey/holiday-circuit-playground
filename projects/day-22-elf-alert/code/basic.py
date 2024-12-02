# Basic multi-sensor elf detector for Circuit Playground Express
# Designed for 9-year-old level

import time
import board
import digitalio
from adafruit_circuitplayground import cp

# Set up motion sensors on A1 and A2
sensors = []
for pin in [board.A1, board.A2]:
    pir = digitalio.DigitalInOut(pin)
    pir.direction = digitalio.Direction.INPUT
    sensors.append(pir)

# Define colors for zones
ZONE_COLORS = [
    (255, 0, 0),    # Zone 1: Red
    (0, 0, 255),    # Zone 2: Blue
]

# Main loop
while True:
    motion_detected = False
    
    # Check each sensor
    for i, sensor in enumerate(sensors):
        if sensor.value:  # Motion detected
            motion_detected = True
            # Light up zone color
            cp.pixels.fill(ZONE_COLORS[i])
            
            # Play tone for zone
            cp.play_tone(440 + (i * 220), 0.1)
            
            # Wait a bit to avoid too many alerts
            time.sleep(0.5)
    
    # If no motion, turn off lights
    if not motion_detected:
        cp.pixels.fill((0, 0, 0))
    
    time.sleep(0.1)