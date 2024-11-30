# Advanced NeoPixel nose control for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import neopixel
import random
from adafruit_circuitplayground import cp

# Set up NeoPixel Jewel
jewel = neopixel.NeoPixel(board.A1, 7, brightness=0.3)

# Define colors
RED = (255, 0, 0)
BRIGHT_RED = (255, 50, 50)
DIM_RED = (64, 0, 0)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

class GlowingNose:
    def __init__(self):
        self.brightness = 0
        self.increasing = True
        self.speed = 0.05
        self.max_bright = 255
        self.min_bright = 20
        self.phase = 0
        self.pattern_index = 0
    
    def breath_effect(self):
        """Create smooth breathing light effect"""
        if self.increasing:
            self.brightness += 5
            if self.brightness >= self.max_bright:
                self.increasing = False
        else:
            self.brightness -= 5
            if self.brightness <= self.min_bright:
                self.increasing = True
        
        return (self.brightness, 0, 0)
    
    def sparkle_effect(self):
        """Create random sparkle pattern"""
        pixels = [OFF] * 7
        bright_pixel = random.randint(0, 6)
        pixels[bright_pixel] = BRIGHT_RED
        return pixels
    
    def candy_cane_spin(self):
        """Red and white spinning pattern"""
        pixels = []
        for i in range(7):
            if (i + self.phase) % 2 == 0:
                pixels.append(RED)
            else:
                pixels.append(WHITE)
        self.phase = (self.phase + 1) % 2
        return pixels
    
    def wave_effect(self):
        """Create wave of brightness"""
        pixels = []
        for i in range(7):
            brightness = int(((math.sin(self.phase + i/2) + 1) / 2) * 255)
            pixels.append((brightness, 0, 0))
        self.phase = (self.phase + 0.2) % (2 * math.pi)
        return pixels

# Create nose controller
nose = GlowingNose()

# Main loop
while True:
    if cp.button_a:
        # Breathing effect
        color = nose.breath_effect()
        jewel.fill(color)
    elif cp.button_b:
        # Sparkle effect
        pixels = nose.sparkle_effect()
        for i in range(7):
            jewel[i] = pixels[i]
    elif cp.button_a and cp.button_b:
        # Candy cane spin
        pixels = nose.candy_cane_spin()
        for i in range(7):
            jewel[i] = pixels[i]
    else:
        # Default wave effect
        pixels = nose.wave_effect()
        for i in range(7):
            jewel[i] = pixels[i]
    
    time.sleep(0.05)