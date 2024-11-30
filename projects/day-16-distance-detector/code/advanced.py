# Advanced distance sensor control for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import digitalio
import neopixel
import random
from adafruit_circuitplayground import cp

class DistanceDetector:
    def __init__(self):
        # Set up distance sensor
        self.trigger = digitalio.DigitalInOut(board.A1)
        self.trigger.direction = digitalio.Direction.OUTPUT
        
        self.echo = digitalio.DigitalInOut(board.A2)
        self.echo.direction = digitalio.Direction.INPUT
        
        # Set up NeoPixel strip
        self.pixels = neopixel.NeoPixel(board.A3, 10, brightness=0.3)
        
        # Configuration
        self.distance_history = [100] * 5
        self.alert_threshold = 30  # cm
        self.max_distance = 200  # cm
        self.animation_phase = 0
    
    def measure_distance(self):
        """Get precise distance measurement"""
        try:
            # Send trigger pulse
            self.trigger.value = True
            time.sleep(0.00001)
            self.trigger.value = False
            
            # Wait for echo with timeout
            start = time.monotonic()
            while not self.echo.value:
                if time.monotonic() - start > 0.1:
                    return None
            pulse_start = time.monotonic()
            
            while self.echo.value:
                if time.monotonic() - pulse_start > 0.1:
                    return None
            pulse_end = time.monotonic()
            
            # Calculate distance
            duration = pulse_end - pulse_start
            distance = duration * 17150
            
            return min(self.max_distance, distance)
        except:
            return None
    
    def get_smoothed_distance(self):
        """Apply moving average to distance readings"""
        distance = self.measure_distance()
        if distance is not None:
            self.distance_history = self.distance_history[1:] + [distance]
            return sum(self.distance_history) / len(self.distance_history)
        return None
    
    def map_distance_to_color(self, distance):
        """Create smooth color transition based on distance"""
        if distance < self.alert_threshold:
            # Pulse red when very close
            intensity = (math.sin(self.animation_phase) + 1) / 2
            return (int(255 * intensity), 0, 0)
        elif distance < self.max_distance:
            # Gradient from yellow to green
            ratio = (distance - self.alert_threshold) / \
                    (self.max_distance - self.alert_threshold)
            return (int(255 * (1 - ratio)), int(255 * ratio), 0)
        else:
            return (0, 255, 0)
    
    def update_animation(self):
        """Update animation state"""
        self.animation_phase = (self.animation_phase + 0.2) % (2 * math.pi)
    
    def display_distance(self):
        """Show distance with animated display"""
        distance = self.get_smoothed_distance()
        if distance is not None:
            # Get base color
            color = self.map_distance_to_color(distance)
            
            # Calculate number of pixels to light
            num_pixels = min(10, int(10 * (1 - distance / self.max_distance)))
            
            # Create animation
            self.pixels.fill((0, 0, 0))
            for i in range(num_pixels):
                self.pixels[i] = color
            
            # Add sparkle effect when close
            if distance < self.alert_threshold and random.random() < 0.3:
                sparkle_pixel = random.randint(0, 9)
                self.pixels[sparkle_pixel] = (255, 255, 255)
        else:
            # Error indication
            self.pixels.fill((50, 0, 0))

# Create detector
detector = DistanceDetector()

# Main loop
while True:
    detector.update_animation()
    detector.display_distance()
    
    # Add sound when very close
    distance = detector.get_smoothed_distance()
    if distance is not None and distance < detector.alert_threshold:
        cp.play_tone(440 + (detector.alert_threshold - distance) * 10, 0.1)
    
    time.sleep(0.05)