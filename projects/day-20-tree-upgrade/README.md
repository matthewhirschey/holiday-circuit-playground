# Day 20: Tree Upgrade and Holiday Train

## Overview
Today we'll upgrade our tree from Day 3 by adding Circuit Playground Express control and a holiday train running around the base! We'll modify our existing circuits, add proper current limiting for the LEDs, and create a moving train effect with a NeoPixel Ring.

## Materials Needed
- Your tree from Day 3
- Circuit Playground Express
- NeoPixel Ring (16 or 24 LEDs)
- 220Ω resistors (one for each LED on tree)
- Mini Breadboard
- Alligator Clips
- Cardboard/paper for train track
- Decorative materials

## Instructions for Age 9

1. Prepare Your Tree:
   - Get your tree from Day 3
   - We'll modify the LED connections
   - Keep the switch in place

2. Add Resistors:
   - One at a time, disconnect each LED from copper tape
   - Add a resistor to the positive leg
   - Reconnect with alligator clips
   - This protects the LEDs!

3. Connect to Circuit Playground:
   - LED 1 to pin A1
   - LED 2 to pin A2
   - LED 3 to pin A3
   - All negative legs to GND

4. Create Train Track:
   - Cut a circle from cardboard
   - Decorate as train track
   - Add snow, trees, etc.

5. Add Train (NeoPixel Ring):
   - Place ring around track
   - Connect power to 3.3V
   - Connect ground to GND
   - Connect data to A4

6. Test Your Display:
   - Tree lights twinkle
   - Train moves around track
   - Switch changes patterns
   - Everything works together!

## Instructions for Age 13

1. Modify Tree Circuits:
   - Follow basic upgrade steps
   - Plan wire routing carefully
   - Consider adding more LEDs

2. Basic Train Code:
```python
import time
import board
import neopixel
from adafruit_circuitplayground import cp

# Set up NeoPixel Ring
train = neopixel.NeoPixel(board.A4, 16, brightness=0.3)

# Train colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

def move_train(position):
    """Create moving train effect"""
    # Clear all pixels
    train.fill(OFF)
    
    # Red for train body (3 pixels)
    train[position] = RED
    train[(position + 1) % 16] = RED
    train[(position + 2) % 16] = RED
    
    # White for headlight
    train[(position + 3) % 16] = WHITE

# Main loop
position = 0
while True:
    move_train(position)
    time.sleep(0.1)
    position = (position + 1) % 16
```

3. Advanced Animation:
```python
class HolidayDisplay:
    def __init__(self):
        # Set up tree LEDs
        self.tree_leds = []
        for pin in [board.A1, board.A2, board.A3]:
            led = digitalio.DigitalInOut(pin)
            led.direction = digitalio.Direction.OUTPUT
            self.tree_leds.append(led)
        
        # Set up train
        self.train = neopixel.NeoPixel(board.A4, 16, brightness=0.3)
        self.train_pos = 0
        self.smoke_level = 0
        self.speed = 0.1
    
    def update_train(self):
        """Update train position and effects"""
        # Clear previous position
        self.train.fill(OFF)
        
        # Add train body
        self.train[self.train_pos] = RED
        self.train[(self.train_pos + 1) % 16] = RED
        self.train[(self.train_pos + 2) % 16] = RED
        
        # Add headlight
        self.train[(self.train_pos + 3) % 16] = WHITE
        
        # Add smoke effect
        smoke_pos = (self.train_pos - 1) % 16
        smoke_brightness = abs(math.sin(self.smoke_level))
        self.train[smoke_pos] = (
            int(50 * smoke_brightness),
            int(50 * smoke_brightness),
            int(50 * smoke_brightness)
        )
        
        # Update position
        self.train_pos = (self.train_pos + 1) % 16
        self.smoke_level += 0.2
    
    def tree_pattern(self):
        """Create tree light pattern"""
        for led in self.tree_leds:
            led.value = random.random() > 0.5
    
    def run_display(self):
        """Main update loop"""
        self.update_train()
        if time.monotonic() % 1 < 0.5:  # Update tree every half second
            self.tree_pattern()
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. LEDs Not Working?
   - Check resistor connections
   - Verify LED direction
   - Test with alligator clips
   - Try different LED

### For 13-Year-Olds:
1. Animation Issues?
   - Debug timing
   - Check array indices
   - Verify loop conditions
   - Test components separately

## Extensions

### For 9-Year-Olds:
1. Add track scenery
2. Change train colors
3. Add sound effects
4. Create station stops

### For 13-Year-Olds:
1. Add speed control
2. Create multiple trains
3. Add light sensors
4. Make interactive stations

## Safety Notes
- Handle modifications carefully
- Mind the LED polarity
- Don't remove necessary parts
- Keep connections secure

## Parent Notes
- Help with circuit changes
- Guide resistor addition
- Support track building
- Assist with testing