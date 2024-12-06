# Day 6: Frosty's Glowing Hat

## Overview
Today we'll create a glowing hat using NeoPixel LEDs! We'll build on our Circuit Playground Express experience and learn to use our first breadboard and jumper wires. The younger group will connect and control individual NeoPixels, while the older group will program color patterns and animations.

## Materials Needed
- Circuit Playground Express
- Diffused 8mm NeoPixels (3-5)
- Mini Breadboard
- Jumper Wires (at least 9: 3 each for power, ground, and signal)
- USB Cable
- Computer with web browser for MakeCode

## Instructions for Age 9

### 1. Meet Your New Tools
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

### 2. Set Up Your Breadboard
- Connect power rail:
  - Red jumper wire from 3.3V to red (+) rail
  - Black jumper wire from GND to blue (-) rail
- Place first NeoPixel on breadboard
- Notice it has 3 connections:
  - Power (marked +)
  - Ground (marked -)
  - Signal (marked IN or DIN)

### 3. Connect First NeoPixel
- Connect to power rail:
  - Red jumper from + rail to NeoPixel +
  - Black jumper from - rail to NeoPixel -
- Connect signal:
  - Colored jumper from A1 to NeoPixel IN

### 4. Program Your First NeoPixel
1. Set Up MakeCode:
   - Go to makecode.adafruit.com in your web browser
   - Click "New Project"
   - Click on "Advanced" in the toolbox
   - Click on "Extensions" at the bottom
   - Click on the "LIGHT" extension to add it

2. Create Your First Program:
   ```
   In "on start":
   1. Find "set pixel color" in LIGHT
   2. Set it to pin A1
   3. Choose any color
   4. Add "show" block after it
   ```

3. Make It Interactive:
   ```
   Add these blocks:
   
   "on button A click":
   1. "set pixel color" (pin A1)
   2. Choose a different color
   3. Add "show" block
   
   "on button B click":
   1. "set pixel color" (pin A1)
   2. Choose another color
   3. Add "show" block
   ```

4. Add Some Animation:
   ```
   In "forever" loop:
   1. "set pixel color" (pin A1)
   2. Choose a color
   3. Add "show" block
   4. Add "pause 500 ms"
   5. "set pixel color" (pin A1)
   6. Choose different color
   7. Add "show" block
   8. Add "pause 500 ms"
   ```

### 5. Test Your NeoPixel
- Download your code to the Circuit Playground
- The NeoPixel should light up with your first color
- Press button A to change to second color
- Press button B to change to third color
- Watch it animate in the forever loop

### 6. Add More NeoPixels
- Place additional NeoPixels on breadboard
- Connect power and ground to rails
- Connect signals to different pins (A2, A3)

### 7. Program Multiple NeoPixels
1. Basic Multiple NeoPixel Program:
   ```
   In "forever" loop:
   1. "set pixel color" (pin A1) to red
   2. "set pixel color" (pin A2) to blue
   3. "set pixel color" (pin A3) to green
   4. Add "show" block
   5. Add "pause 500 ms"
   6. Change colors
   7. Add "show" block
   8. Add "pause 500 ms"
   ```

2. Create a Chase Pattern:
   ```
   In "forever" loop:
   1. Set first pixel to red, others off
   2. Show and pause
   3. Set second pixel to red, others off
   4. Show and pause
   5. Set third pixel to red, others off
   6. Show and pause
   ```

## Troubleshooting for 9-Year-Olds

### NeoPixel Not Lighting Up?
1. Check Your Connections:
   - Are all jumper wires fully inserted?
   - Is the power rail connected properly?
   - Is the NeoPixel in the right direction?
   - Try moving NeoPixel to different rows

2. Check Your Code:
   - Did you add the LIGHT extension?
   - Is the pin number correct (A1, A2, or A3)?
   - Did you add "show" block after color changes?
   - Try downloading the code again

3. Power Issues:
   - If NeoPixels are dim or flickering:
     - Verify 3.3V connection
     - Try reducing brightness in MakeCode
     - Check all ground connections
   - If colors look wrong:
     - Double-check signal wire connection
     - Verify pin numbers in code
     - Try unplugging and reconnecting USB

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
- Insert wires and components carefully and straight
- Don't force connections
- Handle breadboard gently
- Keep track of wire colors
- Ask for help if something doesn't look right

## Parent Notes
- Help understand breadboard connections
- Guide wire color coding
- Assist with first MakeCode program
- Support troubleshooting
- Encourage experimentation with colors and patterns
- Help with understanding timing in animations
