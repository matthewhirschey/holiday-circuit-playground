# Day 6: Frosty's Glowing Hat

## Overview
Today we'll create a glowing hat using NeoPixel LEDs! We'll build on our Circuit Playground Express experience and learn to use our first breadboard and jumper wires. The younger group will connect and control individual NeoPixels, while the older group will program color patterns and animations.

## Materials Needed
- Circuit Playground Express
- Diffused 8mm NeoPixels (3-5)
- Mini Breadboard
- Jumper Wires (at least 9: 3 each for power, ground, and signal)
- USB Cable

## Instructions for Age 9

1. Meet Your New Tools:
   - Look at your breadboard:
     - Notice the holes are in rows and columns
     - Holes in the same row are connected
     - The + and - rails run along the sides
   - Look at your jumper wires:
     - These fit perfectly in the breadboard holes
     - Different colors help keep track of connections
     - Use red for power (3.3V)
     - Use black for ground (GND)
     - Use other colors for signals

2. Set Up Your Breadboard:
   - Connect power rail:
     - Red jumper wire from 3.3V to red (+) rail
     - Black jumper wire from GND to blue (-) rail
   - Place first NeoPixel on breadboard
   - Notice it has 3 connections:
     - Power (marked +)
     - Ground (marked -)
     - Signal (marked IN or DIN)

3. Connect First NeoPixel:
   - Connect to power rail:
     - Red jumper from + rail to NeoPixel +
     - Black jumper from - rail to NeoPixel -
   - Connect signal:
     - Colored jumper from A1 to NeoPixel IN

4. Test Your NeoPixel:
   - Plug in your Circuit Playground Express
   - Press button A to change colors
   - Press button B to make it brighter/dimmer

5. Add More NeoPixels:
   - Place additional NeoPixels on breadboard
   - Connect power and ground to rails
   - Connect signals to different pins (A2, A3)

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
   - Check jumper wire connections in breadboard
   - Make sure wires are fully inserted
   - Verify power rail connections
   - Try moving NeoPixel to different rows

### For 13-Year-Olds:
1. Circuit Issues?
   - Test power rails with multimeter if available
   - Verify all ground connections
   - Check signal wire routing
   - Test each connection point

2. Code Issues?
   [Rest remains the same...]

## Breadboard Tips

1. Understanding Connections:
   - Holes in same row are connected
   - Rails run the full length
   - Center gap breaks connections
   - Keep wires neat and organized

2. Good Practices:
   - Use red wires for power
   - Use black wires for ground
   - Different colors for signals
   - Keep wires short and tidy

## Safety Notes
- Insert wires and components straight and gentle
- Don't force connections
- Handle breadboard carefully
- Keep track of wire colors

## Parent Notes
- Help understand breadboard layout
- Guide wire color coding
- Assist with first connections
- Support troubleshooting
