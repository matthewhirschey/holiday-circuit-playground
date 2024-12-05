# Day 9: Interactive North Pole Dial

## Overview
Today we'll create a rotary control interface using an encoder - like a digital knob for our projects! We'll use the encoder to control lights and make interactive displays. The younger group will learn about rotary input, while the older group will program complex control patterns.

## Materials Needed
- Circuit Playground Express
- Rotary Encoder with Pushbutton
- Mini Breadboard (from previous days)
- Jumper Wires (at least 5: power, ground, and 3 signals)
- NeoPixel Strip or Jewel (optional for display)

## Instructions for Age 9

1. Understand Your Rotary Encoder:
   - Look at the encoder pins:
     - CLK (Pin A) - First signal pin
     - DT (Pin B) - Second signal pin
     - SW - Button signal pin
     - GND - Ground connection
     - + - Power connection (if present)
   - Notice how it clicks when you turn it
   - Try pressing the button on top

2. Set Up Breadboard:
   - Power rails (like previous days):
     - Red jumper wire from 3.3V to red (+) rail
     - Black jumper wire from GND to blue (-) rail

3. Connect Encoder:
   - Place encoder in breadboard
   - Connect power:
     - GND pin to - rail
     - + pin to + rail (if present)
   - Connect signals:
     - CLK (Pin A) to A1 using jumper wire
     - DT (Pin B) to A2 using jumper wire
     - SW (button) to A3 using jumper wire

4. Add Display (Optional):
   - Connect NeoPixel:
     - Power to + rail
     - Ground to - rail
     - Signal to A4

5. Test Your Control:
   - Turn knob right: Change colors
   - Turn knob left: Change brightness
   - Press knob: Special effect!

## Instructions for Age 13

1. Hardware Setup:
   - Follow basic connection steps
   - Ensure encoder is stable in breadboard
   - Consider clean wire routing

2. Basic Encoder Code:
```python
import time
import board
import digitalio

# Set up encoder pins
clk = digitalio.DigitalInOut(board.A1)
dt = digitalio.DigitalInOut(board.A2)
sw = digitalio.DigitalInOut(board.A3)

clk.direction = digitalio.Direction.INPUT
dt.direction = digitalio.Direction.INPUT
sw.direction = digitalio.Direction.INPUT
sw.pull = digitalio.Pull.UP

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
        print(f"Position: {encoder_pos}")
    last_clk = current_clk
    
    # Check button
    if not sw.value:
        print("Button pressed!")
        time.sleep(0.2)  # Debounce
    
    time.sleep(0.01)
```

3. Advanced Features:
```python
class DialControl:
    def __init__(self):
        # Track state
        self.position = 0
        self.mode = 0
        self.brightness = 0.3
        self.last_button = time.monotonic()
        
    def update_from_encoder(self, direction):
        """Handle encoder movement"""
        if self.mode == 0:  # Color mode
            self.position = (self.position + direction) % 255
        else:  # Brightness mode
            self.brightness = max(0.1, min(1.0, 
                self.brightness + direction * 0.05))
    
    def handle_button(self):
        """Handle button press"""
        current = time.monotonic()
        if current - self.last_button > 0.2:  # Debounce
            self.mode = (self.mode + 1) % 2
            self.last_button = current
            return True
        return False
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. Encoder Not Working?
   - Check all wire connections
   - Verify power connections
   - Make sure encoder is fully inserted
   - Try turning slower

### For 13-Year-Olds:
1. Code Issues?
   - Debug encoder readings
   - Check pin assignments
   - Verify state tracking
   - Test button debouncing

## Tips for Success
1. Understanding Rotation:
   - Clockwise usually increases values
   - Counter-clockwise decreases
   - Button press can switch modes

2. Clean Code:
   - Track last position
   - Debounce button presses
   - Use modes for different controls

## Safety Notes
- Handle encoder gently
- Don't force connections
- Keep wires organized
- Mind the polarity

## Parent Notes
- Help with initial wiring
- Guide encoder usage
- Assist with testing
- Support exploration
