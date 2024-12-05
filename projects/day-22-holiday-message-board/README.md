# Day 20: Holiday Message Board

## Overview
Transform your 1.3" OLED display into a festive message board! This project creates an interactive display that can show scrolling holiday messages, custom icons, and animated text. Perfect for spreading holiday cheer or leaving fun messages for family members.

## Materials Needed
- Circuit Playground Express
- 1.3" 128x64 OLED Display (Adafruit #938)
- STEMMA QT / Qwiic JST SH Cable
- Mini Breadboard (optional)
- Jumper Wires (if not using STEMMA QT)
- USB Cable for programming

## Setup

### For 9-Year-Olds
1. Connect Display:
   - Plug one end of STEMMA QT cable into OLED display
   - Connect other end to Circuit Playground Express
   - Display should light up when powered!

2. Basic Display Test:
   - Upload test code to see the display working
   - Try different messages
   - Learn about text size and position

3. Create Message List:
   - Think of fun holiday messages
   - Keep them short enough to fit
   - Include some holiday emojis

### For 13-Year-Olds
1. Advanced Setup:
   - Configure I2C connection
   - Set up multiple font options
   - Create custom holiday icons
   - Plan message animations

2. Basic Message Board Code:
```python
import board
import displayio
import terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label

# Release any resources currently in use for the displays
displayio.release_displays()

# Set up I2C
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

# Set up the display (128x64 pixels)
WIDTH = 128
HEIGHT = 64
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

# Create the display context
main_group = displayio.Group()
display.show(main_group)

# List of holiday messages
messages = [
    "Happy Holidays!",
    "Joy to the World",
    "Let it Snow!",
    "Season's Greetings",
    "Be Merry & Bright"
]

# Basic text display function
def show_message(message, size=1):
    # Create a text label
    text_area = label.Label(
        terminalio.FONT,
        text=message,
        color=0xFFFFFF,
        x=0,
        y=HEIGHT//2
    )
    
    # Scale the text
    text_area.scale = size
    
    # Clear the display
    while len(main_group) > 0:
        main_group.pop()
        
    # Add the text
    main_group.append(text_area)

# Button handler for Circuit Playground Express
from adafruit_circuitplayground import cp
current_message = 0

while True:
    if cp.button_a:
        current_message = (current_message + 1) % len(messages)
        show_message(messages[current_message])
        while cp.button_a:
            pass  # Wait for button release
```

3. Advanced Features:
```python
import time
import math

class HolidayMessageBoard:
    def __init__(self):
        # Initialize display setup (as above)
        self.scroll_pos = 0
        self.current_message = 0
        self.animation_frame = 0
        
    def scroll_text(self, message):
        """Scroll text across the display"""
        text_area = label.Label(
            terminalio.FONT,
            text=message,
            color=0xFFFFFF,
            x=WIDTH - self.scroll_pos,
            y=HEIGHT//2
        )
        
        while len(main_group) > 0:
            main_group.pop()
            
        main_group.append(text_area)
        self.scroll_pos = (self.scroll_pos + 2) % (WIDTH + text_area.width)
        
    def add_holiday_icon(self, icon_type):
        """Add holiday icons to display"""
        # Icon coordinates for different holiday symbols
        icons = {
            'tree': [(64, 10), (60, 15), (68, 15), (56, 20), 
                    (72, 20), (64, 5)],
            'star': [(64, 5), (60, 15), (50, 15), (58, 20),
                    (55, 30), (64, 25), (73, 30), (70, 20),
                    (78, 15), (68, 15)],
            'gift': [(60, 40), (68, 40), (64, 35), (64, 45)]
        }
        
        if icon_type in icons:
            # Create bitmap for icon
            bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
            for x, y in icons[icon_type]:
                bitmap[x, y] = 1
            
            # Create palette
            palette = displayio.Palette(2)
            palette[0] = 0x000000
            palette[1] = 0xFFFFFF
            
            # Create TileGrid
            icon_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
            main_group.append(icon_grid)
    
    def animate_snow(self):
        """Add animated snowflakes"""
        snow_points = [(x, (y + self.animation_frame) % HEIGHT) 
                      for x, y in [(20, 10), (40, 30), (80, 15), 
                                 (100, 25), (60, 40)]]
        
        bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
        for x, y in snow_points:
            bitmap[x, y] = 1
        
        palette = displayio.Palette(2)
        palette[0] = 0x000000
        palette[1] = 0xFFFFFF
        
        snow_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
        main_group.append(snow_grid)
        self.animation_frame = (self.animation_frame + 1) % HEIGHT
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. Display Issues?
   - Check cable connections
   - Make sure display is getting power
   - Try resetting the board
   - Verify message length fits screen

### For 13-Year-Olds:
1. Code Problems?
   - Check I2C address
   - Verify display initialization
   - Test different fonts
   - Debug animation timing

## Extension Ideas

### For 9-Year-Olds:
1. Create themed message sets
   - Christmas messages
   - New Year countdown
   - Winter wonderland themes
   - Thank you notes

### For 13-Year-Olds:
1. Add advanced features
   - Multiple animations
   - Custom character sets
   - Interactive games
   - Temperature display integration

## Message Design Tips

1. Text Layout:
   - Keep messages readable
   - Use appropriate font sizes
   - Consider screen space
   - Plan message timing

2. Animations:
   - Smooth scrolling
   - Consistent timing
   - Clear transitions
   - Engaging effects

## Safety Notes
- Handle display carefully
- Protect from static
- Secure connections
- Monitor power usage

## Parent Notes
- Help with message ideas
- Guide font selection
- Assist with timing
- Support creativity