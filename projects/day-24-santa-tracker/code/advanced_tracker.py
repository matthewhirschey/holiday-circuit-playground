# Advanced Santa Tracker for Circuit Playground Express
# For Henry (Age 13)

import time
import board
import neopixel
from adafruit_rtc import RTC
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull

# Setup hardware
pixels = neopixel.NeoPixel(board.A1, 7, brightness=0.2)
rtc = RTC()

# Setup buttons
button_a = DigitalInOut(board.BUTTON_A)
button_a.direction = Direction.INPUT
button_a.pull = Pull.DOWN

button_b = DigitalInOut(board.BUTTON_B)
button_b.direction = Direction.INPUT
button_b.pull = Pull.DOWN

# Colors and zones
COLORS = {
    'pacific': (0, 0, 255),    # Blue
    'mountain': (0, 255, 0),    # Green
    'central': (255, 255, 0),   # Yellow
    'eastern': (255, 0, 0),     # Red
    'north_pole': (255, 255, 255) # White
}

class SantaTracker:
    def __init__(self):
        self.current_zone = 'north_pole'
        self.brightness = 0.2
        self.show_timezone = False
    
    def update_zone(self, hour):
        if 4 <= hour < 7:
            self.current_zone = 'eastern'
        elif 7 <= hour < 10:
            self.current_zone = 'central'
        elif 10 <= hour < 13:
            self.current_zone = 'mountain'
        elif 13 <= hour < 16:
            self.current_zone = 'pacific'
        else:
            self.current_zone = 'north_pole'
    
    def show_time(self, hours, minutes):
        self.update_zone(hours)
        
        # Clear pixels
        pixels.fill((0, 0, 0))
        
        # Show current zone
        zone_color = COLORS[self.current_zone]
        
        # Create tracking pattern
        for i in range(6):
            if i == (hours % 6):
                pixels[i] = zone_color
            elif i < (hours % 6):
                pixels[i] = tuple(x//4 for x in zone_color)  # Dimmer for passed zones
        
        # Center pixel shows minutes
        if minutes % 2 == 0:
            pixels[6] = zone_color
        
        # Special midnight effect
        if hours == 23 and minutes >= 45:
            self.brightness = min(1.0, self.brightness + 0.01)
            pixels.brightness = self.brightness

tracker = SantaTracker()

while True:
    current = rtc.datetime
    
    # Check buttons
    if button_a.value:  # Toggle timezone display
        tracker.show_timezone = not tracker.show_timezone
        time.sleep(0.2)
    
    if button_b.value:  # Reset brightness
        tracker.brightness = 0.2
        pixels.brightness = tracker.brightness
        time.sleep(0.2)
    
    tracker.show_time(current.tm_hour, current.tm_min)
    time.sleep(0.1)
