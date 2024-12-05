# Advanced multi-sensor elf detector for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import digitalio
import array
import math
from adafruit_circuitplayground import cp

class ElfDetector:
    def __init__(self):
        # Set up motion sensors
        self.sensors = []
        self.sensor_pins = [board.A1, board.A2, board.A3, board.A4]
        
        for pin in self.sensor_pins:
            pir = digitalio.DigitalInOut(pin)
            pir.direction = digitalio.Direction.INPUT
            self.sensors.append(pir)
        
        # Detection tracking
        self.last_detection = [0] * len(self.sensors)
        self.active_zones = []
        self.alert_phase = 0
        
        # Zone colors
        self.COLORS = [
            (255, 0, 0),    # Zone 1: Red
            (0, 0, 255),    # Zone 2: Blue
            (0, 255, 0),    # Zone 3: Green
            (255, 255, 0),  # Zone 4: Yellow
        ]
    
    def check_zones(self):
        """Check all zones and track timing"""
        current_time = time.monotonic()
        active = []
        
        for i, sensor in enumerate(self.sensors):
            if sensor.value:
                active.append(i)
                self.last_detection[i] = current_time
        
        self.active_zones = active
        return active
    
    def zone_alert(self, zone):
        """Create alert pattern for single zone"""
        base_color = self.COLORS[zone]
        # Pulse effect
        brightness = (math.sin(self.alert_phase) + 1) / 2
        color = tuple(int(c * brightness) for c in base_color)
        cp.pixels.fill(color)
        
        # Play zone-specific tone
        if self.alert_phase % (2 * math.pi) < 0.1:
            cp.play_tone(440 + (zone * 220), 0.1)
    
    def multi_zone_alert(self):
        """Create alert pattern for multiple zones"""
        # Rotating colors
        for i in range(10):
            pos = (i + int(self.alert_phase * 2)) % 10
            zone_index = pos % len(self.active_zones)
            cp.pixels[i] = self.COLORS[self.active_zones[zone_index]]
        
        # Play alert sequence
        if self.alert_phase % 1 < 0.1:
            for zone in self.active_zones:
                cp.play_tone(440 + (zone * 110), 0.05)
    
    def movement_tracking(self):
        """Track movement patterns"""
        current_time = time.monotonic()
        recent_zones = [i for i, time in enumerate(self.last_detection)
                       if current_time - time < 2.0]
        
        if len(recent_zones) > 1:
            # Sort by detection time to see movement direction
            recent_zones.sort(key=lambda x: self.last_detection[x])
            return recent_zones
        return None
    
    def update_display(self):
        """Update display based on detections"""
        self.alert_phase += 0.1
        
        active = self.check_zones()
        if len(active) > 1:
            # Multiple zones - special pattern
            self.multi_zone_alert()
            
            # Check for movement patterns
            movement = self.movement_tracking()
            if movement:
                print(f"Movement pattern: {movement}")
        
        elif active:
            # Single zone - simple alert
            self.zone_alert(active[0])
        
        else:
            # No detection - turn off
            cp.pixels.fill((0, 0, 0))

# Create detector
detector = ElfDetector()

# Main loop
while True:
    try:
        detector.update_display()
        time.sleep(0.05)
    except Exception as e:
        # Error indication
        print(f"Error: {e}")
        cp.pixels.fill((50, 0, 0))
        time.sleep(0.2)
        cp.pixels.fill((0, 0, 0))
        time.sleep(0.2)