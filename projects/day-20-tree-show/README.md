# Day 20: Tree Light Show

## Overview
Today we'll create a coordinated light show using multiple LEDs to decorate a tree! We'll combine our experience with different types of LEDs and create synchronized patterns. The younger group will create basic light sequences, while the older group will program complex animations.

## Materials Needed
- Circuit Playground Express
- Regular LEDs (at least 5, various colors)
- Mini Breadboard
- Alligator Clips
- Resistors (220Ω) for each LED
- Tree template or drawing

## Instructions for Age 9

1. Create Your Tree Base:
   - Draw or print a tree outline
   - Mark spots for LEDs
   - Make holes for the LED legs

2. Prepare LEDs:
   - Sort LEDs by color
   - Remember: long leg is positive
   - Each LED needs a resistor

3. Connect First LED:
   - LED positive leg (long) + resistor → A1
   - LED negative leg (short) → GND
   - Test it lights up

4. Add More LEDs:
   - Second LED → A2
   - Third LED → A3
   - Fourth LED → A4
   - Fifth LED → A5
   - Double-check all connections

5. Test Your Display:
   - Press A for pattern 1:
     - LEDs light up in sequence
   - Press B for pattern 2:
     - LEDs twinkle randomly
   - Both buttons for special pattern!

## Instructions for Age 13

1. Hardware Setup:
   - Follow basic assembly steps
   - Plan LED placement for best effect

2. Basic Pattern Code:
```python
import time
import board
import digitalio
from random import randint
from adafruit_circuitplayground import cp

# Set up LED pins
leds = []
led_pins = [board.A1, board.A2, board.A3, board.A4, board.A5]

for pin in led_pins:
    led = digitalio.DigitalInOut(pin)
    led.direction = digitalio.Direction.OUTPUT
    leds.append(led)

def sequence_pattern():
    """Light LEDs in sequence"""
    for led in leds:
        led.value = True
        time.sleep(0.2)
        led.value = False

def twinkle_pattern():
    """Random twinkling effect"""
    for _ in range(10):
        led = leds[randint(0, len(leds)-1)]
        led.value = True
        time.sleep(0.1)
        led.value = False

# Main loop
while True:
    if cp.button_a:
        sequence_pattern()
    elif cp.button_b:
        twinkle_pattern()
    time.sleep(0.1)
```

3. Advanced Patterns:
```python
class TreeLightShow:
    def __init__(self):
        # Initialize LEDs
        self.leds = []
        led_pins = [board.A1, board.A2, board.A3, board.A4, board.A5]
        
        for pin in led_pins:
            led = digitalio.DigitalInOut(pin)
            led.direction = digitalio.Direction.OUTPUT
            self.leds.append(led)
        
        self.pattern_index = 0
        self.last_update = time.monotonic()
    
    def all_off(self):
        """Turn off all LEDs"""
        for led in self.leds:
            led.value = False
    
    def cascade_pattern(self):
        """Cascading light pattern"""
        # Up the tree
        for led in self.leds:
            led.value = True
            time.sleep(0.2)
        time.sleep(0.5)
        
        # Down the tree
        for led in reversed(self.leds):
            led.value = False
            time.sleep(0.2)
    
    def alternating_pattern(self):
        """Alternate even/odd LEDs"""
        # Light even LEDs
        for i in range(0, len(self.leds), 2):
            self.leds[i].value = True
        for i in range(1, len(self.leds), 2):
            self.leds[i].value = False
        time.sleep(0.5)
        
        # Light odd LEDs
        for i in range(0, len(self.leds), 2):
            self.leds[i].value = False
        for i in range(1, len(self.leds), 2):
            self.leds[i].value = True
        time.sleep(0.5)
    
    def wave_pattern(self):
        """Create wave effect"""
        for i in range(len(self.leds)):
            # Light current and adjacent LEDs
            for j in range(max(0, i-1), min(len(self.leds), i+2)):
                self.leds[j].value = True
            time.sleep(0.2)
            self.all_off()
    
    def run_show(self):
        """Run main light show"""
        current_time = time.monotonic()
        
        if cp.button_a:
            self.cascade_pattern()
        elif cp.button_b:
            self.alternating_pattern()
        elif cp.button_a and cp.button_b:
            self.wave_pattern()
        else:
            # Default pattern when no buttons pressed
            if current_time - self.last_update >= 1.0:
                self.pattern_index = (self.pattern_index + 1) % len(self.leds)
                self.all_off()
                self.leds[self.pattern_index].value = True
                self.last_update = current_time
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. LED Not Working?
   - Check LED direction
   - Verify connections
   - Test with different LED
   - Make sure resistor is connected

### For 13-Year-Olds:
1. Pattern Issues?
   - Debug timing
   - Check pin assignments
   - Verify pattern sequence
   - Test individual LEDs

## Extensions

### For 9-Year-Olds:
1. Add more LEDs
2. Create new patterns
3. Change timing
4. Add colored paper effects

### For 13-Year-Olds:
1. Add music synchronization
2. Create custom patterns
3. Add motion triggers
4. Make interactive display

## Safety Notes
- Use resistors with LEDs
- Handle connections carefully
- Mind the LED polarity
- Keep wires organized

## Parent Notes
- Help with LED placement
- Guide resistor selection
- Assist with testing
- Support pattern creation