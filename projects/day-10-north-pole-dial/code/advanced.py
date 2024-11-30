# Advanced rotary encoder control for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import digitalio
import neopixel
from adafruit_circuitplayground import cp

# Set up encoder pins
clk = digitalio.DigitalInOut(board.A1)
dt = digitalio.DigitalInOut(board.A2)
sw = digitalio.DigitalInOut(board.A3)

clk.direction = digitalio.Direction.INPUT
dt.direction = digitalio.Direction.INPUT
sw.direction = digitalio.Direction.INPUT
sw.pull = digitalio.Pull.UP

# Set up NeoPixel Jewel
jewel = neopixel.NeoPixel(board.A0, 7, brightness=0.3)

def rainbow_cycle(pos):
    """Generate rainbow colors based on position"""
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

class EncoderControl:
    def __init__(self):
        self.position = 0
        self.color_pos = 0
        self.brightness = 0.3
        self.effect_mode = 0
        self.last_update = time.monotonic()
        self.acceleration = 1.0
    
    def update_acceleration(self):
        """Update acceleration based on rotation speed"""
        current_time = time.monotonic()
        time_diff = current_time - self.last_update
        self.acceleration = max(1.0, min(5.0, 0.5 / time_diff))
        self.last_update = current_time
    
    def update(self, direction):
        """Update based on encoder turn"""
        self.update_acceleration()
        step = direction * self.acceleration
        
        if self.effect_mode == 0:  # Color mode
            self.color_pos = (self.color_pos + step) % 255
            return rainbow_cycle(int(self.color_pos))
        else:  # Brightness mode
            self.brightness = max(0.1, min(1.0, 
                self.brightness + step * 0.05))
            return None
    
    def button_press(self):
        """Handle button press"""
        self.effect_mode = (self.effect_mode + 1) % 2
        return self.effect_mode

# Initialize controller
controller = EncoderControl()
last_clk = clk.value

# Main loop
while True:
    # Read encoder
    current_clk = clk.value
    if current_clk != last_clk:
        if dt.value != current_clk:
            direction = 1
        else:
            direction = -1
            
        # Update controller
        color = controller.update(direction)
        if color:
            jewel.fill(color)
        jewel.brightness = controller.brightness
        
        # Also update CP LEDs for feedback
        cp.pixels.fill(color if color else (0, 0, 0))
        cp.pixels.brightness = controller.brightness
    
    # Check button press
    if not sw.value:
        mode = controller.button_press()
        # Flash to indicate mode change
        for _ in range(mode + 1):
            jewel.brightness = 0
            time.sleep(0.1)
            jewel.brightness = controller.brightness
            time.sleep(0.1)
        time.sleep(0.2)  # Debounce
    
    last_clk = current_clk
    time.sleep(0.01)