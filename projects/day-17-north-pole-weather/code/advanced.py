# Advanced weather station for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import adafruit_dht
import neopixel
import math
from adafruit_circuitplayground import cp

class WeatherStation:
    def __init__(self):
        self.dht = adafruit_dht.DHT22(board.A1)
        self.pixels = neopixel.NeoPixel(board.A2, 10, brightness=0.3)
        
        # Store reading history
        self.temp_history = [20] * 10
        self.humid_history = [50] * 10
        self.temp_min = float('inf')
        self.temp_max = float('-inf')
        
        # Animation settings
        self.animation_phase = 0
        self.alert_mode = False
    
    def get_smoothed_readings(self):
        """Get averaged sensor readings"""
        try:
            temp = self.dht.temperature
            humid = self.dht.humidity
            
            # Update history
            self.temp_history = self.temp_history[1:] + [temp]
            self.humid_history = self.humid_history[1:] + [humid]
            
            # Update min/max
            self.temp_min = min(self.temp_min, temp)
            self.temp_max = max(self.temp_max, temp)
            
            # Calculate averages
            avg_temp = sum(self.temp_history) / len(self.temp_history)
            avg_humid = sum(self.humid_history) / len(self.humid_history)
            
            return avg_temp, avg_humid
        except RuntimeError:
            return None, None
    
    def temp_to_gradient(self, temp):
        """Create color gradient based on temperature"""
        if temp < 0:
            # Cold: white to blue
            ratio = min(1.0, abs(temp) / 10)
            return (int(255 * (1 - ratio)), int(255 * (1 - ratio)), 255)
        elif temp < 20:
            # Comfortable: blue to green
            ratio = temp / 20
            return (0, int(255 * ratio), int(255 * (1 - ratio)))
        else:
            # Warm: green to red
            ratio = min(1.0, (temp - 20) / 15)
            return (int(255 * ratio), int(255 * (1 - ratio)), 0)
    
    def check_alerts(self, temp, humid):
        """Check for extreme conditions"""
        if temp < -10 or temp > 30 or humid > 90:
            self.alert_mode = True
            # Play alert tone
            if not cp.switch:
                cp.play_tone(880, 0.1)
        else:
            self.alert_mode = False
    
    def display_weather(self):
        """Create weather visualization"""
        temp, humid = self.get_smoothed_readings()
        if temp is not None:
            # Check for alerts
            self.check_alerts(temp, humid)
            
            # Get base color
            color = self.temp_to_gradient(temp)
            
            # Create display pattern
            for i in range(10):
                if i < (humid / 10):
                    if self.alert_mode:
                        # Flashing effect for alerts
                        brightness = (math.sin(time.monotonic() * 4) + 1) / 2
                    else:
                        # Gentle shimmer for normal mode
                        brightness = (math.sin(time.monotonic() * 2 + i) + 1) / 2
                    
                    pixels[i] = tuple(int(c * brightness) for c in color)
                else:
                    pixels[i] = (0, 0, 0)
            
            # Update animation
            self.animation_phase += 0.1
        else:
            # Error indication
            pixels.fill((50, 0, 0))

# Create weather station
station = WeatherStation()

# Main loop
while True:
    station.display_weather()
    time.sleep(0.1)