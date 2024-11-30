# Day 10: Interactive North Pole Dial

## Overview
Today we'll create an interactive dial that controls holiday lights! Using a rotary encoder (like a digital knob), we'll learn about rotary input while controlling NeoPixels. The younger group will use the dial to change colors and brightness, while the older group will program custom effects.

## Materials Needed
- Circuit Playground Express
- Rotary Encoder + Knob
- Mini Breadboard
- Alligator Clips
- NeoPixel Jewel (from Day 6)
- USB Cable

## Instructions for Age 9

1. Meet Your Rotary Encoder:
   - Look at your encoder - it has 5 pins:
     - CLK (clock)
     - DT (data)
     - SW (switch/button)
     - VCC (power)
     - GND (ground)
   - Turning the knob makes clicking sounds
   - The knob can also be pressed like a button

2. Connect the Encoder:
   - Use alligator clips to connect:
     - VCC to 3.3V on Circuit Playground
     - GND to GND
     - CLK to A1
     - DT to A2
     - SW to A3

3. Connect NeoPixel Jewel:
   - Power to 3.3V
   - Ground to GND
   - Signal to A0

4. Try Your Controls:
   - Turn knob right: Change colors
   - Turn knob left: Change brightness
   - Press knob: Toggle special effects
   - Watch the NeoPixels respond!

## Instructions for Age 13

1. Hardware Setup:
   - Follow basic connection instructions above
   - Create secure mounting for encoder

2. Basic Encoder Programming:
```python
import time
import board
import digitalio
import neopixel

# Set up encoder pins
clk = digitalio.DigitalInOut(board.A1)
dt = digitalio.DigitalInOut(board.A2)
sw = digitalio.DigitalInOut(board.A3)

clk.direction = digitalio.Direction.INPUT
dt.direction = digitalio.Direction.INPUT
sw.direction = digitalio.Direction.INPUT
sw.pull = digitalio.Pull.UP

# Set up NeoPixel Jewel
jewel = neopixel.NeoPixel(board.A0, 7, brightness=0.3)

# Track encoder position
encoder_pos = 0
last_clk = clk.value

# Main loop
while True:
    # Read encoder
    current_clk = clk.value
    if current_clk != last_clk:
        if dt.value != current_clk:
            encoder_pos += 1
        else:
            encoder_pos -= 1
        
        # Update color based on position
        color = (abs(encoder_pos) % 255, 0, 0)
        jewel.fill(color)
    
    last_clk = current_clk
    time.sleep(0.01)
```

3. Advanced Features:
```python
def rainbow_cycle(pos):
    """Generate rainbow colors based on position"""
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

class EncoderControl:
    def __init__(self):
        self.position = 0
        self.color_pos = 0
        self.brightness = 0.3
        self.effect_mode = 0
    
    def update(self, direction):
        """Update based on encoder turn"""
        if self.effect_mode == 0:  # Color mode
            self.color_pos = (self.color_pos + direction) % 255
            return rainbow_cycle(self.color_pos)
        else:  # Brightness mode
            self.brightness = max(0.1, min(1.0, 
                self.brightness + direction * 0.05))
            return None
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. Encoder Not Working?
   - Check all connections
   - Verify pins are secure
   - Try rotating slower
   - Press reset button

### For 13-Year-Olds:
1. Code Issues?
   - Check pin assignments
   - Verify encoder readings
   - Debug position tracking
   - Test with print statements

## Extensions

### For 9-Year-Olds:
1. Create color combinations
2. Try different patterns
3. Add button functions

### For 13-Year-Olds:
1. Add more effect modes
2. Create animations
3. Add sound feedback
4. Implement acceleration

## Safety Notes
- Handle connections carefully
- Don't force the encoder
- Keep track of small parts
- Mind the wire connections

## Parent Notes
- Help with initial setup
- Guide proper handling
- Assist with connections
- Support troubleshooting