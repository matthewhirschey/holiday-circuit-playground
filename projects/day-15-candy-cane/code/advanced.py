# Advanced NeoPixel strip control for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import neopixel
import random
import math
from adafruit_circuitplayground import cp

class CandyCane:
    def __init__(self):
        self.strip = neopixel.NeoPixel(board.A1, 10, brightness=0.3)
        self.offset = 0
        self.fade_level = 0
        self.fade_in = True
        self.pattern_index = 0
    
    def smooth_fade(self):
        """Create smooth fading effect"""
        if self.fade_in:
            self.fade_level += 5
            if self.fade_level >= 255:
                self.fade_in = False
        else:
            self.fade_level -= 5
            if self.fade_level <= 50:
                self.fade_in = True
        
        red = (self.fade_level, 0, 0)
        white = (self.fade_level, self.fade_level, self.fade_level)
        return red, white
    
    def sparkle_effect(self):
        """Add random sparkles to pattern"""
        self.strip.fill((0, 0, 0))
        for _ in range(3):
            i = random.randint(0, 9)
            self.strip[i] = (255, 255, 255)
        time.sleep(0.05)
    
    def wave_pattern(self):
        """Create sine wave brightness pattern"""
        for i in range(10):
            brightness = int(((math.sin(self.offset + i/2) + 1) / 2) * 255)
            if i % 2 == 0:
                self.strip[i] = (brightness, 0, 0)  # Red
            else:
                self.strip[i] = (brightness, brightness, brightness)  # White
        self.offset += 0.2
    
    def candy_spiral(self):
        """Create spinning spiral effect"""
        for i in range(10):
            pos = (i + int(self.offset)) % 10
            if pos < 5:  # First half red, second half white
                self.strip[i] = (255, 0, 0)
            else:
                self.strip[i] = (255, 255, 255)
        self.offset = (self.offset + 0.5) % 10
    
    def update(self):
        """Update animation based on current pattern"""
        if cp.button_a:
            red, white = self.smooth_fade()
            for i in range(10):
                self.strip[i] = red if i % 2 == 0 else white
        elif cp.button_b:
            self.wave_pattern()
        elif cp.button_a and cp.button_b:
            self.candy_spiral()
        else:
            self.sparkle_effect()

# Create candy cane controller
cane = CandyCane()

# Main loop
while True:
    cane.update()
    time.sleep(0.05)