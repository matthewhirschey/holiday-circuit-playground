# Advanced magnetic card control for Circuit Playground Express
# Designed for 13-year-old level - works with either connection method

import time
import board
import digitalio
import neopixel
from adafruit_circuitplayground import cp

class MagicCard:
    def __init__(self):
        # Set up magnetic switch
        self.switch = digitalio.DigitalInOut(board.A1)
        self.switch.direction = digitalio.Direction.INPUT
        self.switch.pull = digitalio.Pull.UP
        
        # Set up optional NeoPixel strip
        self.pixels = neopixel.NeoPixel(board.A2, 8, brightness=0.3)
        
        # Track state
        self.is_open = False
        self.last_state = False
        self.open_time = 0
        self.animation_phase = 0
    
    def check_card(self):
        """Check if card state has changed"""
        self.is_open = not self.switch.value
        if self.is_open != self.last_state:
            if self.is_open:
                self.card_opened()
            else:
                self.card_closed()
            self.last_state = self.is_open
    
    def card_opened(self):
        """Handle card opening"""
        self.open_time = time.monotonic()
        # Play opening sound
        cp.play_tone(523, 0.1)  # C5
        time.sleep(0.1)
        cp.play_tone(659, 0.1)  # E5
        
    def card_closed(self):
        """Handle card closing"""
        # Play closing sound
        cp.play_tone(659, 0.1)  # E5
        time.sleep(0.1)
        cp.play_tone(523, 0.1)  # C5
    
    def run_light_show(self):
        """Update lights based on card state"""
        if self.is_open:
            # Calculate time open
            open_duration = time.monotonic() - self.open_time
            
            # Different patterns based on how long open
            if open_duration < 5:  # First 5 seconds
                self.sparkle_pattern()
            else:  # After 5 seconds
                self.rainbow_pattern()
        else:
            # Everything off when closed
            self.pixels.fill((0, 0, 0))
            cp.pixels.fill((0, 0, 0))
    
    def sparkle_pattern(self):
        """Create sparkling effect"""
        # Random twinkling
        for i in range(len(self.pixels)):
            if random.random() > 0.7:
                self.pixels[i] = (255, 255, 255)
            else:
                self.pixels[i] = (0, 0, 0)
        # Also animate CPX LEDs
        for i in range(10):
            if random.random() > 0.7:
                cp.pixels[i] = (255, 255, 255)
            else:
                cp.pixels[i] = (0, 0, 0)
    
    def rainbow_pattern(self):
        """Create moving rainbow effect"""
        self.animation_phase += 0.1
        for i in range(len(self.pixels)):
            # Create rainbow colors
            r = int((math.sin(self.animation_phase + i/2) + 1) * 127)
            g = int((math.sin(self.animation_phase + i/2 + 2) + 1) * 127)
            b = int((math.sin(self.animation_phase + i/2 + 4) + 1) * 127)
            self.pixels[i] = (r, g, b)
        # Similar effect on CPX LEDs
        for i in range(10):
            r = int((math.sin(self.animation_phase + i/3) + 1) * 127)
            g = int((math.sin(self.animation_phase + i/3 + 2) + 1) * 127)
            b = int((math.sin(self.animation_phase + i/3 + 4) + 1) * 127)
            cp.pixels[i] = (r, g, b)

# Create card controller
card = MagicCard()

# Main loop
while True:
    card.check_card()
    card.run_light_show()
    time.sleep(0.01)