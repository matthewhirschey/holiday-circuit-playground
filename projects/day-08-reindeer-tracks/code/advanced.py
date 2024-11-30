# Advanced motion detection for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import digitalio
import neopixel
from adafruit_circuitplayground import cp

class MotionDetector:
    def __init__(self):
        # Set up PIR sensor on A1
        self.pir = digitalio.DigitalInOut(board.A1)
        self.pir.direction = digitalio.Direction.INPUT
        
        # Set up NeoPixel Jewel on A2
        self.jewel = neopixel.NeoPixel(board.A2, 7, brightness=0.3)
        
        # Track detection events
        self.detection_count = 0
        self.last_detection = 0
        self.alert_mode = False
    
    def rainbow_alert(self):
        """Rainbow pattern when motion detected"""
        for i in range(255):
            r = (i * 3) % 255
            g = (i * 7) % 255
            b = (i * 11) % 255
            self.jewel.fill((r, g, b))
            # Stop if no more motion
            if not self.pir.value:
                break
            time.sleep(0.01)
    
    def detection_log(self):
        """Log motion events with timestamps"""
        current_time = time.monotonic()
        self.detection_count += 1
        time_since_last = current_time - self.last_detection if self.last_detection > 0 else 0
        self.last_detection = current_time
        
        print(f"Motion Event #{self.detection_count}")
        print(f"Time: {current_time:.2f}s")
        print(f"Time since last: {time_since_last:.2f}s")
        print("-" * 20)
        
        return current_time
    
    def alert_pattern(self):
        """Create an alert pattern on NeoPixels"""
        # Spin around the jewel
        for i in range(7):
            self.jewel.fill((0, 0, 0))
            self.jewel[i] = (255, 0, 0)
            time.sleep(0.1)
        # Flash all
        for _ in range(3):
            self.jewel.fill((255, 0, 0))
            time.sleep(0.1)
            self.jewel.fill((0, 0, 0))
            time.sleep(0.1)
    
    def update(self):
        """Main update function"""
        if self.pir.value:  # Motion detected
            # Log the event
            self.detection_log()
            
            # Choose pattern based on buttons
            if cp.button_a:
                self.rainbow_alert()
            elif cp.button_b:
                self.alert_pattern()
            else:
                self.jewel.fill((255, 0, 0))
            
            # Also light up Circuit Playground LEDs
            cp.pixels.fill((255, 0, 0))
        else:
            # Everything off when no motion
            self.jewel.fill((0, 0, 0))
            cp.pixels.fill((0, 0, 0))

# Create detector
detector = MotionDetector()

# Main loop
while True:
    detector.update()
    time.sleep(0.1)