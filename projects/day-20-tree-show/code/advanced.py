# Advanced LED tree show for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import digitalio
from random import randint
from adafruit_circuitplayground import cp

class TreeLightShow:
    def __init__(self):
        # Initialize LEDs
        self.leds = []
        led_pins = [board.A1, board.A2, board.A3, board.A4, board.A5]
        
        for pin in led_pins:
            led = digitalio.DigitalInOut(pin)
            led.direction = digitalio.Direction.OUTPUT
            self.leds.append(led)
        
        self.pattern_index = 0
        self.last_update = time.monotonic()
    
    def all_off(self):
        """Turn off all LEDs"""
        for led in self.leds:
            led.value = False
    
    def all_on(self):
        """Turn on all LEDs"""
        for led in self.leds:
            led.value = True
    
    def cascade_pattern(self):
        """Cascading light pattern"""
        # Up the tree
        for led in self.leds:
            led.value = True
            time.sleep(0.2)
        time.sleep(0.5)
        
        # Down the tree
        for led in reversed(self.leds):
            led.value = False
            time.sleep(0.2)
    
    def alternating_pattern(self):
        """Alternate even/odd LEDs"""
        # Light even LEDs
        for i in range(0, len(self.leds), 2):
            self.leds[i].value = True
        for i in range(1, len(self.leds), 2):
            self.leds[i].value = False
        time.sleep(0.5)
        
        # Light odd LEDs
        for i in range(0, len(self.leds), 2):
            self.leds[i].value = False
        for i in range(1, len(self.leds), 2):
            self.leds[i].value = True
        time.sleep(0.5)
    
    def wave_pattern(self):
        """Create wave effect"""
        for i in range(len(self.leds)):
            # Light current and adjacent LEDs
            for j in range(max(0, i-1), min(len(self.leds), i+2)):
                self.leds[j].value = True
            time.sleep(0.2)
            self.all_off()
    
    def sparkle_pattern(self):
        """Random sparkle effect"""
        for _ in range(20):
            # Pick random LED
            led = self.leds[randint(0, len(self.leds)-1)]
            led.value = True
            time.sleep(0.1)
            led.value = False
    
    def run_show(self):
        """Run main light show"""
        current_time = time.monotonic()
        
        if cp.button_a:
            self.cascade_pattern()
        elif cp.button_b:
            self.alternating_pattern()
        elif cp.button_a and cp.button_b:
            self.wave_pattern()
        else:
            # Default pattern - moving dot
            if current_time - self.last_update >= 1.0:
                self.pattern_index = (self.pattern_index + 1) % len(self.leds)
                self.all_off()
                self.leds[self.pattern_index].value = True
                self.last_update = current_time

# Create light show controller
show = TreeLightShow()

# Main loop
while True:
    show.run_show()
    time.sleep(0.01)