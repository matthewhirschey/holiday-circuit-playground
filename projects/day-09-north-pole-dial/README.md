# Day 9: Interactive North Pole Dial

## Project Overview
Transform your Circuit Playground Express into an interactive control station using a rotary encoder! Create a digital North Pole command center that can control lights, animations, and special effects.

**Difficulty**: ⭐⭐⭐ (Intermediate)  
**Duration**: 45-60 minutes  
**Project Type**: 🎮 Interactive Control

## What You'll Learn
- How mechanical rotary encoders work
- Reading and processing multiple input signals
- Creating interactive control interfaces
- Basic state management in code
- Working with hardware interrupts (Age 13)

## Required Materials
- Circuit Playground Express
- PEC11 Rotary Encoder (Adafruit PID: 377)
- Mini Breadboard
- 4x Jumper Wires (male-to-male)
- USB Cable for programming

## Hardware Overview
A rotary encoder is a mechanical device that creates digital signals by making and breaking connections as you turn it. The PEC11 encoder has:

- Channel A: Left pin on 3-pin side, connects to ground in a pattern as you turn
- Common (Ground): Middle pin on 3-pin side
- Channel B: Right pin on 3-pin side, connects to ground in a pattern as you turn
- Switch: 2 pins on opposite side that connect when pressed

Key differences from other rotary devices:
- No power needed - it's purely mechanical
- Can turn continuously without stops
- Makes clicking sounds as you turn
- Includes a pushbutton that clicks when pressed

## Safety First! ⚡
- Always disconnect power before making connections
- Handle the encoder gently - the pins can bend
- Keep workspace clean and organized
- Double-check ground connections
- Adult supervision recommended for initial setup

## Instructions for Age 9

### 1. Understanding Your Encoder
Before we start building, let's understand how our mechanical knob works:
- The encoder has pins on two sides (3 pins and 2 pins)
- Turning right makes clicking sounds - we'll use these for increasing values
- Turning left also clicks - we'll use these for decreasing values
- The button on top can be pressed to change modes
- Inside are tiny switches that connect and disconnect as you turn

### 2. Building the Circuit
1. Ground Setup
   - Connect a black jumper wire from Circuit Playground GND to breadboard's blue (-) rail
   - This provides ground for both the turning and button functions

2. Encoder Connection
   - Place encoder in breadboard, straddling the center gap
   - On the 3-pin side (left to right):
     * Connect left pin (Channel A) to Circuit Playground A1
     * Connect middle pin (Ground) to blue (-) rail
     * Connect right pin (Channel B) to Circuit Playground A2
   - On the 2-pin side:
     * Connect one switch pin to Circuit Playground A3
     * Connect other switch pin to blue (-) rail

### 3. Basic Operation
- Turn right = Next color
- Turn left = Previous color
- Press button = Change brightness mode
- In brightness mode: right = brighter, left = dimmer

## Instructions for Age 13

