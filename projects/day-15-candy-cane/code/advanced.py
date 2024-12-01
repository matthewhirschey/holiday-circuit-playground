# Advanced NeoPixel candy cane for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import neopixel
import random
import math
from adafruit_circuitplayground import cp

class CandyCane:
    def __init__(self):
        # Set up NeoPixel strip
        self.pixels = neopixel.NeoPixel(board.A1, 5, brightness=0.3)
        
        # Animation settings
        self.speed = 0.1
        self.phase = 0
        self.pattern = 0
        
        # Colors
        self.RED = (255, 0, 0)
        self.WHITE = (255, 255, 255)
        self.OFF = (0, 0, 0)
    
    def classic_pattern(self):
        """Traditional red and white stripes"""
        for i in range(5):
            self.pixels[i] = self.RED if i % 2 == 0 else self.WHITE
    
    def spin_pattern(self):
        """Create spinning effect"""
        position = int(self.phase) % 5
        self.pixels.fill(self.RED)
        self.pixels[position] = self.WHITE
        self.phase += 0.2
    
    def fade_pattern(self):
        """Fade between red and white"""
        brightness = (math.sin(self.phase) + 1) / 2
        color = (255, int(255 * brightness), int(255 * brightness))
        self.pixels.fill(color)
        self.phase += 0.1
    
    def sparkle_pattern(self):
        """Random twinkling effect"""
        for i in range(5):
            if random.random() > 0.7:
                self.pixels[i] = self.WHITE
            else:
                self.pixels[i] = self.RED
    
    def wave_pattern(self):
        """Create wave of brightness"""
        for i in range(5):
            brightness = (math.sin(self.phase + i/2) + 1) / 2
            self.pixels[i] = (int(255 * brightness), 0, 0)
        self.phase += 0.1
    
    def run_pattern(self):
        """Update animation based on buttons"""
        if cp.button_a:
            self.spin_pattern()
        elif cp.button_b:
            self.wave_pattern()
        elif cp.button_a and cp.button_b:
            self.sparkle_pattern()
        else:
            self.classic_pattern()
        
        # Optional: Show pattern on CPX LEDs too
        for i in range(10):
            if i < 5:
                cp.pixels[i] = self.pixels[i]
            else:
                cp.pixels[i] = self.OFF

# Create candy cane controller
cane = CandyCane()

# Main loop
while True:
    cane.run_pattern()
    time.sleep(0.05)