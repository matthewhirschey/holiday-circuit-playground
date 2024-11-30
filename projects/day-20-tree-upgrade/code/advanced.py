# Advanced tree upgrade and train control for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import digitalio
import neopixel
import math
import random
from adafruit_circuitplayground import cp

class HolidayDisplay:
    def __init__(self):
        # Set up tree LEDs
        self.tree_leds = []
        for pin in [board.A1, board.A2, board.A3]:
            led = digitalio.DigitalInOut(pin)
            led.direction = digitalio.Direction.OUTPUT
            self.tree_leds.append(led)
        
        # Set up train
        self.train = neopixel.NeoPixel(board.A4, 16, brightness=0.3)
        self.train_pos = 0
        self.smoke_level = 0
        self.speed = 0.1
        self.stopped = False
        self.station_timer = 0
        
        # Colors
        self.RED = (255, 0, 0)
        self.WHITE = (255, 255, 255)
        self.OFF = (0, 0, 0)
    
    def update_train(self):
        """Update train position and effects"""
        # Check if at station
        if self.stopped:
            if time.monotonic() - self.station_timer > 3:  # 3 second stop
                self.stopped = False
            return
        
        # Clear previous position
        self.train.fill(self.OFF)
        
        # Add train body
        self.train[self.train_pos] = self.RED
        self.train[(self.train_pos + 1) % 16] = self.RED
        self.train[(self.train_pos + 2) % 16] = self.RED
        
        # Add headlight
        self.train[(self.train_pos + 3) % 16] = self.WHITE
        
        # Add smoke effect
        smoke_pos = (self.train_pos - 1) % 16
        smoke_brightness = abs(math.sin(self.smoke_level))
        self.train[smoke_pos] = tuple(int(50 * smoke_brightness) for _ in range(3))
        
        # Update position
        self.train_pos = (self.train_pos + 1) % 16
        self.smoke_level += 0.2
        
        # Random station stops
        if random.random() < 0.05:  # 5% chance to stop
            self.stopped = True
            self.station_timer = time.monotonic()
    
    def tree_pattern(self):
        """Create tree light pattern"""
        # Different patterns based on button press
        if cp.button_a:
            # All on/off together
            state = time.monotonic() % 1 > 0.5
            for led in self.tree_leds:
                led.value = state
        elif cp.button_b:
            # Cascade pattern
            index = int(time.monotonic() * 2) % len(self.tree_leds)
            for i, led in enumerate(self.tree_leds):
                led.value = (i == index)
        else:
            # Random twinkle
            for led in self.tree_leds:
                led.value = random.random() > 0.7
    
    def adjust_speed(self):
        """Adjust train speed based on light level"""
        light = cp.light
        # Slower at night (low light)
        self.speed = max(0.2, min(0.05, light / 1000))
    
    def run_display(self):
        """Main update loop"""
        self.adjust_speed()
        self.update_train()
        self.tree_pattern()
        time.sleep(self.speed)

# Create display controller
display = HolidayDisplay()

# Main loop
while True:
    display.run_display()