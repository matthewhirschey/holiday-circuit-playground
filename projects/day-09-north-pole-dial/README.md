# Day 9: Interactive North Pole Dial

## Project Overview
Transform your Circuit Playground Express into an interactive control station using a rotary encoder! Create a digital North Pole command center that can control lights, animations, and special effects.

**Difficulty**: ⭐⭐⭐ (Intermediate)  
**Duration**: 45-60 minutes  
**Project Type**: 🎮 Interactive Control

## What You'll Learn
- How rotary encoders work as digital inputs
- Reading and processing multiple input signals
- Creating interactive control interfaces
- Basic state management in code
- Working with hardware interrupts (Age 13)

## Required Materials
- Circuit Playground Express
- Rotary Encoder (PID: 377)
- Mini Breadboard
- 5x Jumper Wires (male-to-male)
- USB Cable for programming

## Hardware Overview
A rotary encoder is like a digital knob that can turn endlessly in either direction. Unlike a potentiometer, it doesn't have stops and can track relative movement. The encoder we're using includes:

- CLK (Clock/Pin A): Sends pulses as you turn
- DT (Data/Pin B): Helps determine rotation direction
- SW: Built-in pushbutton
- VCC: Power input (3.3V)
- GND: Ground connection

## Safety First! ⚡
- Always disconnect power before making connections
- Handle the encoder gently - the pins can bend
- Use static protection when handling components
- Maximum voltage: 3.3V (DO NOT use 5V with Circuit Playground Express)
- Keep workspace clean and organized
- Adult supervision required for soldering (if needed)

## Instructions for Age 9

### 1. Understanding Your Encoder
Before we start building, let's understand how our digital knob works:
- Turning right makes "clicking" sounds - we'll use these for increasing values
- Turning left also clicks - we'll use these for decreasing values
- The button on top can be pressed to change modes
- Inside are special sensors that tell us which way you're turning

### 2. Building the Circuit
1. Power Setup
   - Connect red jumper wire from 3.3V to breadboard's red (+) rail
   - Connect black jumper wire from GND to breadboard's blue (-) rail

2. Encoder Connection
   - Place encoder in breadboard, straddling the center gap
   - Connect GND pin to blue (-) rail
   - Connect VCC pin to red (+) rail
   - Connect CLK to Circuit Playground A1
   - Connect DT to Circuit Playground A2
   - Connect SW to Circuit Playground A3

### 3. Basic Operation
- Turn right = Next color
- Turn left = Previous color
- Press button = Change brightness mode
- In brightness mode: right = brighter, left = dimmer

## Instructions for Age 13

### 1. Advanced Hardware Setup
```python
import time
import board
import digitalio
from adafruit_circuitplayground import cp

# Encoder Setup
class RotaryEncoder:
    def __init__(self, clk_pin, dt_pin, sw_pin):
        # Initialize pins
        self.clk = digitalio.DigitalInOut(clk_pin)
        self.dt = digitalio.DigitalInOut(dt_pin)
        self.sw = digitalio.DigitalInOut(sw_pin)
        
        # Set pin directions
        self.clk.direction = digitalio.Direction.INPUT
        self.dt.direction = digitalio.Direction.INPUT
        self.sw.direction = digitalio.Direction.INPUT
        
        # Enable pullup on button
        self.sw.pull = digitalio.Pull.UP
        
        # State tracking
        self.last_clk = self.clk.value
        self.position = 0
        self.last_button = time.monotonic()
        
    def update(self):
        """Read encoder and return position change"""
        position_change = 0
        
        # Check rotation
        current_clk = self.clk.value
        if current_clk != self.last_clk:
            if self.dt.value != current_clk:
                position_change = 1
            else:
                position_change = -1
        self.last_clk = current_clk
        
        return position_change
    
    def button_pressed(self):
        """Check if button is pressed with debounce"""
        if not self.sw.value:
            current_time = time.monotonic()
            if current_time - self.last_button > 0.2:
                self.last_button = current_time
                return True
        return False

# Create encoder instance
encoder = RotaryEncoder(
    clk_pin=board.A1,
    dt_pin=board.A2,
    sw_pin=board.A3
)

# Main control loop
mode = 0  # 0 = color, 1 = brightness
color_index = 0
brightness = 0.3

while True:
    # Update encoder position
    change = encoder.update()
    
    # Handle rotation
    if change != 0:
        if mode == 0:
            # Color mode
            color_index = (color_index + change) % 256
            cp.pixels.fill((color_index, 255 - color_index, 128))
        else:
            # Brightness mode
            brightness = max(0.1, min(1.0, brightness + change * 0.05))
            cp.pixels.brightness = brightness
    
    # Handle button press
    if encoder.button_pressed():
        mode = (mode + 1) % 2
        cp.pixels.fill((0, 0, 0))
        time.sleep(0.1)
    
    # Small delay to prevent overwhelming the board
    time.sleep(0.01)
```

## Troubleshooting Guide

### Common Issues
1. Encoder not responding
   - Check all wire connections
   - Verify 3.3V power connection
   - Ensure proper pin assignments in code
   
2. Erratic behavior
   - Add or increase debounce delay
   - Check for loose connections
   - Verify ground connection

3. NeoPixels not updating
   - Check NeoPixel power connection
   - Verify pixel count in code
   - Reset Circuit Playground Express

## Extension Activities
1. Add different control modes:
   - Animation speed control
   - Pattern selection
   - Sound control
   
2. Create a game:
   - Simon Says with encoder movements
   - Reaction timer
   - Pattern matching challenge

## Circuit Diagram
```
Circuit Playground Express    Rotary Encoder
3.3V -------------------- VCC
GND --------------------- GND
A1 --------------------- CLK
A2 --------------------- DT
A3 --------------------- SW
```

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
