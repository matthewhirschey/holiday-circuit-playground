# Advanced motion detection for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import digitalio
import neopixel
from adafruit_circuitplayground import cp

# Set up the motion sensor
pir = digitalio.DigitalInOut(board.A1)
pir.direction = digitalio.Direction.INPUT

# Set up the NeoPixel Jewel
jewel = neopixel.NeoPixel(board.A2, 7, brightness=0.3)

# Track detection events
detection_count = 0
last_detection = 0

def rainbow_alert():
    """Rainbow pattern when motion detected"""
    for i in range(255):
        r = (i * 3) % 255
        g = (i * 7) % 255
        b = (i * 11) % 255
        jewel.fill((r, g, b))
        time.sleep(0.01)
        if not pir.value:  # Stop if no motion
            break

def detection_log():
    """Log motion events with timestamps"""
    global detection_count, last_detection
    current_time = time.monotonic()
    detection_count += 1
    time_since_last = current_time - last_detection if last_detection > 0 else 0
    last_detection = current_time
    
    print(f"Motion Event #{detection_count}")
    print(f"Time: {current_time:.2f}s")
    print(f"Time since last: {time_since_last:.2f}s")
    print("-" * 20)
    
    return current_time

def alert_pattern():
    """Create an alert pattern on NeoPixels"""
    # Spin around the jewel
    for i in range(7):
        jewel.fill((0, 0, 0))
        jewel[i] = (255, 0, 0)
        time.sleep(0.1)
    # Flash all
    for _ in range(3):
        jewel.fill((255, 0, 0))
        time.sleep(0.1)
        jewel.fill((0, 0, 0))
        time.sleep(0.1)

# Main loop
while True:
    if pir.value:  # Motion detected
        timestamp = detection_log()
        
        if cp.button_a:  # Button A for rainbow pattern
            rainbow_alert()
        elif cp.button_b:  # Button B for alert pattern
            alert_pattern()
        else:  # Default red glow
            jewel.fill((255, 0, 0))
            
        # Also light up Circuit Playground LEDs
        cp.pixels.fill((255, 0, 0))
    else:
        # Everything off when no motion
        jewel.fill((0, 0, 0))
        cp.pixels.fill((0, 0, 0))
    
    time.sleep(0.1)