# Day 15: Candy Cane Lights

## Overview
Today we'll create a light-up candy cane using NeoPixel Diffused 8mm Through-Hole LEDs! These special LEDs can each change color independently and can be chained together. We'll learn how to connect them properly on a breadboard and create festive patterns.

## Materials Needed
- Circuit Playground Express
- NeoPixel Diffused 8mm Through-Hole LEDs (5 pack)
- Mini Breadboard (from previous days)
- Jumper Wires
- Cardboard/paper for candy cane shape
- Red and white decorative materials

## Understanding Your NeoPixels
- Each LED has 4 pins in this order:
  1. VDD (Power, 3.3-5V)
  2. GND (Ground)
  3. DI (Data In)
  4. DO (Data Out)
- They work in a chain: DO of one connects to DI of next
- Built-in drivers (no extra resistors needed)
- Flat side/indent shows pin 1 (VDD)

## Instructions for Age 9

1. Plan Your Candy Cane:
   - Draw candy cane shape on cardboard
   - Mark spots for 5 LEDs
   - Space them evenly

2. Breadboard Setup:
   - Power rails (like previous days):
     - Red jumper from 3.3V to + rail
     - Black jumper from GND to - rail

3. Connect First LED:
   - Find pin 1 (look for flat side)
   - Place LED in breadboard
   - Connect VDD (pin 1) to + rail
   - Connect GND (pin 2) to - rail
   - Connect DI (pin 3) to A1 on Circuit Playground
   - DO (pin 4) will connect to next LED

4. Connect Additional LEDs:
   - Place each LED in breadboard
   - VDD to + rail
   - GND to - rail
   - DI connects to previous LED's DO
   - Continue chain for all LEDs

5. Test Your Lights:
   - Press A for red/white pattern
   - Press B for moving light effect
   - Both buttons for rainbow pattern!

## Instructions for Age 13

1. Advanced Setup:
   - Follow basic connection steps
   - Plan efficient wire routing
   - Consider future expansion

2. Basic LED Code:
```python
import time
import board
import neopixel

# Set up NeoPixel strip - 5 LEDs on pin A1
pixels = neopixel.NeoPixel(board.A1, 5, brightness=0.3)

# Define candy cane colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Example pattern
while True:
    # Alternate red and white
    for i in range(5):
        if i % 2 == 0:
            pixels[i] = RED
        else:
            pixels[i] = WHITE
    time.sleep(1)
```

3. Testing Tips:
- Test each LED individually first
- Verify pin orientations
- Check all power connections
- Ensure data chain is correct

## Troubleshooting

1. LEDs Not Lighting?
   - Check pin 1 orientation (flat side)
   - Verify power connections
   - Test data chain sequence
   - Check code pin assignment

2. Wrong Colors/Pattern?
   - Verify power is stable
   - Check data connections
   - Test LEDs one at a time
   - Debug code sequence

## Extensions

### For 9-Year-Olds:
1. Change pattern speeds
2. Try different colors
3. Add more LEDs
4. Make multiple candy canes

### For 13-Year-Olds:
1. Create spinning effects
2. Add motion sensing
3. Sync multiple canes
4. Make interactive patterns

## Safety Notes
- Handle LEDs gently
- Mind pin orientation
- Don't force into breadboard
- Keep connections secure

## Parent Notes
- Help identify pin 1
- Guide breadboard layout
- Assist with chaining
- Support testing process