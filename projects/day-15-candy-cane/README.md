# Day 15: Candy Cane Lights

## Overview
Today we'll create a glowing candy cane using diffused NeoPixel LEDs! These special LEDs spread their light to create a softer glow. The younger group will create red and white patterns, while the older group will program complex animations.

## Materials Needed
- Circuit Playground Express
- Diffused NeoPixel Strip (10 LEDs)
- Mini Breadboard
- Alligator Clips
- Candy cane template/outline
- White craft materials

## Instructions for Age 9

1. Create Your Candy Cane:
   - Draw or trace candy cane shape
   - Cut strip channels for LEDs
   - Make space for wires

2. Connect NeoPixel Strip:
   - Find the arrows on the strip (shows direction)
   - Connect to Circuit Playground Express:
     - Power (red wire) to 3.3V
     - Ground (black wire) to GND
     - Data (white wire) to A1

3. Place Your LEDs:
   - Carefully lay strip in channels
   - Make sure arrows point away from board
   - Secure with tape if needed

4. Test Patterns:
   - Press A for red and white stripes
   - Press B for spinning effect
   - Both buttons for twinkling!

## Instructions for Age 13

1. Hardware Setup:
   - Follow basic assembly instructions
   - Consider multiple strips for bigger display

2. Basic Strip Programming:
```python
import time
import board
import neopixel
from adafruit_circuitplayground import cp

# Set up NeoPixel strip
strip = neopixel.NeoPixel(board.A1, 10, brightness=0.3)

# Define colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

def candy_stripe():
    """Create classic candy cane stripes"""
    for i in range(10):
        if i % 2 == 0:
            strip[i] = RED
        else:
            strip[i] = WHITE

def spin_pattern():
    """Make stripes appear to move"""
    for offset in range(10):
        for i in range(10):
            if (i + offset) % 2 == 0:
                strip[i] = RED
            else:
                strip[i] = WHITE
        time.sleep(0.2)

# Main loop
while True:
    if cp.button_a:
        candy_stripe()
    elif cp.button_b:
        spin_pattern()
    else:
        strip.fill(OFF)
    time.sleep(0.1)
```

3. Advanced Animation:
```python
class CandyCane:
    def __init__(self):
        self.strip = neopixel.NeoPixel(board.A1, 10, brightness=0.3)
        self.offset = 0
        self.fade_level = 0
        self.fade_in = True
    
    def smooth_fade(self):
        """Create smooth fading effect"""
        if self.fade_in:
            self.fade_level += 5
            if self.fade_level >= 255:
                self.fade_in = False
        else:
            self.fade_level -= 5
            if self.fade_level <= 50:
                self.fade_in = True
        
        red = (self.fade_level, 0, 0)
        white = (self.fade_level, self.fade_level, self.fade_level)
        return red, white
    
    def sparkle_effect(self):
        """Add random sparkles to pattern"""
        self.strip.fill(OFF)
        for _ in range(3):
            i = random.randint(0, 9)
            self.strip[i] = WHITE
        time.sleep(0.05)
    
    def wave_pattern(self):
        """Create sine wave brightness pattern"""
        for i in range(10):
            brightness = int(((math.sin(self.offset + i/2) + 1) / 2) * 255)
            if i % 2 == 0:
                self.strip[i] = (brightness, 0, 0)  # Red
            else:
                self.strip[i] = (brightness, brightness, brightness)  # White
        self.offset += 0.2
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. LEDs Not Working?
   - Check strip direction
   - Verify connections
   - Test power
   - Look for loose wires

### For 13-Year-Olds:
1. Animation Issues?
   - Check timing values
   - Verify strip length
   - Debug patterns
   - Test brightness levels

## Extensions

### For 9-Year-Olds:
1. Create new patterns
2. Add more strips
3. Try different shapes

### For 13-Year-Olds:
1. Add sound reaction
2. Create pattern sequences
3. Add motion effects
4. Make interactive displays

## Safety Notes
- Handle strips carefully
- Don't pull on wires
- Keep connections secure
- Mind power usage

## Parent Notes
- Help with strip placement
- Guide proper handling
- Assist with connections
- Support creativity