# Advanced light sensor control for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import analogio
import neopixel
import random

# Set up the light sensor
light_sensor = analogio.AnalogIn(board.A1)

# Set up NeoPixel Jewel
jewel = neopixel.NeoPixel(board.A2, 7, brightness=0.3)

class AdaptiveStar:
    def __init__(self):
        self.light_history = [50] * 10  # Store last 10 readings
        self.effect_mode = 0
        self.twinkle_state = False
        self.color_temp = 255  # Track color temperature
    
    def update_history(self, light_level):
        """Update rolling average of light readings"""
        self.light_history = self.light_history[1:] + [light_level]
        return sum(self.light_history) / len(self.light_history)
    
    def get_adaptive_brightness(self, light_level):
        """Smooth brightness transitions"""
        avg_light = self.update_history(light_level)
        return 1.0 - (avg_light / 100)
    
    def twinkle_effect(self, base_brightness):
        """Create twinkling effect in dark"""
        if base_brightness > 0.7:  # Only twinkle when dark
            self.twinkle_state = not self.twinkle_state
            return base_brightness * (0.7 if self.twinkle_state else 1.0)
        return base_brightness
    
    def get_color_temp(self, brightness):
        """Adjust color temperature based on brightness"""
        # Warmer color when dimmer
        self.color_temp = int(255 - (brightness * 100))
        return (255, self.color_temp, self.color_temp // 2)
    
    def sparkle_effect(self):
        """Create random sparkle effect"""
        pixel = random.randint(0, 6)
        original_color = jewel[pixel]
        jewel[pixel] = (255, 255, 255)
        time.sleep(0.05)
        jewel[pixel] = original_color

# Initialize star controller
star = AdaptiveStar()

# Main loop
while True:
    # Get light level
    light = (light_sensor.value / 65535) * 100
    
    # Update brightness with smooth transitions
    brightness = star.get_adaptive_brightness(light)
    
    # Apply effects based on brightness
    if brightness > 0.7:
        brightness = star.twinkle_effect(brightness)
        if random.random() < 0.1:  # 10% chance of sparkle
            star.sparkle_effect()
    
    # Update star
    jewel.brightness = max(0.1, min(1.0, brightness))
    jewel.fill(star.get_color_temp(brightness))
    
    time.sleep(0.1)