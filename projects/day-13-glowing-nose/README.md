# Day 13: Rudolph's Glowing Nose

## Overview
Today we'll create Rudolph's famous glowing nose using a NeoPixel Jewel! We'll combine our previous NeoPixel knowledge with new animation techniques. The younger group will create basic glowing patterns, while the older group will program complex lighting effects.

## Materials Needed
- Circuit Playground Express
- NeoPixel Jewel
- Mini Breadboard
- Alligator Clips
- Cardstock for Rudolph's face
- Decorating supplies

## Instructions for Age 9

1. Create Rudolph's Face:
   - Draw or trace a simple reindeer face on cardstock
   - Cut out a circle for the nose
   - Add other decorations (eyes, antlers)

2. Connect NeoPixel Jewel:
   - Use alligator clips to connect:
     - Power (red wire) to 3.3V
     - Ground (black wire) to GND
     - Data (white wire) to A1

3. Mount the Jewel:
   - Center the NeoPixel Jewel in nose cutout
   - Secure with tape from behind
   - Make sure connections stay solid

4. Test Your Nose:
   - Press button A for steady glow
   - Press button B for twinkling effect
   - Both buttons for special pattern!
   - Watch your nose light up red

## Instructions for Age 13

1. Hardware Setup:
   - Follow basic assembly instructions above
   - Consider adding additional controls

2. Basic Nose Programming:
```python
import time
import board
import neopixel
from adafruit_circuitplayground import cp

# Set up NeoPixel Jewel
jewel = neopixel.NeoPixel(board.A1, 7, brightness=0.3)

# Define colors
RED = (255, 0, 0)
BRIGHT_RED = (255, 50, 50)
DIM_RED = (64, 0, 0)

def steady_glow():
    """Create a steady glowing effect"""
    jewel.fill(RED)

def simple_twinkle():
    """Basic twinkling effect"""
    jewel.fill(BRIGHT_RED)
    time.sleep(0.5)
    jewel.fill(DIM_RED)
    time.sleep(0.5)

# Main loop
while True:
    if cp.button_a:
        steady_glow()
    elif cp.button_b:
        simple_twinkle()
    else:
        jewel.fill((0, 0, 0))
    time.sleep(0.1)
```

3. Advanced Animation:
```python
class GlowingNose:
    def __init__(self):
        self.brightness = 0
        self.increasing = True
        self.speed = 0.05
        self.max_bright = 255
        self.min_bright = 20
    
    def breath_effect(self):
        """Create smooth breathing light effect"""
        if self.increasing:
            self.brightness += 5
            if self.brightness >= self.max_bright:
                self.increasing = False
        else:
            self.brightness -= 5
            if self.brightness <= self.min_bright:
                self.increasing = True
        
        return (self.brightness, 0, 0)
    
    def sparkle_effect(self):
        """Create random sparkle pattern"""
        pixels = [(0, 0, 0)] * 7  # All off
        # Random bright pixel
        bright_pixel = random.randint(0, 6)
        pixels[bright_pixel] = BRIGHT_RED
        return pixels

    def candy_cane_spin(self):
        """Red and white spinning pattern"""
        pixels = []
        for i in range(7):
            if (i + self.phase) % 2 == 0:
                pixels.append((255, 0, 0))  # Red
            else:
                pixels.append((255, 255, 255))  # White
        self.phase = (self.phase + 1) % 2
        return pixels
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. Nose Not Lighting?
   - Check all connections
   - Verify power connection
   - Try resetting board
   - Test different brightness

### For 13-Year-Olds:
1. Animation Issues?
   - Check timing values
   - Verify pixel indexing
   - Debug brightness levels
   - Test color values

## Extensions

### For 9-Year-Olds:
1. Add different colors
2. Try various patterns
3. Make nose respond to light

### For 13-Year-Olds:
1. Create music sync
2. Add motion response
3. Program weather effects
4. Create interactive patterns

## Safety Notes
- Handle connections carefully
- Don't look directly at bright LEDs
- Keep wires organized
- Mind sharp edges

## Parent Notes
- Help with face assembly
- Guide proper connections
- Assist with decoration
- Support troubleshooting