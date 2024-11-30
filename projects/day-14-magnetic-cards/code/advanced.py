# Advanced magnetic card control for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import digitalio
import neopixel
import random
from adafruit_circuitplayground import cp

class MagneticCard:
    def __init__(self):
        # Set up reed switch
        self.switch = digitalio.DigitalInOut(board.A1)
        self.switch.direction = digitalio.Direction.INPUT
        self.switch.pull = digitalio.Pull.UP
        
        # Set up NeoPixels
        self.pixels = neopixel.NeoPixel(board.A2, 8, brightness=0.3)
        
        # Track state
        self.open_time = 0
        self.animation_phase = 0
        self.is_open = False
        self.current_animation = 0
    
    def check_state(self):
        """Check if card state has changed"""
        current_state = not self.switch.value
        if current_state != self.is_open:
            self.is_open = current_state
            if self.is_open:
                self.open_time = time.monotonic()
                return True
        return False
    
    def wheel(self, pos):
        """Color wheel for rainbow effect"""
        if pos < 85:
            return (pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return (255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return (0, pos * 3, 255 - pos * 3)
    
    def rainbow_welcome(self):
        """Create rainbow effect when card opens"""
        for i in range(8):
            pixel_hue = (i * 32 + self.animation_phase) % 256
            self.pixels[i] = self.wheel(pixel_hue)
        self.animation_phase = (self.animation_phase + 1) % 256
    
    def sparkle_effect(self):
        """Create random sparkle pattern"""
        self.pixels.fill((0, 0, 0))
        for _ in range(3):
            i = random.randint(0, 7)
            self.pixels[i] = (255, 255, 255)
        time.sleep(0.05)
    
    def wave_effect(self):
        """Create wave of light"""
        for i in range(8):
            self.pixels.fill((0, 0, 0))
            self.pixels[i] = (255, 255, 255)
            time.sleep(0.1)
    
    def run_animation(self):
        """Run current animation pattern"""
        if self.current_animation == 0:
            self.rainbow_welcome()
        elif self.current_animation == 1:
            self.sparkle_effect()
        else:
            self.wave_effect()

# Create card controller
card = MagneticCard()

# Main loop
while True:
    if card.check_state():  # Card state changed
        if card.is_open:
            # Change animation when opened
            card.current_animation = (card.current_animation + 1) % 3
            # Play tone on Circuit Playground
            cp.play_tone(440, 0.1)
    
    if card.is_open:
        card.run_animation()
    else:
        card.pixels.fill((0, 0, 0))
    
    time.sleep(0.01)