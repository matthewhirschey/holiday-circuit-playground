# Advanced NeoPixel Jewel control for Circuit Playground Express
# Designed for 13-year-old level - works with either connection method

import time
import board
import neopixel
import math
from adafruit_circuitplayground import cp

class GlowingNose:
    def __init__(self):
        # Set up NeoPixel Jewel
        self.jewel = neopixel.NeoPixel(board.A1, 7, brightness=0.3)
        
        # Animation settings
        self.brightness = 0.3
        self.phase = 0
        self.mode = 0
        
        # Colors
        self.RED = (255, 0, 0)
        self.BRIGHT_RED = (255, 50, 50)
        self.WARM_RED = (255, 30, 0)
    
    def pulse_pattern(self):
        """Create breathing effect"""
        self.phase += 0.1
        brightness = (math.sin(self.phase) + 1) / 2
        return (int(255 * brightness), 0, 0)
    
    def sparkle_pattern(self):
        """Create random sparkle effect"""
        self.jewel.fill(self.RED)
        # Add random bright pixel
        i = random.randint(0, 6)
        self.jewel[i] = self.BRIGHT_RED
        time.sleep(0.1)
    
    def spin_pattern(self):
        """Create spinning light effect"""
        self.jewel.fill((0, 0, 0))
        pos = int(self.phase) % 7
        # Main light
        self.jewel[pos] = self.BRIGHT_RED
        # Fade on either side
        self.jewel[(pos-1) % 7] = self.WARM_RED
        self.jewel[(pos+1) % 7] = self.WARM_RED
        self.phase += 0.2
    
    def run_display(self):
        """Main update function"""
        if cp.button_a:
            # Breathing pattern
            color = self.pulse_pattern()
            self.jewel.fill(color)
            
        elif cp.button_b:
            # Spinning pattern
            self.spin_pattern()
            
        elif cp.button_a and cp.button_b:
            # Sparkle pattern
            self.sparkle_pattern()
        else:
            # Default glow
            self.jewel.fill(self.RED)
        
        # Optional: Show mode on CPX LEDs
        if self.mode == 0:
            cp.pixels[0] = (10, 0, 0)  # Dim red
        else:
            cp.pixels[0] = (0, 0, 0)

# Create nose controller
nose = GlowingNose()

# Main loop
while True:
    nose.run_display()
    time.sleep(0.01)