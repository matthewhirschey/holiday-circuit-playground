# Advanced weather station for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import adafruit_ahtx0
import array
import math
from adafruit_circuitplayground import cp

class WeatherStation:
    def __init__(self):
        # Set up the AHT20 sensor
        i2c = board.I2C()
        self.sensor = adafruit_ahtx0.AHTx0(i2c)
        
        # Data tracking
        self.temp_history = array.array('f', [20.0] * 10)
        self.humid_history = array.array('f', [50.0] * 10)
        self.history_index = 0
        
        # Animation
        self.animation_phase = 0
        
        # Temperature thresholds
        self.COLD = 18
        self.WARM = 25
    
    def update_history(self):
        """Update rolling averages"""
        try:
            # Get new readings
            temp = self.sensor.temperature
            humid = self.sensor.relative_humidity
            
            # Update history
            self.temp_history[self.history_index] = temp
            self.humid_history[self.history_index] = humid
            self.history_index = (self.history_index + 1) % 10
            
            return True
        except Exception:
            return False
    
    def get_averages(self):
        """Get current averages"""
        avg_temp = sum(self.temp_history) / len(self.temp_history)
        avg_humid = sum(self.humid_history) / len(self.humid_history)
        return avg_temp, avg_humid
    
    def temp_to_color(self, temp):
        """Create smooth color transitions"""
        if temp < self.COLD:
            # Blue to green
            ratio = max(0, temp / self.COLD)
            return (0, int(255 * ratio), int(255 * (1 - ratio)))
        elif temp < self.WARM:
            # Green to red
            ratio = (temp - self.COLD) / (self.WARM - self.COLD)
            return (int(255 * ratio), int(255 * (1 - ratio)), 0)
        else:
            # Full red
            return (255, 0, 0)
    
    def show_readings(self):
        """Display temperature and humidity"""
        avg_temp, avg_humid = self.get_averages()
        
        # Update NeoPixels
        color = self.temp_to_color(avg_temp)
        for i in range(10):
            # Create wave effect
            brightness = (math.sin(self.animation_phase + i/2) + 1) / 2
            adjusted_color = tuple(int(c * brightness) for c in color)
            cp.pixels[i] = adjusted_color
        
        self.animation_phase += 0.1
    
    def check_alerts(self):
        """Check for extreme conditions"""
        avg_temp, avg_humid = self.get_averages()
        
        # Temperature alerts
        if avg_temp < 10:  # Too cold
            cp.play_tone(880, 0.1)  # High beep
        elif avg_temp > 30:  # Too hot
            cp.play_tone(220, 0.1)  # Low beep
        
        # Humidity alerts
        if avg_humid > 80:  # Too humid
            cp.play_tone(440, 0.1)  # Mid beep
    
    def print_status(self):
        """Print current readings"""
        avg_temp, avg_humid = self.get_averages()
        print(f"Temperature: {avg_temp:.1f} °C")
        print(f"Humidity: {avg_humid:.1f} %")
        print("-" * 20)

# Create weather station
station = WeatherStation()

# Main loop
while True:
    if station.update_history():
        station.show_readings()
        
        if cp.button_a:
            station.print_status()
        if cp.button_b:
            station.check_alerts()
    else:
        # Error indication
        cp.pixels.fill((50, 0, 0))
        time.sleep(0.2)
        cp.pixels.fill((0, 0, 0))
        time.sleep(0.2)
    
    time.sleep(0.05)