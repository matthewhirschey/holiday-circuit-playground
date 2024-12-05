# Advanced rotary encoder control for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import digitalio
import neopixel
from adafruit_circuitplayground import cp
import math

class DialControl:
    def __init__(self):
        # Set up encoder pins
        self.clk = digitalio.DigitalInOut(board.A1)
        self.dt = digitalio.DigitalInOut(board.A2)
        self.sw = digitalio.DigitalInOut(board.A3)
        
        self.clk.direction = digitalio.Direction.INPUT
        self.dt.direction = digitalio.Direction.INPUT
        self.sw.direction = digitalio.Direction.INPUT
        self.sw.pull = digitalio.Pull.UP
        
        # Set up display
        self.display = neopixel.NeoPixel(board.A4, 30, brightness=0.3)
        
        # Track state
        self.last_clk = self.clk.value
        self.position = 0
        self.mode = 0  # 0=color, 1=brightness
        self.brightness = 0.3
        self.last_button = time.monotonic()
        self.animation_phase = 0
    
    def read_encoder(self):
        """Read encoder movement"""
        current_clk = self.clk.value
        if current_clk != self.last_clk:
            if self.dt.value != current_clk:
                direction = 1
            else:
                direction = -1
            self.update_from_encoder(direction)
        self.last_clk = current_clk
    
    def update_from_encoder(self, direction):
        """Handle encoder movement"""
        if self.mode == 0:  # Color mode
            self.position = (self.position + direction) % 255
            self.update_color()
        else:  # Brightness mode
            self.brightness = max(0.1, min(1.0, 
                self.brightness + direction * 0.05))
            self.display.brightness = self.brightness
    
    def check_button(self):
        """Check for button press"""
        if not self.sw.value:
            current = time.monotonic()
            if current - self.last_button > 0.2:  # Debounce
                self.mode = (self.mode + 1) % 2
                self.last_button = current
                return True
        return False
    
    def update_color(self):
        """Update display color based on position"""
        # Create smooth rainbow effect
        r = int((math.sin(self.position / 40.0) + 1.0) * 127)
        g = int((math.sin(self.position / 40.0 + 2.094) + 1.0) * 127)
        b = int((math.sin(self.position / 40.0 + 4.188) + 1.0) * 127)
        self.display.fill((r, g, b))
    
    def run_animation(self):
        """Run animation when button pressed"""
        # Spinning animation
        for i in range(len(self.display)):
            self.display.fill((0, 0, 0))
            self.display[i] = (255, 255, 255)
            time.sleep(0.05)
    
    def update(self):
        """Main update function"""
        self.read_encoder()
        if self.check_button():
            self.run_animation()
            self.update_color()

# Create controller
control = DialControl()

# Main loop
while True:
    control.update()
    time.sleep(0.01)