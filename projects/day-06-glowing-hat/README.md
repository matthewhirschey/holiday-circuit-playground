# Day 6: Frosty's Glowing Hat

## Overview
Today we'll create a glowing hat using NeoPixel LEDs! We'll build on our Circuit Playground Express experience, introducing colorful, controllable lights. The younger group will connect and control individual NeoPixels, while the older group will program color patterns and animations.

## Materials Needed
- Circuit Playground Express
- Diffused 8mm NeoPixels (3-5)
- Mini Breadboard
- Alligator Clips
- USB Cable

## Instructions for Age 9

1. Set Up Your Breadboard:
   - Place your NeoPixels on the breadboard
   - Notice each NeoPixel has 3 connections:
     - Power (marked +)
     - Ground (marked -)
     - Signal (marked IN or DIN)

2. Connect First NeoPixel:
   - Use alligator clips to connect:
     - NeoPixel + to 3.3V on Circuit Playground
     - NeoPixel - to GND
     - NeoPixel IN to pin A1

3. Test Your NeoPixel:
   - Plug in your Circuit Playground Express
   - Press button A to change colors
   - Press button B to make it brighter/dimmer

4. Add More NeoPixels:
   - Place additional NeoPixels on breadboard
   - Connect power (+) and ground (-) same as first
   - The signal line can connect to different pins (A2, A3)

5. Create Your Hat Display:
   - Arrange NeoPixels in a pattern
   - Test each one with the buttons
   - Watch them light up in different colors!

## Instructions for Age 13

1. Hardware Setup:
   - Follow steps 1-2 from basic instructions
   - Connect multiple NeoPixels to different pins

2. Basic NeoPixel Programming:
```python
import time
import board
import neopixel
from adafruit_circuitplayground import cp

# Set up NeoPixels on pins A1, A2, A3
pixel1 = neopixel.NeoPixel(board.A1, 1, brightness=0.3)
pixel2 = neopixel.NeoPixel(board.A2, 1, brightness=0.3)
pixel3 = neopixel.NeoPixel(board.A3, 1, brightness=0.3)

# Define some colors
COLORS = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Purple
    (0, 255, 255),  # Cyan
    (255, 255, 255) # White
]

def color_chase():
    """Move through colors one at a time"""
    for color in COLORS:
        pixel1.fill(color)
        time.sleep(0.5)
        pixel2.fill(color)
        time.sleep(0.5)
        pixel3.fill(color)
        time.sleep(0.5)
        
# Main loop
while True:
    if cp.button_a:
        color_chase()
    elif cp.button_b:
        # Rainbow cycle
        for i in range(len(COLORS)):
            pixel1.fill(COLORS[i])
            pixel2.fill(COLORS[(i+1) % len(COLORS)])
            pixel3.fill(COLORS[(i+2) % len(COLORS)])
            time.sleep(0.5)
```

3. Advanced Animation:
```python
def rainbow_fade(speed=0.02):
    """Create smooth rainbow fade effect"""
    for i in range(255):
        r = (i * 3) % 255
        g = (i * 7) % 255
        b = (i * 11) % 255
        pixel1.fill((r, g, b))
        pixel2.fill((g, b, r))
        pixel3.fill((b, r, g))
        time.sleep(speed)
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. NeoPixel Not Lighting?
   - Check all three connections
   - Verify power connection (3.3V)
   - Make sure ground is connected
   - Try a different pin

### For 13-Year-Olds:
1. Code Issues?
   - Check pin assignments
   - Verify color values (0-255)
   - Test with simple colors first
   - Print debug messages

## Extensions

### For 9-Year-Olds:
1. Try different arrangements
2. Add more NeoPixels
3. Create patterns with buttons

### For 13-Year-Olds:
1. Create new color patterns
2. Add motion detection
3. Sync with music
4. Make interactive games

## Safety Notes
- Handle connections carefully
- Don't look directly at bright LEDs
- Keep track of wiring
- Adult supervision for connections

## Parent Notes
- Help with breadboard setup
- Guide proper connections
- Monitor brightness levels
- Assist with troubleshooting