# Advanced distance detector for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import digitalio
import array
import math
from adafruit_circuitplayground import cp

class DistanceDetector:
    def __init__(self):
        # Set up trigger pin
        self.trigger = digitalio.DigitalInOut(board.A2)
        self.trigger.direction = digitalio.Direction.OUTPUT
        
        # Set up echo pin (through voltage divider!)
        self.echo = digitalio.DigitalInOut(board.A1)
        self.echo.direction = digitalio.Direction.INPUT
        
        # Distance tracking
        self.history = array.array('f', [0] * 5)  # Last 5 readings
        self.history_index = 0
        self.valid_reading_count = 0
        
        # Animation
        self.alert_phase = 0
    
    def measure_distance(self):
        """Get distance measurement with safety checks"""
        try:
            # Send trigger pulse
            self.trigger.value = True
            time.sleep(0.00001)    # 10 microseconds
            self.trigger.value = False
            
            # Wait for echo to start (with timeout)
            timeout = time.monotonic() + 0.1
            while not self.echo.value:
                if time.monotonic() > timeout:
                    return None
            pulse_start = time.monotonic()
            
            # Wait for echo to end (with timeout)
            timeout = time.monotonic() + 0.1
            while self.echo.value:
                if time.monotonic() > timeout:
                    return None
            pulse_end = time.monotonic()
            
            # Calculate distance
            distance = ((pulse_end - pulse_start) * 34300) / 2
            
            # Validate reading
            if distance < 2 or distance > 400:
                return None
                
            return distance
            
        except RuntimeError:
            return None
    
    def update_history(self, distance):
        """Update rolling average of readings"""
        if distance is not None:
            self.history[self.history_index] = distance
            self.history_index = (self.history_index + 1) % 5
            if self.valid_reading_count < 5:
                self.valid_reading_count += 1
    
    def get_average_distance(self):
        """Get smoothed distance value"""
        if self.valid_reading_count == 0:
            return None
        return sum(self.history) / self.valid_reading_count
    
    def show_distance_neopixels(self, distance):
        """Display distance on NeoPixels with effects"""
        if distance is None:
            # Error indication
            cp.pixels.fill((10, 0, 0))  # Dim red
            return
        
        # Calculate display parameters
        max_distance = 200  # cm
        brightness = max(0.1, min(1.0, 1.0 - (distance / max_distance)))
        pixels_to_light = min(10, int(distance / 20))
        
        # Create color based on distance
        if distance < 30:
            color = (255, 0, 0)  # Red for close
        elif distance < 100:
            color = (255, 255, 0)  # Yellow for medium
        else:
            color = (0, 255, 0)  # Green for far
        
        # Update pixels
        for i in range(10):
            if i < pixels_to_light:
                cp.pixels[i] = tuple(int(c * brightness) for c in color)
            else:
                cp.pixels[i] = (0, 0, 0)
    
    def run_detector(self):
        """Main update function"""
        # Get new reading
        distance = self.measure_distance()
        
        # Update tracking
        self.update_history(distance)
        avg_distance = self.get_average_distance()
        
        # Update display
        self.show_distance_neopixels(avg_distance)
        
        # Print debug info
        if avg_distance is not None:
            print(f"Distance: {avg_distance:.1f} cm")
        
        # Optional: sound alert for close objects
        if avg_distance is not None and avg_distance < 30:
            cp.play_tone(1000 + (30 - avg_distance) * 20, 0.1)

# Create detector
detector = DistanceDetector()

# Main loop
while True:
    detector.run_detector()
    time.sleep(0.05)