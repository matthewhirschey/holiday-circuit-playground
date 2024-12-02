# Basic Santa Tracker for Circuit Playground Express
# For Grace (Age 9)

import time
import board
import neopixel
from adafruit_rtc import RTC

# Setup NeoPixel Jewel
pixels = neopixel.NeoPixel(board.A1, 7, brightness=0.2)

# Setup RTC
rtc = RTC()

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

def show_time(hours, minutes):
    # Clear all pixels
    pixels.fill(OFF)
    
    # Show hours (red)
    hour_pixel = (hours % 12) // 2  # Map 24 hours to 6 pixels
    pixels[hour_pixel] = RED
    
    # Show minutes (blue)
    minute_pixel = (minutes // 10)  # Map 60 minutes to 6 pixels
    if minute_pixel != hour_pixel:
        pixels[minute_pixel] = BLUE
    
    # Center pixel shows every minute
    if minutes % 2 == 0:
        pixels[6] = WHITE
    else:
        pixels[6] = OFF

while True:
    current = rtc.datetime
    show_time(current.tm_hour, current.tm_min)
    time.sleep(1)
