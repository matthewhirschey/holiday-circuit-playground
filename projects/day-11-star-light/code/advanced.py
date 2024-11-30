# Advanced light-responsive star for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import analogio
import neopixel
import math
from adafruit_circuitplayground import cp

class TwinklingStar:
    def __init__(self):
        # Set up light sensor
        self.light_sensor = analogio.AnalogIn(board.A1)
        
        # Set up NeoPixel Jewel
        self.jewel = neopixel.NeoPixel(board.A2, 7, brightness=0.3)
        
        # Track state
        self.current_brightness = 0.3
        self.target_brightness = 0.3
        self.twinkle_phase = 0
        self.light_history = [50] * 10  # Store last 10 readings
    
    def get_smooth_light(self):
        """Get averaged light reading"""
        current = (self.light_sensor.value / 65535) * 100
        self.light_history = self.light_history[1:] + [current]
        return sum(self.light_history) / len(self.light_history)
    
    def color_from_light(self, light_level):
        """Create color based on light level"""
        # Interpolate between warm and cool white
        warmth = max(0, min(1, (70 - light_level) / 40))
        return (
            255,  # Red stays full
            int(200 + (55 * (1 - warmth))),  # Green increases
            int(50 + (205 * (1 - warmth)))    # Blue increases
        )
    
    def twinkle_effect(self):
        """Create gentle twinkling"""
        self.twinkle_phase += 0.1
        base_brightness = self.current_brightness
        twinkle = (math.sin(self.twinkle_phase) + 1) / 2 * 0.2
        return base_brightness + twinkle
    
    def update_brightness(self, target):
        """Smoothly adjust brightness"""
        step = 0.05
        if self.current_brightness < target:
            self.current_brightness = min(
                self.current_brightness + step, target)
        else:
            self.current_brightness = max(
                self.current_brightness - step, target)
    
    def run_display(self):
        """Main update function"""
        # Get light reading
        light = self.get_smooth_light()
        
        # Calculate target brightness (inverse of light)
        self.target_brightness = 0.9 - (light / 100) * 0.6
        
        # Update current brightness
        self.update_brightness(self.target_brightness)
        
        # Add twinkle when dark
        if light < 30:
            brightness = self.twinkle_effect()
        else:
            brightness = self.current_brightness
        
        # Update jewel
        self.jewel.brightness = brightness
        self.jewel.fill(self.color_from_light(light))
        
        # Optional: Show light level on CPX
        pixels_on = int(light / 10)  # 0-100 maps to 0-10 LEDs
        for i in range(10):
            if i < pixels_on:
                cp.pixels[i] = (10, 10, 10)  # Dim white
            else:
                cp.pixels[i] = (0, 0, 0)

# Create star controller
star = TwinklingStar()

# Main loop
while True:
    star.run_display()
    time.sleep(0.05)