# Advanced NeoPixel Ring light show for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import neopixel
import math
import random
from adafruit_circuitplayground import cp

class LightShow:
    def __init__(self):
        # Set up NeoPixel Ring
        self.ring = neopixel.NeoPixel(board.A1, 24, brightness=0.3)
        
        # Animation settings
        self.phase = 0
        self.mode = 0
        self.speed = 1.0
        
        # Color settings
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.WHITE = (255, 255, 255)
        self.GOLD = (255, 200, 0)
    
    def wheel(self, pos):
        """Generate rainbow colors"""
        if pos < 85:
            return (pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return (255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return (0, pos * 3, 255 - pos * 3)
    
    def pulse_pattern(self):
        """Create pulsing wave effect"""
        intensity = (math.sin(self.phase) + 1) / 2
        color = tuple(int(c * intensity) for c in self.GOLD)
        self.ring.fill(color)
        self.phase += 0.1
    
    def comet_tail(self):
        """Create comet effect with fading tail"""
        self.ring.fill((0, 0, 0))
        pos = int(self.phase * 2) % 24
        
        # Bright head
        self.ring[pos] = self.WHITE
        
        # Fading tail
        for i in range(12):
            tail_pos = (pos - i) % 24
            brightness = 1.0 - (i / 12)
            self.ring[tail_pos] = tuple(int(255 * brightness) for _ in range(3))
        
        self.phase += self.speed
    
    def sparkle_fade(self):
        """Create random sparkles that fade"""
        # Fade existing pixels
        for i in range(24):
            r, g, b = self.ring[i]
            self.ring[i] = (max(0, r-10), max(0, g-10), max(0, b-10))
        
        # Add new sparkles
        if random.random() < 0.3:
            i = random.randint(0, 23)
            self.ring[i] = self.WHITE
    
    def color_wipe(self):
        """Wipe colors around the ring"""
        pos = int(self.phase) % 24
        self.ring[pos] = self.wheel(int(self.phase * 10) % 255)
        self.phase += 0.5
    
    def dual_spin(self):
        """Two colors spinning in opposite directions"""
        for i in range(24):
            # Forward spinner
            fwd_pos = (i + int(self.phase)) % 24
            # Reverse spinner
            rev_pos = (-i + int(self.phase)) % 24
            
            if i % 2 == 0:
                self.ring[fwd_pos] = self.RED
                self.ring[rev_pos] = self.GREEN
            else:
                self.ring[fwd_pos] = self.GREEN
                self.ring[rev_pos] = self.RED
        
        self.phase += 0.2
    
    def run_show(self):
        """Main show control function"""
        if cp.button_a and cp.button_b:
            self.mode = (self.mode + 1) % 5
            time.sleep(0.2)
        
        # Run current pattern
        if self.mode == 0:
            self.pulse_pattern()
        elif self.mode == 1:
            self.comet_tail()
        elif self.mode == 2:
            self.sparkle_fade()
        elif self.mode == 3:
            self.color_wipe()
        else:
            self.dual_spin()
        
        # Mirror to CPX LEDs for extra effect
        for i in range(10):
            cp.pixels[i] = self.ring[i * 2]

# Create light show
show = LightShow()

# Main loop
while True:
    show.run_show()
    time.sleep(0.01)