### 1. Advanced Hardware Setup
"""
North Pole Dial - Day 9 Project
For Circuit Playground Express with PEC11 Rotary Encoder

Connections:
- Channel A (left pin of 3) -> A1
- Common (middle pin) -> GND
- Channel B (right pin) -> A2
- Switch (either pin) -> A3
- Switch (other pin) -> GND
"""
```
import time
import board
import digitalio
from adafruit_circuitplayground import cp

class RotaryEncoder:
    def __init__(self, clk_pin, dt_pin, sw_pin):
        # Set up encoder pins
        self.clk = digitalio.DigitalInOut(clk_pin)  # Channel A
        self.dt = digitalio.DigitalInOut(dt_pin)    # Channel B
        self.sw = digitalio.DigitalInOut(sw_pin)    # Push Button
        
        # Configure all pins as inputs
        self.clk.direction = digitalio.Direction.INPUT
        self.dt.direction = digitalio.Direction.INPUT
        self.sw.direction = digitalio.Direction.INPUT
        
        # Enable pull-up resistor on button
        # This makes the button read False when pressed
        self.sw.pull = digitalio.Pull.UP
        
        # Remember last state for rotation detection
        self.last_clk = self.clk.value
        self.last_button_time = time.monotonic()  # For debouncing
    
    def read_encoder(self):
        """
        Read encoder rotation. Returns:
         1 for clockwise
        -1 for counter-clockwise
         0 for no movement
        """
        # No change since last read
        if self.clk.value == self.last_clk:
            return 0
            
        # Save the new state
        self.last_clk = self.clk.value
        
        # Check rotation direction
        if self.dt.value != self.clk.value:
            return 1  # Clockwise
        else:
            return -1  # Counter-clockwise
    
    def button_pressed(self):
        """Check if button is pressed, with debouncing"""
        if not self.sw.value:  # Button is pressed (reads False when pressed)
            current_time = time.monotonic()
            # Check if enough time has passed since last press
            if current_time - self.last_button_time > 0.2:
                self.last_button_time = current_time
                return True
        return False

# Set up the NeoPixels
cp.pixels.brightness = 0.3
cp.pixels.fill((0, 0, 0))

# Create our encoder
encoder = RotaryEncoder(
    clk_pin=board.A1,  # Channel A
    dt_pin=board.A2,   # Channel B
    sw_pin=board.A3    # Push Button
)

# Variables for tracking state
mode = 0        # 0 = color mode, 1 = brightness mode
color_hue = 0   # 0-255 for color wheel position
brightness = 0.3  # 0.0-1.0 for LED brightness

def wheel(pos):
    """
    Color wheel for making rainbow colors.
    Input: 0-255 position on wheel
    Output: (r, g, b) tuple
    """
    pos = pos % 255  # Keep position in valid range
    
    if pos < 85:  # Red to Green
        return (255 - pos * 3, pos * 3, 0)
    elif pos < 170:  # Green to Blue
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    else:  # Blue to Red
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)

# Main loop
while True:
    # Check for rotation
    change = encoder.read_encoder()
    
    if change != 0:  # If encoder was turned
        if mode == 0:  # Color mode
            # Update color (0-255)
            color_hue = (color_hue + change * 5) % 256
            # Set all pixels to new color
            cp.pixels.fill(wheel(color_hue))
        else:  # Brightness mode
            # Update brightness (0.1-1.0)
            brightness = max(0.1, min(1.0, brightness + change * 0.05))
            cp.pixels.brightness = brightness
    
    # Check for button press
    if encoder.button_pressed():
        mode = (mode + 1) % 2  # Toggle between modes
        # Flash pixels off briefly to show mode change
        cp.pixels.fill((0, 0, 0))
        time.sleep(0.1)
        cp.pixels.fill(wheel(color_hue))
    
    # Small delay to prevent overwhelming the board
    time.sleep(0.01)
```


## Troubleshooting Guide

### Common Issues
1. Encoder not responding
   - Check ground connections
   - Verify both middle pin and switch are grounded
   - Ensure proper pin assignments in code
   
2. Erratic behavior
   - Add or increase debounce delay
   - Check for loose connections
   - Make sure each pin is in its own breadboard row

3. NeoPixels not updating
   - Check code is properly uploaded
   - Verify pixel settings in code
   - Reset Circuit Playground Express

## Circuit Diagram
```
Circuit Playground Express    Rotary Encoder (3-pin side)
A1 --------------------- Channel A (left pin)
GND -------------------- Common (middle pin)
A2 --------------------- Channel B (right pin)

Circuit Playground Express    Rotary Encoder (2-pin side)
A3 --------------------- Switch Pin 1
GND -------------------- Switch Pin 2
```

## Extension Activities
1. Add different control modes:
   - Animation speed control
   - Pattern selection
   - Sound control
   
2. Create a game:
   - Simon Says with encoder movements
   - Reaction timer
   - Pattern matching challenge

## Additional Resources
- [Circuit Playground Express Pinout Guide](https://learn.adafruit.com/adafruit-circuit-playground-express/pinouts)
- [Rotary Encoder Documentation](https://learn.adafruit.com/rotary-encoder)
- [CircuitPython NeoPixel Guide](https://learn.adafruit.com/circuitpython-essentials/circuitpython-neopixel)

## Parent/Teacher Notes
- Help with initial wiring setup
- Supervise breadboard connections
- Assist with understanding rotation direction
- Guide through troubleshooting steps
- Encourage experimentation with different modes
- Help with code modifications

Remember to save your code as `code.py` on the Circuit Playground Express and ensure all necessary libraries are installed in the `lib` folder.
